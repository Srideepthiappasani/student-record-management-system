from utils.colors import Colors


def success(message):
    print(Colors.SUCCESS + f"\n✔ {message}")


def error(message):
    print(Colors.ERROR + f"\n✖ {message}")


def warning(message):
    print(Colors.WARNING + f"\n⚠ {message}")


def info(message):
    print(Colors.INFO + f"\nℹ {message}")