from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
import csv
import database


class AttendanceReport:

    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Report")
        self.root.geometry("900x550")
        self.root.resizable(False, False)

        Label(
            root,
            text="Attendance Report",
            font=("Arial", 20, "bold"),
            bg="#2196F3",
            fg="white",
            pady=10
        ).pack(fill=X)

        btn_frame = Frame(root)
        btn_frame.pack(pady=10)

        Button(
            btn_frame,
            text="Refresh",
            width=15,
            bg="green",
            fg="white",
            command=self.load_data
        ).grid(row=0, column=0, padx=10)

        Button(
            btn_frame,
            text="Export CSV",
            width=15,
            bg="orange",
            command=self.export_csv
        ).grid(row=0, column=1, padx=10)

        columns = (
            "ID",
            "Roll No",
            "Student Name",
            "Date",
            "Status"
        )

        self.tree = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=18
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=170)

        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.load_data()

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        records = database.get_attendance()

        for row in records:
            self.tree.insert("", END, values=row)

    def export_csv(self):

        records = database.get_attendance()

        if not records:
            messagebox.showwarning(
                "No Data",
                "No attendance records found."
            )
            return

        filename = asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV File", "*.csv")],
            title="Save Attendance Report"
        )

        if not filename:
            return

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Roll No",
                "Student Name",
                "Date",
                "Status"
            ])

            writer.writerows(records)

        messagebox.showinfo(
            "Success",
            "Attendance report exported successfully."
        )


if __name__ == "__main__":

    database.create_tables()

    root = Tk()
    AttendanceReport(root)
    root.mainloop()