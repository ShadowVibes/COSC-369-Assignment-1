from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.shared import Inches, Pt
from datetime import datetime

INPUT_FILE = "formatted_schedule.txt"
OUTPUT_FILE = "Final_Schedule.docx"

# Change this to a professor's name to show only their classes.
# Use "ALL" to show every class.
TEACHER_NAME = "ALL"


def format_time(value):
    value = value.strip()

    if value == "N/A" or "Asynchronous" in value:
        return value

    try:
        time_value = datetime.strptime(value, "%H:%M:%S")
        return time_value.strftime("%I:%M %p").lstrip("0")
    except ValueError:
        return value


def format_days(days):
    day_names = {
        "M": "Monday",
        "T": "Tuesday",
        "W": "Wednesday",
        "R": "Thursday",
        "F": "Friday"
    }

    if days == "N/A":
        return "Online Asynchronous"

    names = []

    for letter in days:
        if letter in day_names:
            names.append(day_names[letter])

    if len(names) == 1:
        return names[0]

    if len(names) == 2:
        return f"{names[0]} & {names[1]}"

    if len(names) > 2:
        return ", ".join(names[:-1]) + f" & {names[-1]}"

    return days


def read_schedule():
    courses = []
    office_hours = ""

    current_course = None
    reading_office_hours = False

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if not line:
                continue

            if line == "OFFICE HOURS":
                if current_course:
                    courses.append(current_course)
                    current_course = None

                reading_office_hours = True
                continue

            if reading_office_hours:
                if line.startswith("Office Hours:"):
                    office_hours = line.replace(
                        "Office Hours:", "", 1
                    ).strip()

                continue

            if line.startswith("Course ID:"):
                if current_course:
                    courses.append(current_course)

                current_course = {
                    "course": line.replace("Course ID:", "").strip(),
                    "title": "",
                    "begin": "",
                    "end": "",
                    "days": "",
                    "room": "",
                    "instructor": ""
                }

            elif current_course:
                if line.startswith("Title:"):
                    current_course["title"] = (
                        line.replace("Title:", "").strip()
                    )

                elif line.startswith("Begin:"):
                    current_course["begin"] = (
                        line.replace("Begin:", "").strip()
                    )

                elif line.startswith("End:"):
                    current_course["end"] = (
                        line.replace("End:", "").strip()
                    )

                elif line.startswith("Days:"):
                    current_course["days"] = (
                        line.replace("Days:", "").strip()
                    )

                elif line.startswith("Room:"):
                    current_course["room"] = (
                        line.replace("Room:", "").strip()
                    )

                elif line.startswith("Instructor:"):
                    current_course["instructor"] = (
                        line.replace("Instructor:", "").strip()
                    )

    if current_course:
        courses.append(current_course)

    return courses, office_hours


def create_document(courses, instructor_name, office_hours):
    document = Document()

    section = document.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Inches(11)
    section.page_height = Inches(8.5)

    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.4)
    section.right_margin = Inches(0.4)

    heading = document.add_paragraph()

    heading_run = heading.add_run("CLASS SCHEDULE")
    heading_run.bold = True
    heading_run.font.size = Pt(16)

    instructor_paragraph = document.add_paragraph()

    instructor_run = instructor_paragraph.add_run(
        f"Instructor: {instructor_name}"
    )
    instructor_run.bold = True
    instructor_run.font.size = Pt(12)

    table = document.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    header_cells = table.rows[0].cells

    header_cells[0].width = Inches(2.6)
    header_cells[1].width = Inches(6.0)
    header_cells[2].width = Inches(1.2)

    headers = ["Course", "Times", "Location"]

    for index, title in enumerate(headers):
        paragraph = header_cells[index].paragraphs[0]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = paragraph.add_run(title)
        run.bold = True
        run.font.size = Pt(12)

    for course in courses:
        row = table.add_row().cells

        row[0].width = Inches(2.6)
        row[1].width = Inches(6.0)
        row[2].width = Inches(1.2)

        for cell in row:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP

        course_paragraph = row[0].paragraphs[0]
        course_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        course_run = course_paragraph.add_run(course["course"])
        course_run.bold = True
        course_run.font.size = Pt(10)

        title_run = course_paragraph.add_run(
            f"\n({course['title']})"
        )
        title_run.bold = True
        title_run.font.size = Pt(9)

        begin = format_time(course["begin"])
        end = format_time(course["end"])
        days = format_days(course["days"])

        if "Asynchronous" in begin or days == "Online Asynchronous":
            time_text = "Online Asynchronous Course"

        elif end == "N/A":
            time_text = f"{days} {begin}"

        else:
            time_text = f"{days} {begin} to {end}"

        time_paragraph = row[1].paragraphs[0]

        time_run = time_paragraph.add_run(time_text)
        time_run.bold = True
        time_run.font.size = Pt(10)

        location_paragraph = row[2].paragraphs[0]
        location_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        location_run = location_paragraph.add_run(course["room"])
        location_run.bold = True
        location_run.font.size = Pt(10)

    document.add_paragraph()

    office_heading = document.add_paragraph()

    office_heading_run = office_heading.add_run("OFFICE HOURS")
    office_heading_run.bold = True
    office_heading_run.font.size = Pt(16)

    note = document.add_paragraph()

    note_run = note.add_run(
        "NOTE: Instructors are not to be interrupted during class times."
    )
    note_run.bold = True

    office_table = document.add_table(rows=1, cols=1)
    office_table.style = "Table Grid"

    cell = office_table.cell(0, 0)

    paragraph = cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    if instructor_name == "All Instructors":
        if office_hours:
            office_text = (
                "Dr. Appolo Tankeh — "
                "Tuesday & Thursday: 10:45 AM – 1:00 PM"
            )
        else:
            office_text = "No office hours were provided."

    elif "tankeh" in instructor_name.lower() and office_hours:
        office_text = (
            "Dr. Appolo Tankeh — "
            "Tuesday & Thursday: 10:45 AM – 1:00 PM"
        )

    else:
        office_text = (
            "Office hours were not provided for this instructor "
            "in the supplied files."
        )

    run = paragraph.add_run(office_text)
    run.bold = True
    run.font.size = Pt(14)

    document.save(OUTPUT_FILE)

    print(f"Created {OUTPUT_FILE}")


courses, office_hours = read_schedule()

if TEACHER_NAME.upper() == "ALL":
    filtered_courses = courses
    instructor_name = "All Instructors"

else:
    filtered_courses = [
        course for course in courses
        if TEACHER_NAME.lower() in course["instructor"].lower()
    ]

    if filtered_courses:
        instructor_name = filtered_courses[0]["instructor"]


if not filtered_courses:
    print(f"No classes found for instructor: {TEACHER_NAME}")

else:
    print(f"Found {len(filtered_courses)} class(es).")

    create_document(
        filtered_courses,
        instructor_name,
        office_hours
    )