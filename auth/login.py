import os

ADMIN_FILE = "data/admin.txt"


# ---------------------------------
# Login
# ---------------------------------
def login():

    with open(ADMIN_FILE, "r") as file:

        username = file.readline().strip()

        password = file.readline().strip()

    attempts = 3

    while attempts > 0:

        print("=" * 60)
        print("                ADMIN LOGIN")
        print("=" * 60)

        user = input("Username : ").strip()

        pwd = input("Password : ").strip()

        if user == username and pwd == password:

            print("\nLogin Successful!\n")

            return True

        attempts -= 1

        print("\nInvalid Username or Password")

        print(f"Attempts Remaining : {attempts}\n")

    print("Too Many Failed Attempts.")

    return False