from tkinter import *


class About:

    def __init__(self, root):
        self.root = root
        self.root.title("About")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        # ---------------- Title ----------------
        title = Label(
            self.root,
            text="Attendance Management System",
            font=("Arial", 22, "bold"),
            bg="#2196F3",
            fg="white",
            pady=12
        )
        title.pack(fill=X)

        # ---------------- About Text ----------------
        about_text = """
Project Name:
Attendance Management System

Description:
Attendance Management System is a desktop application
developed using Python, Tkinter, and SQLite.

The system helps educational institutions manage
student attendance digitally instead of maintaining
manual attendance registers.

Main Features:
• Student Registration
• Update Student Details
• Delete Student
• Mark Daily Attendance
• Attendance Reports
• SQLite Database
• User-Friendly Interface

Technology Used:
• Python 3.x
• Tkinter GUI
• SQLite Database

Developer:
Md Sirajuddin Ahmed

Course:
Bachelor of Engineering (Computer Science)

Project Type:
Final Year Mini Project
"""

        Label(
            self.root,
            text=about_text,
            justify=LEFT,
            font=("Arial", 12),
            bg="white",
            anchor="nw"
        ).pack(padx=20, pady=20, fill=BOTH, expand=True)

        # ---------------- Footer ----------------
        Label(
            self.root,
            text="© 2026 Attendance Management System",
            font=("Arial", 10),
            bg="white",
            fg="gray"
        ).pack(side=BOTTOM, pady=10)


if __name__ == "__main__":
    root = Tk()
    About(root)
    root.mainloop()