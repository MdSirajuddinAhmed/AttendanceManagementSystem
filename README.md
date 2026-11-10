# Attendance Management System

## Project Overview

The **Attendance Management System** is a desktop application developed using **Python**, **Tkinter**, and **SQLite**. It helps educational institutions manage student records and attendance digitally.

---

## Features

- Secure Login
- Student Management
  - Add Student
  - Update Student
  - Delete Student
  - View Student List
- Attendance Management
  - Mark Present/Absent
  - Store Daily Attendance
- Attendance Report
  - View Attendance Records
  - Export Report to CSV
- SQLite Database
- User-Friendly Graphical Interface

---

## Technologies Used

- Python 3.x
- Tkinter
- SQLite3

---

## Project Structure

```
AttendanceManagementSystem/
│
├── login.py
├── main.py
├── database.py
├── student.py
├── attendance.py
├── report.py
├── about.py
├── attendance.db
├── requirements.txt
└── README.md
```

---

## Installation

1. Install Python 3.10 or later.

2. Clone the repository or download the project.

3. Open the project folder in VS Code.

4. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

5. Run the project:

```bash
python login.py
```

---

## Default Login

Username:

```
admin
```

Password:

```
admin123
```

---

## Database

The application automatically creates:

```
attendance.db
```

Tables:

- students
- attendance

---

## Modules

### Login
Allows the administrator to log in.

### Student Management

- Add Student
- Update Student
- Delete Student
- View Students

### Attendance

- Mark Attendance
- Present/Absent
- Save Attendance

### Reports

- Display Attendance Records
- Export Attendance Report to CSV

### About

Displays project details.

---

## Future Enhancements

- Student Photo
- QR Code Attendance
- Face Recognition
- Email Notifications
- Excel Export
- PDF Report
- Cloud Database

---

## Author

**Md Sirajuddin Ahmed**

Bachelor of Engineering (Computer Science)

Final Year Mini Project

---

## License

This project is developed for educational purposes.