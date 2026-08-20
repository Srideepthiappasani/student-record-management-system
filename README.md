\# Student Record Management System



A Python-based Student Record Management System designed to efficiently manage student information through a modular and user-friendly Command-Line Interface (CLI).



\## 📌 Overview



The Student Record Management System provides a structured way to manage student records using Python. The application follows a modular architecture, separating authentication, data models, services, menu handling, configuration, and utility functions.



It is designed as an educational and portfolio project to demonstrate Python programming, modular development, file handling, object-oriented programming, and CLI application development.



\## ✨ Features



\- 🔐 User authentication

\- 👨‍🎓 Add student records

\- 📋 View student records

\- 🔍 Search student records

\- ✏️ Update student information

\- 🗑️ Delete student records

\- 📁 Student data management

\- 🖥️ Menu-driven Command-Line Interface

\- 🧩 Modular project architecture

\- ⚙️ Configuration and settings management

\- 🛠️ Utility functions for reusable operations



\## 🛠️ Technologies Used



\- \*\*Python\*\*

\- \*\*Object-Oriented Programming\*\*

\- \*\*File Handling\*\*

\- \*\*Modular Programming\*\*

\- \*\*Command-Line Interface (CLI)\*\*



📂 Project Structure

student-record-management-system/
│
├── auth/
│   └── Authentication modules
│
├── config/
│   └── Configuration files
│
├── data/
│   └── Student data files
│
├── menu/
│   └── CLI menu and user interaction modules
│
├── models/
│   └── Student data models
│
├── services/
│   └── Application business logic
│
├── settings/
│   └── Application settings
│
├── utils/
│   └── Utility and helper functions
│
├── main.py
│   └── Main application entry point
│
├── requirements.txt
│   └── Python dependencies
│
├── .gitignore
│   └── Git ignored files
│
└── README.md
    └── Project documentation

🚀 Getting Started

Follow the steps below to run the project locally.

Prerequisites

Make sure Python is installed on your system.

Check the Python version:
python --version

📥 Installation
1. Clone the Repository
git clone https://github.com/Srideepthiappasani/student-record-management-system.git

Navigate to the project directory:
cd student-record-management-system

2. Create a Virtual Environment
Create a Python virtual environment:
python -m venv venv

3. Activate the Virtual Environment
Windows
venv\Scripts\activate

After activation, your terminal should show:
(venv)

4. Install Dependencies
Install the required Python packages:
pip install -r requirements.txt

▶️ Running the Application
Run the main application:
python main.py
The application launches through a menu-driven Command-Line Interface.

💻 Application Workflow
The system provides functionality for managing student records.
A typical workflow includes:

🔐 Authentication
The system includes an authentication module to control access to the application.
The authentication component is responsible for:
- User login
- User validation
- Credential handling
- Access control

  👨‍🎓 Student Management
The Student Management functionality supports common CRUD operations.

Create
Add a new student record.

Read
View existing student records.

Update
Modify existing student information.

Delete
Remove student records.

Search
Find student records based on available information.

📊 Data Management

Student information is organized within the data/ directory.
The application separates data storage from business logic to keep the project organized and maintainable.

🧩 Modular Design
The project follows a modular design approach.
Each module has a specific responsibility:

auth/
Handles authentication-related functionality.

config/
Contains configuration-related components.

data/
Contains student-related data.

menu/
Handles the command-line menu and user interaction.

models/
Contains data models used by the application.

services/
Contains the application's business logic.

settings/
Contains application-level settings.

utils/
Contains reusable helper and utility functions.

main.py
Acts as the main entry point of the application.
    






 


