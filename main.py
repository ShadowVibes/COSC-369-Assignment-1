
import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from docx import Document

FOLDER = Path(__file__).resolve().parent

DAY_NAMES = {
    "M": "monday",
    "T": "tuesday",
    "W": "wednesday",
    "R": "thursday",
    "F": "friday"
}

DAY_PATTERNS = {
    "monday": r"\bmon(?:day)?\b",
    "tuesday": r"\btue(?:s(?:day)?)?\b",
    "wednesday": r"\bwed(?:nesday)?\b",
    "thursday": r"\bthu(?:r(?:s(?:day)?)?)?\b",
    "friday": r"\bfri(?:day)?\b"
}


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def clean(value):
    """Convert empty or missing values to Unknown."""
    if pd.isna(value) or str(value).strip().lower() in (
        "", "n/a", "not available", "nan"
    ):
        return "Unknown"
    return str(value).strip()


def atom(value):
    """Escape text for use in Prolog facts."""
    value = clean(value).replace("\\", "\\\\").replace("'", "''")
    return f"'{value}'"


def time_text(value):
    """Convert Excel time values to 24-hour format."""
    if pd.isna(value):
        return "Unknown"
    return value.strftime("%H:%M") if hasattr(value, "strftime") else clean(value)


def weekdays(value):
    """Recognize full weekday names, abbreviations, and day codes."""
    text = clean(value).lower()

    if text == "unknown":
        return []

    found = [
        day for day, pattern in DAY_PATTERNS.items()
        if re.search(pattern, text)
    ]

    if found:
        return found

    code = text.upper().strip()

    if re.fullmatch(r"[MTWRF]+", code):
        return list(dict.fromkeys(DAY_NAMES[letter] for letter in code))

    return []


def syllabus_time(value):
    """Convert syllabus times such as 9:30AM to 09:30."""
    value = re.sub(r"\s+", "", value.upper())

    for fmt in ("%I:%M%p", "%I%p"):
        try:
            return datetime.strptime(value, fmt).strftime("%H:%M")
        except ValueError:
            continue

    return "Unknown"


# --------------------------------------------------
# Read input files
# --------------------------------------------------

def read_enrollment():
    """Read class sections from the first Excel sheet."""
    df = pd.read_excel(
        FOLDER / "Enrollment info.xlsx",
        sheet_name=0
    )

    sections = []

    for _, row in df.iterrows():
        section_id = clean(row["ID"])

        sections.append({
            "section_id": section_id,
            "course_id": section_id.split(".")[0],
            "title": clean(row["Course Title"]).split("(")[0].strip(),
            "begin": time_text(row["Begin"]),
            "end": time_text(row["End "]),
            "days": clean(row["Days"]),
            "room": clean(row["Room"]),
            "instructor": clean(row["Instructor 2025"])
        })

    return sections


def read_syllabus():
    """Extract course details and instructor information."""
    doc = Document(FOLDER / "Syllabus.docx")
    lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    text = "\n".join(lines)

    def field(label):
        for line in lines:
            if line.lower().startswith(label.lower() + ":"):
                return line.split(":", 1)[1].strip()
        return "Unknown"

    match = re.search(
        r"\b([A-Z]{2,6}\s*\d{3})\s*\(\d+\s*Cr\)\s*(.*)",
        text, re.I
    )

    course_id = (
        re.sub(r"\s+", " ", match.group(1)).upper()
        if match else "Unknown"
    )

    if course_id == "COSC 365":
        course_id = "COSC 369"

    title = match.group(2).strip() if match else "Unknown"

    title = re.split(
        r"\b(?:Fall|Spring|Summer)\s+Semester\b",
        title, maxsplit=1, flags=re.I
    )[0].strip()

    class_hours = field("Class Hours")

    times = re.findall(
        r"\d{1,2}(?::\d{2})?\s*[AP]M",
        class_hours, re.I
    )

    begin, end = (
        (syllabus_time(times[0]), syllabus_time(times[1]))
        if len(times) >= 2 else ("Unknown", "Unknown")
    )

    details = {
        "professor": field("Instructor"),
        "office": field("Office Location"),
        "email": field("Email"),
        "office_hours": field("Office Hours")
    }

    days = weekdays(class_hours)
    day_codes = {name: code for code, name in DAY_NAMES.items()}

    section = {
        "section_id": course_id,
        "course_id": course_id,
        "title": title,
        "begin": begin,
        "end": end,
        "days": "".join(day_codes[day] for day in days) if days else "Unknown",
        "room": details["office"],
        "instructor": details["professor"]
    }

    return section, details


