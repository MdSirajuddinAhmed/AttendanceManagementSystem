from tkinter import *
from tkinter import ttk, messagebox
import database


class StudentManagement:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.root.geometry("950x600")
        self.root.resizable(False, False)

        self.selected_id = None

        Label(
            root,
            text="Student Management",
            font=("Arial", 20, "bold"),
            bg="#2196F3",
            fg="white",
            pady=10
        ).pack(fill=X)

        form = Frame(root)
        form.pack(pady=15)

        # ---------------- Roll No ----------------

        Label(form, text="Roll No").grid(row=0, column=0, padx=5, pady=5)

        self.roll = Entry(form, width=25)
        self.roll.grid(row=0, column=1)

        # ---------------- Name ----------------

        Label(form, text="Name").grid(row=1, column=0, padx=5, pady=5)

        self.name = Entry(form, width=25)
        self.name.grid(row=1, column=1)

        # ---------------- Department ----------------

        Label(form, text="Department").grid(row=2, column=0, padx=5, pady=5)

        self.dept = Entry(form, width=25)
        self.dept.grid(row=2, column=1)

        # ---------------- Semester ----------------

        Label(form, text="Semester").grid(row=3, column=0, padx=5, pady=5)

        self.sem = Entry(form, width=25)
        self.sem.grid(row=3, column=1)

        # ---------------- Buttons ----------------

        btn_frame = Frame(root)
        btn_frame.pack(pady=10)

        Button(
            btn_frame,
            text="Add",
            width=15,
            bg="green",
            fg="white",
            command=self.add_student
        ).grid(row=0, column=0, padx=5)

        Button(
            btn_frame,
            text="Update",
            width=15,
            bg="orange",
            command=self.update_student
        ).grid(row=0, column=1, padx=5)

        Button(
            btn_frame,
            text="Delete",
            width=15,
            bg="red",
            fg="white",
            command=self.delete_student
        ).grid(row=0, column=2, padx=5)

        Button(
            btn_frame,
            text="Clear",
            width=15,
            command=self.clear
        ).grid(row=0, column=3, padx=5)

        # ---------------- Table ----------------

        columns = ("ID", "Roll", "Name", "Department", "Semester")

        self.tree = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=170)

        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.select_student)

        database.create_tables()
        self.load_students()

    # ---------------- Load Students ----------------

    def load_students(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = database.get_students()

        for row in rows:
            self.tree.insert("", END, values=row)

    # ---------------- Add ----------------

    def add_student(self):

        if (
            self.roll.get() == "" or
            self.name.get() == "" or
            self.dept.get() == "" or
            self.sem.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        try:

            database.add_student(
                self.roll.get(),
                self.name.get(),
                self.dept.get(),
                self.sem.get()
            )

            messagebox.showinfo(
                "Success",
                "Student Added Successfully"
            )

            self.clear()
            self.load_students()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- Select ----------------

    def select_student(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected, "values")

        self.selected_id = values[0]

        self.roll.delete(0, END)
        self.roll.insert(0, values[1])

        self.name.delete(0, END)
        self.name.insert(0, values[2])

        self.dept.delete(0, END)
        self.dept.insert(0, values[3])

        self.sem.delete(0, END)
        self.sem.insert(0, values[4])

    # ---------------- Update ----------------

    def update_student(self):

        if self.selected_id is None:
            messagebox.showwarning("Warning", "Select a student")
            return

        database.update_student(
            self.selected_id,
            self.roll.get(),
            self.name.get(),
            self.dept.get(),
            self.sem.get()
        )

        messagebox.showinfo("Success", "Student Updated")

        self.clear()
        self.load_students()

    # ---------------- Delete ----------------

    def delete_student(self):

        if self.selected_id is None:
            messagebox.showwarning("Warning", "Select a student")
            return

        database.delete_student(self.selected_id)

        messagebox.showinfo("Success", "Student Deleted")

        self.clear()
        self.load_students()

    # ---------------- Clear ----------------

    def clear(self):

        self.selected_id = None

        self.roll.delete(0, END)
        self.name.delete(0, END)
        self.dept.delete(0, END)
        self.sem.delete(0, END)


if __name__ == "__main__":

    root = Tk()
    StudentManagement(root)
    root.mainloop()