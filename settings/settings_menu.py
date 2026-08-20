import os

ADMIN_FILE = "data/admin.txt"


# ---------------------------------
# Read Admin Credentials
# ---------------------------------
def read_admin():

    with open(ADMIN_FILE, "r") as file:

        username = file.readline().strip()

        password = file.readline().strip()

    return username, password


# ---------------------------------
# Write Admin Credentials
# ---------------------------------
def write_admin(username, password):

    with open(ADMIN_FILE, "w") as file:

        file.write(username + "\n")
        file.write(password)


# ---------------------------------
# Change Username
# ---------------------------------
def change_username():

    username, password = read_admin()

    print("\n========== CHANGE USERNAME ==========\n")

    print(f"Current Username : {username}")

    new_username = input("\nEnter New Username : ").strip()

    if new_username == "":

        print("\nUsername cannot be empty.")

        return

    write_admin(new_username, password)

    print("\nUsername Updated Successfully.")


# ---------------------------------
# Change Password
# ---------------------------------
def change_password():

    username, password = read_admin()

    print("\n========== CHANGE PASSWORD ==========\n")

    current = input("Current Password : ").strip()

    if current != password:

        print("\nIncorrect Current Password.")

        return

    new_password = input("New Password : ").strip()

    if new_password == "":

        print("\nPassword cannot be empty.")

        return

    confirm = input("Confirm Password : ").strip()

    if new_password != confirm:

        print("\nPasswords do not match.")

        return

    write_admin(username, new_password)

    print("\nPassword Updated Successfully.")


# ---------------------------------
# Settings Menu
# ---------------------------------
def settings_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("               SETTINGS")
        print("=" * 50)

        print("1. Change Username")
        print("2. Change Password")
        print("3. Back")

        print("=" * 50)

        choice = input("Enter Choice : ").strip()

        if choice == "1":

            change_username()

        elif choice == "2":

            change_password()

        elif choice == "3":

            break

        else:

            print("\nInvalid Choice.")