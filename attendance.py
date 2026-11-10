from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
import database


class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        Label(
            root,
            text="Attendance Management",
            font=("Arial", 20, "bold"),
            bg="#2196F3",
            fg="white",
            pady=10
        ).pack(fill=X)

        form = Frame(root)
        form.pack(pady=15)

        Label(form, text="Student").grid(row=0, column=0, padx=5, pady=5)

        self.student = ttk.Combobox(form, width=40, state="readonly")
        self.student.grid(row=0, column=1)

        self.student_map = {}
        self.load_students()

        Label(form, text="Date").grid(row=1, column=0, padx=5, pady=5)

        self.date_entry = Entry(form, width=25)
        self.date_entry.grid(row=1, column=1)

        self.date_entry.insert(0, str(date.today()))

        Label(form, text="Status").grid(row=2, column=0, padx=5, pady=5)

        self.status = ttk.Combobox(
            form,
            values=["Present", "Absent"],
            state="readonly",
            width=22
        )
        self.status.grid(row=2, column=1)
        self.status.current(0)

        Button(
            form,
            text="Mark Attendance",
            width=20,
            bg="green",
            fg="white",
            command=self.save_attendance
        ).grid(row=3, column=0, columnspan=2, pady=15)

        columns = ("ID", "Roll", "Name", "Date", "Status")

        self.table = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=160)

        self.table.pack(fill=BOTH, padx=10, pady=10)

        self.load_attendance()

    def load_students(self):
        students = database.get_students()

        values = []

        for student in students:
            sid = student[0]
            roll = student[1]
            name = student[2]

            text = f"{roll} - {name}"

            values.append(text)
            self.student_map[text] = sid

        self.student["values"] = values

        if values:
            self.student.current(0)

    def save_attendance(self):

        if self.student.get() == "":
            messagebox.showerror("Error", "Select Student")
            return

        student_id = self.student_map[self.student.get()]

        database.mark_attendance(
            student_id,
            self.date_entry.get(),
            self.status.get()
        )

        messagebox.showinfo(
            "Success",
            "Attendance Marked Successfully"
        )

        self.load_attendance()

    def load_attendance(self):

        for row in self.table.get_children():
            self.table.delete(row)

        records = database.get_attendance()

        for row in records:
            self.table.insert("", END, values=row)


if __name__ == "__main__":
    database.create_tables()

    root = Tk()
    Attendance(root)
    root.mainloop()