def read_faculty():
    """Read faculty profiles from the Faculty_Info Excel sheet."""
    df = pd.read_excel(
        FOLDER / "Enrollment info.xlsx",
        sheet_name="Faculty_Info",
        dtype=str
    ).fillna("")

    # Match Excel column names to the names used by the program.
    df.columns = df.columns.str.strip()

    df = df.rename(columns={
        "Email (generated, unverified)": "Email",
        "Office Days (sample)": "Office Days",
        "Office Hours (sample)": "Office Hours",
        "Office Location (sample)": "Office",
        "Appointment Policy (sample)": "Appointment"
    })

    return df.to_dict(orient="records")


# --------------------------------------------------
# Generate combined schedule for C
# --------------------------------------------------

def write_combined(sections, office_hours, faculty):
    """Create the class schedule and faculty office hours for C."""
    courses = {section["course_id"]: section for section in sections}
    path = FOLDER / "Combined_Schedule_Office_Hours.txt"

    labels = {
        "Course ID": "course_id",
        "Title": "title",
        "Begin": "begin",
        "End": "end",
        "Days": "days",
        "Room": "room",
        "Instructor": "instructor"
    }

    with path.open("w", encoding="utf-8") as file:
        file.write("Combined Class Schedule and Office Hours\n")
        file.write("=" * 50 + "\n")

        # Write class schedules
        for section in courses.values():
            for label, key in labels.items():
                file.write(f"{label}: {section[key]}\n")

            file.write("-" * 30 + "\n")

        # Write syllabus office hours
        if office_hours != "Unknown":
            file.write("\nSyllabus Office Hours\n")
            file.write(f"Office Hours: {office_hours}\n")
            file.write("-" * 30 + "\n")

        # Write faculty office hours
        file.write("\nFaculty Office Hours\n")
        file.write("=" * 50 + "\n")
        file.write(
            "Note: Faculty office hours below are sample "
            "demonstration data, not verified schedules.\n\n"
        )

        for person in faculty:
            name = clean(person.get("Professor", ""))
            days = clean(person.get("Office Days", ""))
            hours = clean(person.get("Office Hours", ""))

            if name == "Unknown":
                continue

            file.write(f"Professor: {name}\n")

            if days != "Unknown":
                file.write(f"Office Days: {days}\n")

            if hours != "Unknown":
                file.write(f"Office Hours: {hours}\n")
            else:
                file.write("Office Hours: Not provided\n")

            file.write("-" * 30 + "\n")


# --------------------------------------------------
# Generate Prolog knowledge base
# --------------------------------------------------

