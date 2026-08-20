import os

from utils.colors import Colors


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():

    clear_screen()

    print(Colors.HEADER + "=" * 65)
    print(Colors.HEADER + "      STUDENT RECORD MANAGEMENT SYSTEM")
    print(Colors.HEADER + "=" * 65)

    print(Colors.MENU + "1.  Add Student")
    print(Colors.MENU + "2.  View Students")
    print(Colors.MENU + "3.  Search Student")
    print(Colors.MENU + "4.  Update Student")
    print(Colors.MENU + "5.  Delete Student")
    print(Colors.MENU + "6.  Find Topper")
    print(Colors.MENU + "7.  Average Marks")
    print(Colors.MENU + "8.  Sort Students")
    print(Colors.MENU + "9.  Statistics Dashboard")
    print(Colors.MENU + "10. Exit")

    print(Colors.HEADER + "=" * 65)