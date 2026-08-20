from utils.file_handler import read_students, write_students

from utils.validator import (
    validate_name,
    validate_age,
    validate_marks,
    validate_student_id,
    student_exists
)

from utils.table import print_table


# -----------------------------
# Add Student
# -----------------------------
def add_student():

    students = read_students()

    student_id = input("Enter Student ID: ").strip().upper()

    if not validate_student_id(student_id):
        print("\nInvalid Student ID.")
        return

    if student_exists(student_id, students):
        print("\nStudent ID already exists.")
        return

    name = input("Enter Name: ").strip()

    if not validate_name(name):
        print("\nInvalid Name.")
        return

    age = input("Enter Age: ").strip()

    if not validate_age(age):
        print("\nInvalid Age.")
        return

    # Number of Subjects
    while True:
        try:
            number_of_subjects = int(input("Enter Number of Subjects: "))

            if number_of_subjects > 0:
                break

            print("Number of subjects must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    subjects = []
    total_marks = 0

    for i in range(number_of_subjects):

        print(f"\nSubject {i + 1}")

        subject = input("Enter Subject Name: ").strip()

        while True:

            marks = input(f"Enter Marks for {subject}: ").strip()

            if validate_marks(marks):
                marks = float(marks)
                break

            print("Invalid Marks! Enter marks between 0 and 100.")

        total_marks += marks

        subjects.append(f"{subject}:{marks}")

    average_marks = round(total_marks / number_of_subjects, 2)

    student = {

        "student_id": student_id,
        "name": name,
        "age": int(age),
        "subjects": ";".join(subjects),
        "total_marks": total_marks,
        "average_marks": average_marks

    }

    students.append(student)

    write_students(students)

    print("\nStudent Added Successfully.")


# -----------------------------
# View Students
# -----------------------------
def view_students():

    students = read_students()

    if not students:
        print("\nNo Student Records Found.")
        return

    print_table(students)


# -----------------------------
# Update Student
# -----------------------------
def update_student():

    students = read_students()

    student_id = input("Enter Student ID to Update: ").strip().upper()

    for student in students:

        if student["student_id"] == student_id:

            print("\nLeave blank to keep old value.\n")

            name = input(f"Name ({student['name']}): ").strip()

            if name:

                if validate_name(name):
                    student["name"] = name
                else:
                    print("Invalid Name")

            age = input(f"Age ({student['age']}): ").strip()

            if age:

                if validate_age(age):
                    student["age"] = int(age)
                else:
                    print("Invalid Age")

            choice = input(
                "\nDo you want to update all subjects? (Y/N): "
            ).strip().upper()

            if choice == "Y":

                while True:

                    try:

                        number_of_subjects = int(
                            input("Enter Number of Subjects: ")
                        )

                        if number_of_subjects > 0:
                            break

                        print("Number of subjects must be greater than 0.")

                    except ValueError:

                        print("Please enter a valid number.")

                subjects = []

                total_marks = 0

                for i in range(number_of_subjects):

                    print(f"\nSubject {i+1}")

                    subject = input("Enter Subject Name: ").strip()

                    while True:

                        marks = input(
                            f"Enter Marks for {subject}: "
                        ).strip()

                        if validate_marks(marks):
                            marks = float(marks)
                            break

                        print("Invalid Marks.")

                    total_marks += marks

                    subjects.append(f"{subject}:{marks}")

                student["subjects"] = ";".join(subjects)

                student["total_marks"] = total_marks

                student["average_marks"] = round(
                    total_marks / number_of_subjects,
                    2
                )

            write_students(students)

            print("\nStudent Updated Successfully.")

            return

    print("\nStudent Not Found.")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():

    students = read_students()

    student_id = input("Enter Student ID to Delete: ").strip().upper()

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Details")
            print("-" * 50)

            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")

            print("\nSubjects")

            for item in student["subjects"].split(";"):

                subject, marks = item.split(":")

                print(f"{subject:<15} {marks}")

            print(f"\nTotal Marks   : {student['total_marks']}")
            print(f"Average Marks : {student['average_marks']}")

            print("-" * 50)

            confirm = input(
                "\nAre you sure you want to delete this student? (Y/N): "
            ).strip().upper()

            if confirm == "Y":

                students.remove(student)

                write_students(students)

                print("\nStudent Deleted Successfully.")

            else:

                print("\nDelete Cancelled.")

            return

    print("\nStudent Not Found.")