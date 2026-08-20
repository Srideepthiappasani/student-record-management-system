class Student:

    def __init__(self,
                 student_id,
                 name,
                 age,
                 subject,
                 marks):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.subject = subject
        self.marks = marks

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "subject": self.subject,
            "marks": self.marks
        }

    def __str__(self):

        return (
            f"{self.student_id} | "
            f"{self.name} | "
            f"{self.subject} | "
            f"{self.marks}"
        )