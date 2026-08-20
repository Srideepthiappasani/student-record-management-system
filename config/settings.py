import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")

CSV_FILE = os.path.join(DATA_FOLDER, "students.csv")

BACKUP_FOLDER = os.path.join(BASE_DIR, "backup")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")