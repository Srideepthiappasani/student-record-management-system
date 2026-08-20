import re
# ---------------------------------
# Validate Student Name
# ---------------------------------
def validate_name(name):

    if not name.strip():
        return False

    # Allow alphabets and spaces only
    if all(ch.isalpha() or ch.isspace() for ch in name):
        return True

    return False


# ---------------------------------
# Validate Age
# ---------------------------------
def validate_age(age):

    try:
        age = int(age)

        if 5 <= age <= 100:
            return True

        return False

    except ValueError:
        return False


# ---------------------------------
# Validate Marks
# ---------------------------------
def validate_marks(marks):

    try:
        marks = float(marks)

        if 0 <= marks <= 100:
            return True

        return False

    except ValueError:
        return False


# ---------------------------------
# Check Duplicate Student ID
# ---------------------------------
def student_exists(student_id, students):

    for student in students:

        if student["student_id"] == student_id:
            return True

    return False


import re

# ---------------------------------
# Validate Student ID
# ---------------------------------
def validate_student_id(student_id):

    student_id = student_id.strip()

    # Allow only letters and numbers
    pattern = r"^[A-Za-z0-9]+$"

    return bool(re.fullmatch(pattern, student_id))