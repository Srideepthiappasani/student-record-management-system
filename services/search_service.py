from utils.file_handler import read_students
from utils.table import print_table


# ---------------------------------
# Calculate Grade
# ---------------------------------
def get_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    elif average >= 35:
        return "E"

    else:
        return "F"


# ---------------------------------
# Search Student
# ---------------------------------
def search_student():

    students = read_students()

    if not students:
        print("\nNo Student Records Found.")
        return

    print("\n========== SEARCH STUDENT ==========")
    print("1. Search by Student ID")
    print("2. Search by Student Name")
    print("3. Search by Subject")
    print("4. Average Marks Above")
    print("5. Average Marks Below")
    print("6. Search by Grade")
    print("7. Back")
    print("====================================")

    choice = input("\nEnter your choice: ").strip()

    # -----------------------------
    # Search by ID
    # -----------------------------
    if choice == "1":

        student_id = input("Enter Student ID: ").strip().upper()

        result = []

        for student in students:

            if student["student_id"] == student_id:
                result.append(student)

        if result:
            print_table(result)
        else:
            print("\nStudent Not Found.")

    # -----------------------------
    # Search by Name
    # -----------------------------
    elif choice == "2":

        name = input("Enter Student Name: ").strip().lower()

        result = []

        for student in students:

            if name in student["name"].lower():
                result.append(student)

        if result:
            print_table(result)
        else:
            print("\nStudent Not Found.")

    # -----------------------------
    # Search by Subject
    # -----------------------------
    elif choice == "3":

        subject = input("Enter Subject Name: ").strip().lower()

        result = []

        for student in students:

            subject_list = student["subjects"].split(";")

            for item in subject_list:

                sub, marks = item.split(":")

                if sub.lower() == subject:
                    result.append(student)
                    break

        if result:
            print_table(result)
        else:
            print("\nNo students found.")

    # -----------------------------
    # Average Marks Above
    # -----------------------------
    elif choice == "4":

        value = float(input("Enter Average Marks: "))

        result = []

        for student in students:

            if student["average_marks"] >= value:
                result.append(student)

        if result:
            print_table(result)
        else:
            print("\nNo students found.")

    # -----------------------------
    # Average Marks Below
    # -----------------------------
    elif choice == "5":

        value = float(input("Enter Average Marks: "))

        result = []

        for student in students:

            if student["average_marks"] <= value:
                result.append(student)

        if result:
            print_table(result)
        else:
            print("\nNo students found.")

    # -----------------------------
    # Search by Grade
    # -----------------------------
    elif choice == "6":

        grade = input("Enter Grade (A-F): ").strip().upper()

        result = []

        for student in students:

            if get_grade(student["average_marks"]) == grade:
                result.append(student)

        if result:
            print_table(result)
        else:
            print("\nNo students found.")

    elif choice == "7":
        return

    else:
        print("\nInvalid Choice.")