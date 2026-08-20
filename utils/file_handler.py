import csv
import os

from config.settings import CSV_FILE


# ---------------------------------
# Create CSV File
# ---------------------------------
def create_file():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "name",
                "age",
                "subjects",
                "total_marks",
                "average_marks"
            ])


# ---------------------------------
# Read Students
# ---------------------------------
def read_students():

    create_file()

    students = []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            students.append({

                "student_id": row["student_id"],

                "name": row["name"],

                "age": int(row["age"]),

                "subjects": row["subjects"],

                "total_marks": float(row["total_marks"]),

                "average_marks": float(row["average_marks"])

            })

    return students


# ---------------------------------
# Write Students
# ---------------------------------
def write_students(students):

    create_file()

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "student_id",
            "name",
            "age",
            "subjects",
            "total_marks",
            "average_marks"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:

            writer.writerow(student)