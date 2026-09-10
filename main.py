import pandas as pd
"""
take the two input files (enrollment info and the professor's syllabus) and create a new 
file that contains the combined class schedule and office hours (sample output in the 
instruction file)
"""
#make output more readable by adding some new lines
msg = "\n\n\n\n"
print(msg)




#Part 1: read the enrollment info file and store the data in a list of dictionaries


df = pd.read_excel("Enrollment info.xlsx")
courses = {}


#store courses in a dictionary with key:course ID value:(a tuple of course info)
for _, row in df.iterrows():
    course_id = str(row["ID"]).split(".", 1)[0]

    course_info = (
        str(row["Course Title"]).split("(", 1)[0].strip(),
        row["Begin"],
        row["End "],
        row["Days"],
        row["Room"],
        row["Instructor 2025"]
    )

    courses[course_id] = course_info

#print courses (debugging)
for course_id, course_info in courses.items():
    print(course_id, course_info)
    print()
#print(courses) #full sctructure (debugging)



#Part 2: read the syllabus file and extract the office hours information --------------------
from docx import Document

doc = Document("Syllabus.docx")
office_hours = None

for paragraph in doc.paragraphs:
    text = paragraph.text.strip()

    if "Office Hours:" in text:
        office_hours = text
        break

print(office_hours)



#Part 3: create a new file that contains the combined class schedule and office hours --------------------
with open("Combined_Schedule_Office_Hours.txt", "w") as f:
    f.write("Combined Class Schedule and Office Hours\n")
    f.write("=" * 50 + "\n")

    # Write class schedule
    for course_id, course_info in courses.items():
        f.write(f"Course ID: {course_id}\n")
        f.write(f"Title: {course_info[0]}\n")
        f.write(f"Begin: {course_info[1]}\n")
        f.write(f"End: {course_info[2]}\n")
        f.write(f"Days: {course_info[3]}\n")
        f.write(f"Room: {course_info[4]}\n")
        f.write(f"Instructor: {course_info[5]}\n")
        f.write("-" * 30 + "\n")

    # Write office hours
    if office_hours:
        f.write(f"Office Hours: {office_hours}\n")


#Part 4: to do in C: take this text file and create a new Word document that contains the 
#same information in a way that matches the expected output format







print(msg)
