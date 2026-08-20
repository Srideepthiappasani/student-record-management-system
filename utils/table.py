from tabulate import tabulate


# ---------------------------------
# Display Students in Table Format
# ---------------------------------
def print_table(students):

    if not students:
        print("\nNo Student Records Found.")
        return

    table_data = []

    for student in students:

        subject_details = ""

        # Convert
        # Python:95;Java:90
        # into
        # Python(95), Java(90)

        for item in student["subjects"].split(";"):

            subject, marks = item.split(":")

            subject_details += f"{subject}({marks})\n"

        table_data.append([

            student["student_id"],

            student["name"],

            student["age"],

            subject_details.strip(),

            student["total_marks"],

            student["average_marks"]

        ])

    headers = [

        "Student ID",

        "Name",

        "Age",

        "Subjects",

        "Total Marks",

        "Average"

    ]

    print()

    print(tabulate(
        table_data,
        headers=headers,
        tablefmt="grid"
    ))