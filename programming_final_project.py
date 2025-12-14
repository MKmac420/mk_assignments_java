open("students.txt", "a").close()
open("courses.txt", "a").close()
open("grades.txt", "a").close()

def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    while True:
        student_email = input("Enter Email: ")
        if student_email.endswith("@gmail.com"):
            break
        else:
            print(" This email is invalid. Please enter a valid Email address.")

    with open("students.txt", "a") as f:
        f.write(f"{student_id},{student_name},{student_email}\n")

    print("Student added successfully!\n")


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
    course_name = input("Enter Course Name: ")

    with open("courses.txt","a") as f:
        f.write(f"{course_id},{course_name}\n")

    print("Course added successfully!\n")


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
    student_id = input("Enter Your Student ID: ")
    course_id = input("Enter Your Course ID: ")

    while True:
        try:
            student_marks = float(input("Enter Your Marks: "))
            if 0 <= student_marks <= 100:
                break
            else:
                print("The Marks You Have Entered Is Invalid.")
        except ValueError:
                print("Please Enter Numbers That Is Valid.")

    if student_marks >= 80:
        course_grade = "A+"
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
    else:
        course_grade = "F"

    with open("grades.txt", "a") as f:
        f.write(f"{student_id},{course_id},{student_marks},{course_grade}\n")
    print(f"Marks Have Been Successfully Recorded! Grade: {course_grade}\n")


def display_student_performance():
    student_id = input("Enter Student ID: ")
    student_name = ""
    student_email = ""
    found_grades = False
    
    with open("students.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            if data[0] == student_id:
                student_name = data[1]
                student_email = data[2]
                found_grades = True
                break 

    if not found_grades:
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

    try:
        with open("grades.txt", "r") as grades_file:
            for line in grades_file:
                if not line.strip(): continue
                data = line.strip().split(",")

                if data[0] == student_id:
                    print(f"{data[1]:<15} | {data[2]:<8} | {data[3]:<5}")
                    found_grades = True
    except FileNotFoundError:
        print("No grades recorded.")

    if not found_grades:
        print("\nStudent has no grades.")
        
    print("========================================\n")


def display_course_summary():
    course_id = input("Enter course ID: ")
    marks_list = []
    course_name = ""

    with open("courses.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            if data[0] == course_id:
                course_name = data[1]
                break
    
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
    

    with open("students.txt", "r") as f:
        for line in f:
            if not line.strip(): continue
            data = line.strip().split(",")
            # Check if this is the student we want
            if data[0] == student_id:
                student_name = data[1]
                student_email = data[2]
                break 

    filename = f"report_{student_id}.txt"
    found_grades = False

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

        with open("grades.txt", "r") as grades_file:
            for line in grades_file:
                if not line.strip(): continue
                data = line.strip().split(",")

                if data[0] == student_id:
                    export_file.write(f"{data[1]:<15} | {data[2]:<8} | {data[3]:<5}\n")
                    found_grades = True

        if not found_grades:
            export_file.write("\nStudent has no grades.\n")
            
        export_file.write("========================================\n")
    
    print(f"Success! Report saved as {filename}.\n")


while True:
    print("\n========= Main Menu =========")
    print("|1. Add Student               |")
    print("|2. Remove Student            |")
    print("|3. Add Course                |")
    print("|4. Remove Course             |")
    print("|5. Record Marks              |")
    print("|6. See student performance   |")
    print("|7. Display course summary    |")
    print("|8. Export student performance|")
    print("|9. Exit                      |")
    print("===============================")

    choice = input("Enter your option: ")

    match choice:
        
        case "1":
            add_student()
        case "2":
            remove_student()
        case "3":
            add_course()
        case "4":
            remove_course()
        case "5":
            record_marks()
        case "6":
            display_student_performance()
        case "7":
            display_course_summary()
        case "8":
            export_performance_report()
        case "9":
            print("Goodbye!")
            break
        case _:
            print("Invalid Choice. Please Pick A Valid Option.")
