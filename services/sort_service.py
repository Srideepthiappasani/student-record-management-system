from utils.file_handler import read_students
from utils.table import print_table


# ---------------------------------
# Sort Students
# ---------------------------------
def sort_students():

    students = read_students()

    if not students:
        print("\nNo Student Records Found.")
        return

    print("\n========== SORT STUDENTS ==========")
    print("1. Sort by Name (A-Z)")
    print("2. Sort by Age")
    print("3. Sort by Total Marks (High to Low)")
    print("4. Sort by Average Marks (High to Low)")
    print("5. Sort by Number of Subjects")
    print("6. Back")
    print("===================================")

    choice = input("\nEnter your choice: ").strip()

    # ---------------------------------
    # Sort by Name
    # ---------------------------------
    if choice == "1":

        sorted_students = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

        print("\nStudents Sorted by Name\n")
        print_table(sorted_students)

    # ---------------------------------
    # Sort by Age
    # ---------------------------------
    elif choice == "2":

        sorted_students = sorted(
            students,
            key=lambda student: student["age"]
        )

        print("\nStudents Sorted by Age\n")
        print_table(sorted_students)

    # ---------------------------------
    # Sort by Total Marks
    # ---------------------------------
    elif choice == "3":

        sorted_students = sorted(
            students,
            key=lambda student: student["total_marks"],
            reverse=True
        )

        print("\nStudents Sorted by Total Marks\n")
        print_table(sorted_students)

    # ---------------------------------
    # Sort by Average Marks
    # ---------------------------------
    elif choice == "4":

        sorted_students = sorted(
            students,
            key=lambda student: student["average_marks"],
            reverse=True
        )

        print("\nStudents Sorted by Average Marks\n")
        print_table(sorted_students)

    # ---------------------------------
    # Sort by Number of Subjects
    # ---------------------------------
    elif choice == "5":

        sorted_students = sorted(
            students,
            key=lambda student: len(student["subjects"].split(";")),
            reverse=True
        )

        print("\nStudents Sorted by Number of Subjects\n")
        print_table(sorted_students)

    elif choice == "6":
        return

    else:
        print("\nInvalid Choice.")