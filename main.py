from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel

import student
import attendance
import report
import about
import database

# Create database tables
database.create_tables()


class AttendanceManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("900x550")
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(False, False)

        # ---------------- Title ----------------
        title = Label(
            self.root,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            bg="#1E90FF",
            fg="white",
            font=("Arial", 22, "bold"),
            pady=15
        )
        title.pack(fill=X)

        # ---------------- Buttons Frame ----------------
        frame = Frame(self.root, bg="#f0f8ff")
        frame.pack(pady=40)

        Button(
            frame,
            text="Student Management",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.student_management
        ).grid(row=0, column=0, padx=20, pady=10)

        Button(
            frame,
            text="Mark Attendance",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.mark_attendance
        ).grid(row=1, column=0, padx=20, pady=10)

        Button(
            frame,
            text="Attendance Report",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.attendance_report
        ).grid(row=2, column=0, padx=20, pady=10)

        Button(
            frame,
            text="About",
            font=("Arial", 14),
            width=25,
            height=2,
            command=self.about_project
        ).grid(row=3, column=0, padx=20, pady=10)

        Button(
            frame,
            text="Exit",
            font=("Arial", 14),
            width=25,
            height=2,
            bg="red",
            fg="white",
            command=self.root.destroy
        ).grid(row=4, column=0, padx=20, pady=10)

        footer = Label(
            self.root,
            text="Developed By: Md Sirajuddin Ahmed | B.E. CSE Final Year Project",
            font=("Arial", 10),
            bg="#f0f8ff",
            fg="gray"
        )
        footer.pack(side=BOTTOM, pady=10)

    # ---------------- Student Module ----------------
    def student_management(self):
        win = Toplevel(self.root)
        student.StudentManagement(win)

    # ---------------- Attendance Module ----------------
    def mark_attendance(self):
        win = Toplevel(self.root)
        attendance.Attendance(win)

    # ---------------- Report Module ----------------
    def attendance_report(self):
        win = Toplevel(self.root)
        report.AttendanceReport(win)

    # ---------------- About Module ----------------
    def about_project(self):
        win = Toplevel(self.root)
        about.About(win)


# ---------------- Main ----------------
if __name__ == "__main__":
    root = Tk()
    app = AttendanceManagementSystem(root)
    root.mainloop()