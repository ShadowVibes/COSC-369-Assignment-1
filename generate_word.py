
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


FOLDER = Path(__file__).resolve().parent
INPUT_FILE = FOLDER / "formatted_schedule.txt"
KNOWLEDGE_BASE = FOLDER / "knowledge_base.pl"
OUTPUT_FILE = FOLDER / "Final_Schedule.docx"

# Change to a professor's name to filter results.
TEACHER_NAME = "ALL"
BLUE = RGBColor(54, 95, 145)


def prolog_facts(predicate, count):
    """Read matching facts from the Prolog knowledge base."""
    if not KNOWLEDGE_BASE.exists():
        return []

    pattern = re.compile(rf"^{re.escape(predicate)}\((.*)\)\.$")
    atoms = re.compile(r"'((?:''|[^'])*)'")
    facts = []

    for line in KNOWLEDGE_BASE.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line.strip())
        if match:
            values = [v.replace("''", "'") for v in atoms.findall(match.group(1))]
            if len(values) == count:
                facts.append(values)

    return facts


def format_time(value):
    """Convert 24-hour time to 12-hour time."""
    value = str(value).strip()
    for fmt in ("%H:%M:%S", "%H:%M"):
        try:
            return datetime.strptime(value, fmt).strftime("%I:%M %p").lstrip("0")
        except ValueError:
            pass
    return value


def format_office_hours(value):
    """Standardize office-hour time ranges."""
    value = re.sub(
        r"^(?:Tue/Thursday|Tuesday/Thursday)\s*:\s*",
        "",
        value.replace("Office Hours:", "").strip(),
        flags=re.I
    )

    match = re.fullmatch(r"(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})", value)
    if match:
        return f"{format_time(match[1])} – {format_time(match[2])}"

    match = re.fullmatch(
        r"(\d{1,2}(?::\d{2})?)\s*-\s*(\d{1,2}(?::\d{2})?)\s*([ap]m)",
        value, re.I
    )
    if match:
        start, end, period = match.groups()
        period = period.upper()
        start_period = "AM" if period == "PM" and int(start.split(":")[0]) > int(end.split(":")[0]) else period
        return (
            f"{start if ':' in start else start + ':00'} {start_period} – "
            f"{end if ':' in end else end + ':00'} {period}"
        )

    return value


def format_days(value):
    """Convert weekday codes to readable names."""
    names = {"M": "Monday", "T": "Tuesday", "W": "Wednesday",
             "R": "Thursday", "F": "Friday"}
    value = value.strip().upper()

    if value in ("", "N/A", "UNKNOWN"):
        return "Online Asynchronous"

    days = [names[c] for c in value if c in names]
    return ", ".join(days[:-1]) + " & " + days[-1] if len(days) > 1 else (
        days[0] if days else value
    )


def normalize_name(name):
    """Remove titles and standardize names for searching."""
    name = re.sub(r"\b(?:dr|professor|prof)\.?\s*", "", name, flags=re.I)
    return set(re.findall(r"[a-z]+", name.lower()))


def read_courses():
    """Extract course records from the formatted text file."""
    if not INPUT_FILE.exists():
        print("Missing formatted_schedule.txt.")
        return []

    fields = {"Course ID": "course", "Title": "title", "Begin": "begin",
              "End": "end", "Days": "days", "Room": "room",
              "Instructor": "instructor"}
    courses, current = [], None

    for raw in INPUT_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        if line.upper() in ("OFFICE HOURS", "SYLLABUS OFFICE HOURS",
                            "FACULTY OFFICE HOURS"):
            break

        if line.startswith("Course ID:"):
            if current:
                courses.append(current)
            current = dict.fromkeys(fields.values(), "")

        if current is not None and ":" in line:
            label, value = line.split(":", 1)
            if label in fields:
                current[fields[label]] = value.strip()

    if current:
        courses.append(current)
    return courses


def load_office_hours():
    """Collect office hours without duplicate entries."""
    hours = defaultdict(list)

    for professor, day, time in prolog_facts("office_hours", 3):
        entry = (day.title(), format_office_hours(time))
        if entry not in hours[professor]:
            hours[professor].append(entry)

    return hours


def style_cell(cell, bold=False, header=False):
    """Apply padding, font styling, and optional header shading."""
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    tc_pr = cell._tc.get_or_add_tcPr()

    margins = tc_pr.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tc_pr.append(margins)

    for side in ("top", "bottom", "left", "right"):
        element = margins.find(qn(f"w:{side}"))
        if element is None:
            element = OxmlElement(f"w:{side}")
            margins.append(element)
        element.set(qn("w:w"), "110")
        element.set(qn("w:type"), "dxa")

    if header:
        shading = OxmlElement("w:shd")
        shading.set(qn("w:fill"), "EAF0F7")
        tc_pr.append(shading)

    for paragraph in cell.paragraphs:
        paragraph.paragraph_format.space_after = Pt(0)
        paragraph.paragraph_format.line_spacing = 1.1
        for run in paragraph.runs:
            run.font.name = "Calibri"
            run.font.size = Pt(11)
            if bold:
                run.bold = True


