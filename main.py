import os

from auth.register import register
from settings.settings_menu import settings_menu
from auth.login import login
from menu.menu import display_menu

from services.student_service import (
    add_student,
    view_students,
    update_student,
    delete_student
)

from services.search_service import search_student

from services.report_service import (
    find_topper,
    average_marks,
    statistics_dashboard
)

from services.sort_service import sort_students


def pause():
    input("\nPress Enter to continue...")


def main():

    while True:

        display_menu()

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_student()
            pause()

        elif choice == "2":
            view_students()
            pause()

        elif choice == "3":
            search_student()
            pause()

        elif choice == "4":
            update_student()
            pause()

        elif choice == "5":
            delete_student()
            pause()

        elif choice == "6":
            find_topper()
            pause()

        elif choice == "7":
            average_marks()
            pause()

        elif choice == "8":
            sort_students()
            pause()

        elif choice == "9":
            statistics_dashboard()
            pause()

        elif choice == "10":

            settings_menu()

            pause()

        elif choice == "11":

            print("\nThank you for using Student Record Management System.")

            break

        else:

            print("\nInvalid Choice.")

            pause()

ADMIN_FILE = "data/admin.txt"

if __name__ == "__main__":

    if not os.path.exists(ADMIN_FILE) or os.path.getsize(ADMIN_FILE) == 0:

        register()

    if login():

        main()