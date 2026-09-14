# COSC 369 Assignment 1

## Project Description

This project takes the input files and uses them to create a class schedule and office hours document.

We used Python, C, a static library, a Makefile, and Prolog for the project.

The Python part reads the input files and puts the information into a text file. The C part takes that text file and formats the information, while another Python file creates the final Word document.

We also added Prolog so users can search for information about classes, professors, and office hours.

## Input Files

The three input files are:

1. `Enrollment info.xlsx`
   - This file has the class information like the course number, title, days, times, room, and instructor.

2. `Syllabus.docx`
   - This file has the professor information, class information, and office hours.

3. `faculty_info.csv`
   - This file has additional professor information like their office, department, and office hours.

## Project Files

- `main.py` reads the input files and creates the combined text file and Prolog knowledge base.
- `formatter.h` is the header file for the C formatting function.
- `formatter.c` contains the C code that formats the schedule.
- `main.c` runs the C formatting part of the project.
- `generate_word.py` creates the final Word document.
- `Makefile` builds and runs the project.
- `libformatter.a` is the static library used by the C program.
- `prolog_queries.py` lets users search for class and professor information.
- `knowledge_base.pl` contains the information used for the Prolog searches.

## How to Run the Project

Open the project folder in VS Code and open the terminal.

To run the project, type these commands in order:

```powershell
python main.py
.\schedule_formatter.exe
python generate_word.py
```

To open the final Word document, type:

```powershell
start Final_Schedule.docx
```

The final output file is:

`Final_Schedule.docx`

You can also use the Makefile if Make and a C compiler are installed.

```bash
make
```

If you want to remove the generated files and rebuild the project, type:

```bash
make clean
make
```

## Prolog Search

We also added a Prolog search to the project.

It uses the information from the input files to let users search for things like what professor teaches a class, class schedules, and professor office hours.

To run it, type:

```powershell
python prolog_queries.py
```

The program gives different options depending on what information you want to find.

## Static Library

The static library used in this project is:

`libformatter.a`

It is created from `formatter.c` and then linked with `main.c`.