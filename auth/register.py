import os

ADMIN_FILE = "data/admin.txt"


# ---------------------------------
# Register Admin
# ---------------------------------
def register():

    print("=" * 60)
    print("        CREATE ADMIN ACCOUNT")
    print("=" * 60)

    while True:

        username = input("Create Username : ").strip()

        if username == "":
            print("Username cannot be empty.\n")
            continue

        password = input("Create Password : ").strip()

        if password == "":
            print("Password cannot be empty.\n")
            continue

        confirm = input("Confirm Password : ").strip()

        if password != confirm:

            print("\nPasswords do not match.\n")

            continue

        with open(ADMIN_FILE, "w") as file:

            file.write(username + "\n")
            file.write(password)

        print("\nAdmin Account Created Successfully.")

        print("\nPlease Login.\n")

        break