def write_knowledge_base(sections, syllabus, faculty):
    """Generate course facts, faculty facts, and Prolog rules."""
    path = FOLDER / "knowledge_base.pl"

    predicates = [
        "course_section/2",
        "teaches/2",
        "teaches_section/2",
        "course_title/2",
        "class_schedule/5",
        "meets_on/2",
        "office_hours/3",
        "faculty_member/1",
        "faculty_department/2",
        "faculty_email/2",
        "faculty_office/2",
        "faculty_appointment/2"
    ]

    with path.open("w", encoding="utf-8") as file:
        file.write("% COSC 369 - Prolog Knowledge Base\n\n")

        for predicate in predicates:
            file.write(f":- discontiguous {predicate}.\n")

        # Course information
        file.write("\n% Course information\n\n")

        for section in sections:
            sid = atom(section["section_id"])
            cid = atom(section["course_id"])
            prof = atom(section["instructor"])

            facts = [
                f"course_section({sid}, {cid})",
                f"teaches({prof}, {cid})",
                f"teaches_section({prof}, {sid})",
                f"course_title({cid}, {atom(section['title'])})",
                f"class_schedule({sid}, {atom(section['days'])}, "
                f"{atom(section['begin'])}, {atom(section['end'])}, "
                f"{atom(section['room'])})"
            ]

            facts.extend(
                f"meets_on({sid}, {atom(day)})"
                for day in weekdays(section["days"])
            )

            file.write(".\n".join(facts) + ".\n\n")

        # Syllabus faculty information
        file.write("% Syllabus faculty information\n\n")

        if syllabus["professor"] != "Unknown":
            prof = atom(syllabus["professor"])
            file.write(f"faculty_member({prof}).\n")

            for key, predicate in (
                ("email", "faculty_email"),
                ("office", "faculty_office")
            ):
                if syllabus[key] != "Unknown":
                    file.write(f"{predicate}({prof}, {atom(syllabus[key])}).\n")

            if syllabus["office_hours"] != "Unknown":
                file.write(
                    f"syllabus_office_hours({atom(syllabus['office_hours'])}).\n"
                )

                for day in weekdays(syllabus["office_hours"]):
                    file.write(
                        f"office_hours({prof}, {atom(day)}, "
                        f"{atom(syllabus['office_hours'])}).\n"
                    )

        # Faculty information from Excel
        file.write("\n% Faculty information\n")
        file.write("% Sample office hours are not verified.\n\n")

        fields = {
            "Department": "faculty_department",
            "Email": "faculty_email",
            "Office": "faculty_office",
            "Appointment": "faculty_appointment"
        }

        for person in faculty:
            name = clean(person.get("Professor", ""))

            if name == "Unknown":
                continue

            prof = atom(name)
            file.write(f"faculty_member({prof}).\n")

            for column, predicate in fields.items():
                value = clean(person.get(column, ""))

                if value != "Unknown":
                    file.write(f"{predicate}({prof}, {atom(value)}).\n")

            days = clean(person.get("Office Days", ""))
            hours = clean(person.get("Office Hours", ""))

            if days != "Unknown" and hours != "Unknown":
                for day in weekdays(days):
                    file.write(
                        f"office_hours({prof}, {atom(day)}, {atom(hours)}).\n"
                    )

            file.write("\n")

        # Prolog rules
        file.write("""
% Prolog rules

teaches_course(P, C) :- teaches(P, C).
professor_courses(P, C) :- teaches(P, C).
section_instructor(S, P) :- teaches_section(P, S).

course_on_day(C, D) :-
    course_section(S, C),
    meets_on(S, D).

professor_teaches_on(P, D) :-
    teaches_section(P, S),
    meets_on(S, D).

professor_office_hours(P, D, H) :-
    office_hours(P, D, H).

faculty_search(Search, P) :-
    faculty_member(P),
    downcase_atom(Search, L),
    downcase_atom(P, LP),
    sub_atom(LP, _, _, _, L).

professor_email(P, E) :- faculty_email(P, E).
professor_office(P, O) :- faculty_office(P, O).
professor_department(P, D) :- faculty_department(P, D).
""")


# --------------------------------------------------
# Main program
# --------------------------------------------------

def main():
    """Process input files and generate schedule data."""
    sections = read_enrollment()
    excel_count = len(sections)

    syllabus_section, syllabus = read_syllabus()

    if (
        syllabus_section["course_id"] != "Unknown"
        and syllabus["professor"] != "Unknown"
        and not any(
            s["course_id"] == syllabus_section["course_id"]
            and s["instructor"].lower() == syllabus["professor"].lower()
            for s in sections
        )
    ):
        sections.append(syllabus_section)

    faculty = read_faculty()

    write_combined(sections, syllabus["office_hours"], faculty)
    write_knowledge_base(sections, syllabus, faculty)

    print("Combined schedule file generated successfully!")
    print("Prolog knowledge base generated successfully!")
    print(f"Excel sections processed: {excel_count}")
    print(f"Total sections: {len(sections)}")
    print(f"Faculty profiles: {len(faculty)}")
    print(f"Syllabus course: {syllabus_section['course_id']}")


if __name__ == "__main__":
    main()
