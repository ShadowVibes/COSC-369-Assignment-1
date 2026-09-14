# COSC 369 Assignment 1

## Project Description

This project takes 2+ input files and uses them to create a class schedule and office hours document.

We used Python, C, a static library, and a Makefile for the project.

The Python part reads the input files and puts the information into a temporary text file. The C part takes that text file and formats the information, while another Python file creates the final Word document.

## Input Files

The input files are:

1. `Enrollment info.xlsx`

   - This file has the class information for all relevant courses like the course number, title, days, times, room, and instructor.

2. `Syllabus.docx` (and optionally additional syllabi)

   - This file has the professor(s) information and office hours.

## Project Files

- `main.py` reads the two input files and creates the combined text file.
- `formatter.h` is the header file for the C formatting function.
- `formatter.c` contains the C code that formats the schedule.
- `main.c` runs the C formatting part of the project.
- `generate_word.py` creates the final Word document.
- `Makefile` builds and runs the project.
- `libformatter.a` is the static library used by the C program.

## How to Run the Project

Open the project folder in VS Code and open the terminal.

To build and run the project, type:

```bash
make run
```

Ensure all required input files are in the project folder. To create a document for a different teacher, go to generate_word.py and assign any part of the teacher's name to the "TEACHER_NAME" variable.
