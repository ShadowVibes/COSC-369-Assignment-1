# COSC 369 Assignment 1

## Project Description

This project takes two input files and uses them to create a class schedule and office hours document.

We used Python, C, a static library, a Makefile, and Prolog for the project.

The Python part reads the input files and puts the information into a text file. The C part takes that text file and formats the information, while another Python file creates the final Word document.

We also added Prolog so users can search for information about classes, professors, and office hours.

## Input Files

The project uses two input files.

**1. Enrollment info.xlsx**

This file has the class information like the course number, title, days, times, room, and instructor. It also has a second sheet called Faculty_Info with additional professor information like their department, office, and office hours.

**2. Syllabus.docx**

This file has the professor information, class information, and office hours.

Both files are stored in the project folder, so the program can read them without needing the internet.

Some of the additional office hours are sample information and are not verified.

## Project Files

- **main.py** reads the input files and creates the combined text file and Prolog knowledge base.
- **formatter.h** is the header file for the C formatting function.
- **formatter.c** contains the C code that formats the schedule.
- **main.c** runs the C formatting part of the project.
- **generate_word.py** creates the final Word document.
- **Makefile** builds and runs the project.
- **libformatter.a** is the static library used by the C program.
- **prolog_queries.py** lets users search for class and professor information.
- **knowledge_base.pl** contains the information used for the Prolog searches.
- **Combined_Schedule_Office_Hours.txt** contains the information collected from the input files.
- **formatted_schedule.txt** is the text file formatted by the C program.
- **Final_Schedule.docx** is the final Word document.

## How to Run the Project

Open the project folder in VS Code and open the MSYS2 UCRT64 terminal.

The project uses GCC, Make, and Python. The Python environment also needs pandas, openpyxl, and python-docx.

To run the entire project, type:

```bash
mingw32-make
```

This will compile the C files, create the static library, run the Python programs, and generate the final Word document.

To open the Word document, type:

```bash
explorer.exe Final_Schedule.docx
```

The final output file is **Final_Schedule.docx**.

If you want to remove the generated files and rebuild the project, type:

```bash
mingw32-make clean
```

Then:

```bash
mingw32-make
```

The Makefile uses the Python environment in .venv, so that environment needs to be set up before running the project on another computer.

## Professor Search

We also added an option to generate a schedule for a specific professor instead of showing everyone.

In generate_word.py, there is a variable called TEACHER_NAME.

By default, it is set to ALL, which shows all professors and their schedules.

If you change it to a professor's name, the program will only show that professor's classes and office hours when you generate the Word document again.

## Prolog Search

We also added a Prolog search to the project.

It uses the information from the input files to let users search for things like what professor teaches a class, class schedules, professor office hours, and other faculty information.

To run it, type:

```bash
./.venv/bin/python prolog_queries.py
```

The program gives different options depending on what information you want to find.

The Prolog search also requires the necessary Prolog software and Python package.

## Static Library

The static library used in this project is **libformatter.a**.

It is created from formatter.c and then linked with main.c.

The Makefile handles compiling the C code, creating the static library, and linking everything together.

This lets us keep the C formatting function separate from the main C program.

## Final Output

The final Word document contains the class schedules and office hours for the professors.

It shows the course information, instructor, class days and times, and locations.

We also improved the formatting so the document is easier to read and closer to the example provided in the assignment.

The additional faculty office hours come from the sample information in the Excel file. The program uses those values instead of creating new office-hour times automatically.</