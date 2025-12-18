open("students.txt", "a").close()
open("courses.txt", "a").close()
open("grades.txt", "a").close()

import re

def valid_name(name):
    return bool(re.fullmatch(r"[A-Za-z .'/\-]+", name))

def add_student():
    while True:
        student_id_input = input("Enter Student ID: ").strip()

        if student_id_input.isdigit():
            student_id = int(student_id_input)
            break
        else:
            print("Invalid Student ID. Please enter numbers only.")
    with open("students.txt", "r") as f:
        for line in f:
            if line.startswith(f"{student_id},"):
                print("Error: This Student ID already exists.")
                return
    while True:
        student_name = input("Enter Student Name: ").strip()
        if valid_name(student_name):
            break
        else:
            print("Invalid Name")
    while True:
        student_email = input("Enter Email: ").strip().lower()
        if student_email.endswith("@imail.sunway.edu.my")and student_email !="@imail.sunway.edu.my":
            break
        else:
            print("This email is invalid. Please enter a valid Email address.")

    with open("students.txt", "a") as f:
        f.write(f"{student_id},{student_name},{student_email}\n")

    print("Student added successfully!\n")

def modify_student():
    student_id = input("Enter Student ID to modify: ")
    lines = []
    found = False

    with open("students.txt", "r") as f:
        lines = f.readlines()

    with open("students.txt", "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == student_id:
                found = True
                current_name = data[1]
                current_email = data[2]
                while True:
                    print(f"Current Name: {current_name}")
                    new_name = input("Enter New Name (or press Enter to keep): ").strip()

                    if new_name == "":
                        new_name = current_name
                        break
                    elif valid_name(new_name):
                        break
                    else:
                        print("Invalid Name")

                while True:
                    print(f"Current Email: {current_email}")
                    new_email = input("Enter New Email (or press Enter to keep): ").strip().lower()
                    
                    if new_email == "":
                        new_email = current_email
                        break
                    elif new_email.endswith("@imail.sunway.edu.my")and new_email !="@imail.sunway.edu.my":
                        break
                    else:
                        print("This email is invalid. Please enter a valid Email address.")

                f.write(f"{student_id},{new_name},{new_email}\n")
                print("Student details updated successfully.\n")
            
            else:
                f.write(line)

    if not found:
        print("Student ID not found.\n")


def remove_student():
    student_id = input("Enter student ID: ")
    found = False
    
    with open("students.txt", "r") as f:
        lines = f.readlines() # loads students.txt into memory because opening in w mode will wipe the file

    with open("students.txt", "w") as f:
        for line in lines:
            if not line.startswith(f"{student_id},"): # if not the target we want to delete, write it back
                f.write(line)
            else:
                found = True # if the line was found, it would not be written back into the file

    if not found:
        print("Student ID does not exist, nothing was deleted.")
        return

    with open("grades.txt", "r") as f:
        lines = f.readlines()

    with open("grades.txt", "w") as f: # delete their grades too
        for line in lines:
            if not line.strip():
                continue
            if not line.startswith(f"{student_id},"):
                f.write(line)
                

    print(f"Student {student_id} Has been delete.")


def add_course():
    course_id = input("Enter Course ID: ")

    with open("courses.txt", "r") as f:
        for line in f:
            if line.startswith(f"{course_id},"):
                print("Error: This Course ID already exists.")
                return

    course_name = input("Enter Course Name: ")

    with open("courses.txt","a") as f:
        f.write(f"{course_id},{course_name}\n")

    print("Course added successfully!\n")


def modify_course():
    course_id = input("Enter Course ID to modify: ")
    lines = []
    found = False

    with open("courses.txt", "r") as f:
        lines = f.readlines()

    with open("courses.txt", "w") as f:
        for line in lines:
            if not line.strip():
                continue
            data = line.strip().split(",")
            
            if data[0] == course_id:
                found = True
                current_name = data[1]
                
                print(f"Current Course Name: {current_name}")
                new_name = input("Enter New Name (or press Enter to keep): ")
                
                if new_name == "": 
                    new_name = current_name

                f.write(f"{course_id},{new_name}\n")
                print("Course name updated successfully.\n")
            
            else:
                f.write(line)

    if not found:
        print("Course ID not found.\n")


def remove_course():
    course_id = input("Enter Course ID to delete: ")
    found = False

    with open("courses.txt", "r") as f:
        lines = f.readlines()

    with open("courses.txt", "w") as f:
        for line in lines:
            if not line.startswith(f"{course_id},"):
                f.write(line)
            else:
                found = True

    if not found:
        print("Course ID does not exist, nothing was deleted.")
        return
    
    with open("grades.txt", "r") as f:
        lines = f.readlines()

    
    with open("grades.txt", "w") as f:
        for line in lines:
            if not line.strip():
                continue
                
            data = line.strip().split(",") # removes newlines and creates a list by splitting the commas
            if data[1] != course_id: # write the line back in only if its not the course to be deleted
                f.write(line)

    print(f"Course {course_id} Has been deleted.")


def record_marks():
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")

    student_exists = False
    with open("students.txt", "r") as f:
        for line in f:
            if line.startswith(f"{student_id},"):
                student_exists = True
                break
    
    if not student_exists:
        print("Error: Student ID not found.")
        return

    course_exists = False
    with open("courses.txt", "r") as f:
        for line in f:
            if line.startswith(f"{course_id},"):
                course_exists = True
                break

    if not course_exists:
        print("Error: Course ID not found.")
        return

    while True:
        try:
            student_marks = float(input("Enter Marks: "))
            if 0 <= student_marks <= 100:
                break
            else:
                print("The Marks You Have Entered Is Invalid.")
        except ValueError:
                print("Please Enter Numbers That Is Valid.")

    if student_marks >= 80: course_grade = "A+"
    elif student_marks >= 75:
        course_grade = "A"
    elif student_marks >= 70:
        course_grade = "B+"
    elif student_marks >= 65:
        course_grade = "B"
    elif student_marks >= 60:
        course_grade = "B-"
    elif student_marks >= 55:
        course_grade = "C+"
    elif student_marks >= 50:
        course_grade = "C"
    else: course_grade = "F"

    new_record = f"{student_id},{course_id},{student_marks},{course_grade}\n"
    
    lines = []

    with open("grades.txt", "r") as f:
        lines = f.readlines()

    found = False
    
    with open("grades.txt", "w") as f:
        for line in lines:
            if not line.strip():
                continue
            data = line.strip().split(",")
            
            if data[0] == student_id and data[1] == course_id:
                f.write(new_record)
                found = True
                print(f"Marks Have Been Successfully Updated! Grade: {course_grade}.\n")
            else:
                f.write(line)
        
        if not found:
            f.write(new_record)
            print(f"Marks Have Been Successfully Recorded! Grade: {course_grade}\n")
            
    print(f"Grade assigned: {course_grade}\n")


def display_student_performance():
    student_id = input("Enter Student ID: ")
    student_name = ""
    student_email = ""
    found_student = False
    found_grades = False
    
    with open("students.txt", "r") as f:
        for line in f:
            if not line.strip():
                continue
            data = line.strip().split(",")
            if data[0] == student_id:
                student_name = data[1]
                student_email = data[2]
                found_student = True
                break 

    if not found_student:
        print("\nError, student does not exist.")
        return

    print("\n========================================")
    print("          PERFORMANCE SUMMARY            ")
    print("========================================")
    print(f"Student Name:  {student_name}")
    print(f"Student ID:    {student_id}")
    print(f"Email:         {student_email}")
    print("----------------------------------------")
    print(f"{'Course ID':<15} | {'Marks':<8} | {'Grade':<5}") # < alligns the text and pads with spaces, quotation mark gave error idk why
    print("----------------------------------------")

    with open("grades.txt", "r") as grades_file:
        for line in grades_file:
            if not line.strip(): continue
            data = line.strip().split(",")

            if data[0] == student_id:
                print(f"{data[1]:<15} | {data[2]:<8} | {data[3]:<5}")
                found_grades = True

    if not found_grades:
        print("\nStudent has no grades.")
        
    print("========================================\n")


def display_course_summary():
    course_id = input("Enter course ID: ")
    marks_list = []
    course_name = ""
    found_course= False

    with open("courses.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            if data[0] == course_id:
                course_name = data[1]
                found_course = True
                break
    if not found_course:
        print("\nError, course does not exist.")
        return
    
    print("==================================")
    print(f" COURSE: {course_name} ({course_id})")
    print("==================================")
    print(f"{'Student ID':<15} | {'Mark':<8} | {'Grade':<5}") # < alligns the text and pads with spaces
    print("----------------------------------")

    with open("grades.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            
            if data[1] == course_id:
                marks = float(data[2])
                marks_list.append(marks)
                
                print(f"{data[0]:<15} | {marks:<8.2f} | {data[3]:<5}")

    print("----------------------------------")

    if len(marks_list) > 0:
        average_mark = sum(marks_list) / len(marks_list)
        highest_mark = max(marks_list)
        lowest_mark = min(marks_list)
        
        print(f" Total Students: {len(marks_list)}")
        print(f" Average Mark:   {average_mark:.2f}")
        print(f" Highest Mark:   {highest_mark:.2f}")
        print(f" Lowest Mark:    {lowest_mark:.2f}")
    else:
        print("No students enrolled in this course.")
    
    print("==================================")


def export_performance_report():
    student_id = input("Enter Student ID to export: ")
    student_name = ""
    student_email = ""
    found_student = False

    with open("students.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            if data[0] == student_id:
                student_name = data[1]
                student_email = data[2]
                found_student = True
                break 

    if not found_student:
        print("Student ID entered is incorrect or does not exist.")
        return

    student_grades = []
    with open("grades.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            if data[0] == student_id:
                student_grades.append(data)

    if not student_grades:
        print("This student has no grades recorded yet. No report generated.")
        return

    filename = f"report_{student_id}.txt"
    
    with open(filename, "w") as export_file:
        export_file.write("========================================\n")
        export_file.write("          PERFORMANCE REPORT            \n")
        export_file.write("========================================\n")
        export_file.write(f"Student Name:  {student_name}\n")
        export_file.write(f"Student ID:    {student_id}\n")
        export_file.write(f"Email:         {student_email}\n")
        export_file.write("----------------------------------------\n")
        export_file.write(f"{'Course ID':<15} | {'Marks':<8} | {'Grade':<5}\n")
        export_file.write("----------------------------------------\n")

        for data in student_grades:
            export_file.write(f"{data[1]:<15} | {data[2]:<8} | {data[3]:<5}\n")
            
        export_file.write("========================================\n")
    
    print(f"Success! Report saved as {filename}.\n")


def manage_students():
    while True:
        print("\n=== Manage Students ===")
        print("|1. Add Student       |")
        print("|2. Modify Student    |")
        print("|3. Remove Student    |")
        print("|4. Back to Main Menu |")
        print("=======================")
        
        choice = input("Enter option: ")
        
        match choice:
            case "1":
                add_student()
            case "2":
                modify_student()
            case "3":
                remove_student()
            case "4":
                return
            case _:
                print("Invalid Choice. Please Pick A Valid Option.")


def manage_courses():
    while True:
        print("\n=== Manage Courses ===")
        print("|1. Add Course        |")
        print("|2. Modify Course     |")
        print("|3. Remove Course     |")
        print("|4. Back to Main Menu |")
        print("======================")
        
        choice = input("Enter option: ")
        
        match choice:
            case "1":
                add_course()
            case "2":
                modify_course()
            case "3":
                remove_course()
            case "4":
                return
            case _:
                print("Invalid Choice. Please Pick A Valid Option.")

while True:
    print("\n========= Main Menu =========")
    print("|1. Manage Students           |")
    print("|2. Manage Courses            |")
    print("|3. Record Marks              |")
    print("|4. See student performance   |")
    print("|5. Display course summary    |")
    print("|6. Export student performance|")
    print("|7. Exit                      |")
    print("===============================")

    choice = input("Enter your option: ")

    match choice:
        case "1":
            manage_students()
        case "2":
            manage_courses()
        case "3":
            record_marks()
        case "4":
            display_student_performance()
        case "5":
            display_course_summary()
        case "6":
            export_performance_report()
        case "7":
            print("Goodbye!")
            break
        case _:
            print("Invalid Choice. Please Pick A Valid Option.")
