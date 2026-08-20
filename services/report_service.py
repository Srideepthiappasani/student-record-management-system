from collections import defaultdict

from utils.file_handler import read_students
from utils.table import print_table


# ---------------------------------
# Find Overall Topper
# ---------------------------------
def find_topper():

    students = read_students()

    if not students:
        print("\nNo Student Records Found.")
        return

    topper = max(
        students,
        key=lambda student: student["average_marks"]
    )

    print("\n========== OVERALL TOPPER ==========\n")

    print_table([topper])


# ---------------------------------
# Overall Class Average
# ---------------------------------
def average_marks():

    students = read_students()

    if not students:
        print("\nNo Student Records Found.")
        return

    average = (
        sum(student["average_marks"] for student in students)
        / len(students)
    )

    print("\n========== CLASS AVERAGE ==========")
    print(f"Overall Average Marks : {average:.2f}")
    print("===================================")


# ---------------------------------
# Statistics Dashboard
# ---------------------------------
def statistics_dashboard():

    students = read_students()

    if not students:
        print("\nNo Student Records Found.")
        return

    total_students = len(students)

    highest_average = max(
        student["average_marks"]
        for student in students
    )

    lowest_average = min(
        student["average_marks"]
        for student in students
    )

    highest_total = max(
        student["total_marks"]
        for student in students
    )

    lowest_total = min(
        student["total_marks"]
        for student in students
    )

    class_average = (
        sum(student["average_marks"] for student in students)
        / total_students
    )

    passed_students = len([
        student
        for student in students
        if student["average_marks"] >= 35
    ])

    failed_students = total_students - passed_students

    pass_percentage = (
        passed_students / total_students
    ) * 100

    fail_percentage = (
        failed_students / total_students
    ) * 100

    print("\n")
    print("=" * 65)
    print("              STUDENT ANALYTICS DASHBOARD")
    print("=" * 65)

    print(f"Total Students          : {total_students}")
    print(f"Highest Average Marks   : {highest_average:.2f}")
    print(f"Lowest Average Marks    : {lowest_average:.2f}")
    print(f"Overall Class Average   : {class_average:.2f}")

    print()

    print(f"Highest Total Marks     : {highest_total:.2f}")
    print(f"Lowest Total Marks      : {lowest_total:.2f}")

    print()

    print(f"Passed Students         : {passed_students}")
    print(f"Failed Students         : {failed_students}")

    print(f"Pass Percentage         : {pass_percentage:.2f}%")
    print(f"Fail Percentage         : {fail_percentage:.2f}%")

    print()
    print("=" * 65)

    print("GRADE DISTRIBUTION")

    grades = {

        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0

    }

    for student in students:

        average = student["average_marks"]

        if average >= 90:
            grades["A"] += 1

        elif average >= 80:
            grades["B"] += 1

        elif average >= 70:
            grades["C"] += 1

        elif average >= 60:
            grades["D"] += 1

        elif average >= 35:
            grades["E"] += 1

        else:
            grades["F"] += 1

    for grade, count in grades.items():

        print(f"{grade} Grade : {count}")

    print()
    print("=" * 65)
    # ---------------------------------
    # Top 5 Students
    # ---------------------------------

    print("TOP 5 STUDENTS")

    ranked_students = sorted(
        students,
        key=lambda student: student["average_marks"],
        reverse=True
    )

    print()

    print("{:<6} {:<15} {:<15}".format(
        "Rank",
        "Name",
        "Average"
    ))

    print("-" * 40)

    for rank, student in enumerate(ranked_students[:5], start=1):

        print("{:<6} {:<15} {:<15.2f}".format(
            rank,
            student["name"],
            student["average_marks"]
        ))

    print()

    print("=" * 65)

    # ---------------------------------
    # Subject-wise Average
    # ---------------------------------

    print("SUBJECT-WISE AVERAGE")

    subject_marks = defaultdict(list)

    for student in students:

        subjects = student["subjects"].split(";")

        for item in subjects:

            subject, marks = item.split(":")

            subject_marks[subject].append(float(marks))

    best_subject = ""
    best_average = 0

    for subject in sorted(subject_marks):

        average = (
            sum(subject_marks[subject])
            / len(subject_marks[subject])
        )

        print(f"{subject:<20}{average:.2f}")

        if average > best_average:

            best_average = average
            best_subject = subject

    print()

    print("=" * 65)

    # ---------------------------------
    # Subject-wise Topper
    # ---------------------------------

    print("SUBJECT-WISE TOPPERS")

    for subject in sorted(subject_marks):

        topper_name = ""
        topper_marks = -1

        for student in students:

            for item in student["subjects"].split(";"):

                sub, marks = item.split(":")

                marks = float(marks)

                if sub == subject and marks > topper_marks:

                    topper_marks = marks
                    topper_name = student["name"]

        print(f"{subject:<20}{topper_name} ({topper_marks:.2f})")

    print()

    print("=" * 65)

    # ---------------------------------
    # Best Performing Subject
    # ---------------------------------

    print("BEST PERFORMING SUBJECT")

    print(f"\n{best_subject} ({best_average:.2f})")

    print()

    print("=" * 65)

    # ---------------------------------
    # Overall Topper Details
    # ---------------------------------

    topper = max(
        students,
        key=lambda student: student["average_marks"]
    )

    print("OVERALL TOPPER")

    print()

    print(f"Student ID       : {topper['student_id']}")
    print(f"Name             : {topper['name']}")
    print(f"Age              : {topper['age']}")
    print(f"Average Marks    : {topper['average_marks']:.2f}")
    print(f"Total Marks      : {topper['total_marks']:.2f}")

    print()

    print("=" * 65)

    print("Dashboard Generated Successfully")

    print("=" * 65)