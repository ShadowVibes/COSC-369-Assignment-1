
from pathlib import Path
from pyswip import Prolog
import re

# Load the Prolog knowledge base
prolog = Prolog()
kb_path = Path(__file__).resolve().parent / "knowledge_base.pl"

if not kb_path.exists():
    print("Knowledge base missing. Run main.py first.")
    raise SystemExit(1)

prolog.consult(str(kb_path))


def atom(value):
    """Convert text into a safe Prolog atom."""
    value = str(value).replace("\\", "\\\\").replace("'", "''")
    return f"'{value}'"


def query(statement):
    """Execute a Prolog query."""
    try:
        return list(prolog.query(statement))
    except Exception as error:
        print(f"Query error: {error}")
        return []


def normalize(name):
    """Standardize professor names for matching."""
    name = re.sub(r"\b(dr|professor|prof)\.?\s*", "", name, flags=re.I)
    return set(re.findall(r"[a-z]+", name.lower()))


def find_names(search):
    """Find professors by first name, last name, or full name."""
    results = query("teaches(P, _)")
    results += query("faculty_member(P)")

    names = {str(r["P"]) for r in results}
    words = normalize(search)

    return sorted(
        name for name in names
        if words and words.issubset(normalize(name))
    )


def find_courses(search):
    """Match a course number or complete course ID."""
    search = re.sub(r"\s+", "", search).upper()
    results = query("course_section(_, C)")
    courses = {str(r["C"]) for r in results}

    matches = []

    for course in courses:
        cleaned = re.sub(r"\s+", "", course).upper()
        number = re.search(r"\d+[A-Z]?$", cleaned)

        if cleaned == search or (
            search.isdigit()
            and number
            and number.group() == search
        ):
            matches.append(course)

    return sorted(matches)


def search_system(option, value):
    """Run searches using the Prolog knowledge base."""
    value = value.strip()

    if not value:
        print("\nPlease enter a search value.")
        return

    answers = []

    if option == "1":
        for course in find_courses(value):
            results = query(f"teaches_course(P, {atom(course)})")
            answers += [
                f"{course}: {r['P']}" for r in results
            ]

        print(f"\nProfessors teaching {value}:")

    elif option == "2":
        for name in find_names(value):
            results = query(f"professor_courses({atom(name)}, C)")
            answers += [
                f"{name}: {r['C']}" for r in results
            ]

        print(f"\nCourses taught by {value}:")

    elif option == "3":
        results = query(f"course_on_day(C, {atom(value.lower())})")
        answers = [str(r["C"]) for r in results]
        print(f"\nCourses meeting on {value.title()}:")

    elif option == "4":
        names = find_names(value)

        for name in names:
            results = query(
                f"professor_office_hours({atom(name)}, D, H)"
            )
            answers += [
                f"{name} - {r['D']}: {r['H']}"
                for r in results
            ]

        print(f"\nOffice hours for {value}:")

    elif option == "5":
        results = query(
            f"class_schedule({atom(value.upper())}, D, B, E, R)"
        )

        answers = [
            f"Days: {r['D']} | Time: {r['B']} - {r['E']} | Room: {r['R']}"
            for r in results
        ]

        print(f"\nSchedule for {value.upper()}:")

    elif option == "6":
        names = find_names(value)

        for name in names:
            print(f"\n--- {name} ---")

            fields = {
                "Department": "faculty_department",
                "Email": "faculty_email",
                "Office": "faculty_office",
                "Appointment": "faculty_appointment"
            }

            for label, predicate in fields.items():
                results = query(f"{predicate}({atom(name)}, V)")
                answer = str(results[0]["V"]) if results else "Not available"
                print(f"{label}: {answer}")

            hours = query(
                f"professor_office_hours({atom(name)}, D, H)"
            )

            if hours:
                for r in hours:
                    print(f"Office Hours: {r['D']} - {r['H']}")
            else:
                print("Office Hours: Not available")

            courses = query(
                f"professor_courses({atom(name)}, C)"
            )

            if courses:
                course_list = sorted({str(r["C"]) for r in courses})
                print("Courses:", ", ".join(course_list))
            else:
                print("Courses: Not available")

        if not names:
            print("\nNo matching professor found.")
        return

    for answer in sorted(set(answers)):
        print("-", answer)

    if not answers:
        print("- No matching information found.")


def ask_question():
    """Accept simple natural-language questions."""
    print("\nAsk about professors, courses, or schedules.")
    print("Type 'back' to return to the menu.")

    while True:
        question = input("\nAsk a question: ").strip()
        lower = question.lower()

        if lower in ("back", "quit", "exit"):
            break

        course = re.search(
            r"\b(?:[a-z]{2,6}\s*)?\d{3}[a-z]?\b",
            question,
            re.I
        )

        section = re.search(
            r"\b[a-z]{2,6}\s*\d{3}\.\d+\b",
            question,
            re.I
        )

        day = re.search(
            r"\b(monday|tuesday|wednesday|thursday|friday)\b",
            lower
        )

        if section and any(
            word in lower for word in ("schedule", "room", "time", "when")
        ):
            search_system("5", section.group())

        elif course and any(
            word in lower for word in ("who", "teach", "instructor")
        ):
            search_system("1", course.group())

        elif day and "office hour" in lower:
            print("\nPlease enter the professor's name.")
            name = input("Professor: ")
            search_system("4", name)

        elif day and any(
            word in lower for word in ("course", "class", "meet")
        ):
            search_system("3", day.group())

        elif "office hour" in lower:
            name = re.sub(
                r"\b(what|when|where|are|is|the|office|hours|hour|for|of|does|do|has|have)\b",
                "",
                question,
                flags=re.I
            ).strip(" ?.'s")

            search_system("4", name)

        elif any(
            word in lower for word in ("teach", "course", "class")
        ):
            name = re.sub(
                r"\b(what|which|courses|course|classes|class|does|do|teach|teaches|teaching|by)\b",
                "",
                question,
                flags=re.I
            ).strip(" ?.")

            search_system("2", name)

        elif any(
            word in lower for word in ("profile", "email", "department")
        ):
            name = re.sub(
                r"\b(show|me|find|what|is|the|profile|email|department|for|of|about)\b",
                "",
                question,
                flags=re.I
            ).strip(" ?.")

            search_system("6", name)

        else:
            print("Question not recognized. Try rephrasing it.")


def main():
    """Display the interactive menu."""
    options = {
        "1": ("Find professor by course", "Enter course ID or number: "),
        "2": ("Find courses by professor", "Enter professor name: "),
        "3": ("Find courses by weekday", "Enter weekday: "),
        "4": ("Find professor office hours", "Enter professor name: "),
        "5": ("Find section schedule", "Enter section ID: "),
        "6": ("Search faculty profile", "Enter professor name: ")
    }

    while True:
        print("\n" + "=" * 45)
        print("COSC 369 - PROFESSOR KNOWLEDGE SYSTEM")
        print("=" * 45)

        for number, (label, _) in options.items():
            print(f"{number}. {label}")

        print("7. Ask a question")
        print("8. Exit")

        choice = input("\nSelect an option (1-8): ").strip()

        if choice in options:
            label, prompt = options[choice]
            value = input(prompt)
            search_system(choice, value)

        elif choice == "7":
            ask_question()

        elif choice == "8":
            print("\nExiting Prolog query system.")
            break

        else:
            print("\nInvalid option. Please select 1-8.")


if __name__ == "__main__":
    main()