def make_table(document, headers, widths):
    """Create a formatted table with a repeating header."""
    table = document.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.autofit = False

    for i, heading in enumerate(headers):
        table.columns[i].width = Inches(widths[i])
        cell = table.rows[0].cells[i]
        cell.width = Inches(widths[i])
        cell.text = heading
        style_cell(cell, bold=True, header=True)

    repeat = OxmlElement("w:tblHeader")
    repeat.set(qn("w:val"), "true")
    table.rows[0]._tr.get_or_add_trPr().append(repeat)
    return table


def add_row(table, values, widths, bold_first=False):
    """Add a styled table row without splitting across pages."""
    row = table.add_row()

    for i, value in enumerate(values):
        cell = row.cells[i]
        cell.width = Inches(widths[i])
        cell.text = str(value)
        style_cell(cell)

        if bold_first and i == 0:
            cell.paragraphs[0].runs[0].bold = True

    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
    return row


def add_heading(document, title):
    """Create a blue section heading."""
    heading = document.add_heading(title, level=1)
    heading.paragraph_format.space_before = Pt(12)
    heading.paragraph_format.space_after = Pt(8)

    for run in heading.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(16)
        run.font.color.rgb = BLUE
        run.bold = True


def add_schedule_table(document, courses):
    """Create the four-column class schedule."""
    widths = [2.0, 2.1, 4.2, 1.7]
    table = make_table(
        document, ["Course", "Instructor", "Schedule", "Location"], widths
    )

    for course in courses:
        begin, end = format_time(course["begin"]), format_time(course["end"])
        days = format_days(course["days"])

        if "asynchronous" in begin.lower():
            schedule = "Online Asynchronous"
        elif not end or end.lower() in ("n/a", "unknown"):
            schedule = f"{days}, {begin}"
        else:
            schedule = f"{days}, {begin} – {end}"

        row = add_row(table, [
            f"{course['course']}\n{course['title']}",
            course["instructor"] or "Not provided",
            schedule,
            course["room"] or "Not provided"
        ], widths)

        # Bold only the course number, not the title.
        paragraph = row.cells[0].paragraphs[0]
        paragraph.clear()
        number = paragraph.add_run(course["course"])
        number.bold = True
        paragraph.add_run("\n" + course["title"])
        style_cell(row.cells[0])


def add_office_hours(document, hours, selected):
    """Create the office-hours table with professor filtering."""
    add_heading(document, "OFFICE HOURS")
    document.add_paragraph(
        "NOTE: Instructors are not to be interrupted during class times."
    )

    note = document.add_paragraph(
        "Additional faculty office hours are sample demonstration data "
        "and have not been verified."
    )
    for run in note.runs:
        run.italic = True
        run.font.size = Pt(10)

    widths = [3.2, 6.8]
    table = make_table(document, ["Professor", "Office Hours"], widths)
    found = False

    for professor in sorted(hours):
        if selected.upper() != "ALL" and not normalize_name(selected).issubset(
            normalize_name(professor)
        ):
            continue

        found = True
        schedule = "; ".join(f"{day}: {time}" for day, time in hours[professor])
        add_row(table, [professor, schedule], widths)

    if not found:
        add_row(
            table,
            [selected if selected.upper() != "ALL" else "All faculty",
             "Office hours not provided"],
            widths
        )


def create_document():
    """Generate the final Word schedule."""
    courses = read_courses()
    hours = load_office_hours()

    if not courses and not hours:
        print("No schedule or office-hour information found.")
        return

    selected = TEACHER_NAME.strip()

    if selected.upper() != "ALL":
        courses = [
            course for course in courses
            if normalize_name(selected).issubset(
                normalize_name(course["instructor"])
            )
        ]

    document = Document()
    section = document.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width, section.page_height = Inches(11), Inches(8.5)
    section.top_margin = section.bottom_margin = Inches(0.6)
    section.left_margin = section.right_margin = Inches(0.5)

    normal = document.styles["Normal"]
    normal.font.name, normal.font.size = "Calibri", Pt(11)
    normal.paragraph_format.space_after = Pt(6)

    title = document.add_heading("FACULTY CLASS SCHEDULE", level=0)
    for run in title.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(20)
        run.font.color.rgb = BLUE
        run.bold = True

    document.add_paragraph(
        "Instructor: " + (
            "All Instructors" if selected.upper() == "ALL" else selected
        )
    )

    add_heading(document, "TEACHING SCHEDULE")
    if courses:
        add_schedule_table(document, courses)
    else:
        document.add_paragraph("No matching classes found.")

    add_office_hours(document, hours, selected)

    try:
        document.save(OUTPUT_FILE)
        print(f"Created: {OUTPUT_FILE.name}")
        print(f"Courses included: {len(courses)}")
        print(f"Faculty with office hours: {len(hours)}")
    except PermissionError:
        print("Close the Word document and run the program again.")


if __name__ == "__main__":
    create_document()
