from tkinter import *
from tkinter import messagebox
import main


class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        Label(
            root,
            text="Attendance Management System",
            font=("Arial", 20, "bold"),
            bg="#2196F3",
            fg="white",
            pady=10
        ).pack(fill=X)

        frame = Frame(root, bg="white")
        frame.pack(pady=40)

        Label(
            frame,
            text="Username",
            bg="white",
            font=("Arial", 12)
        ).grid(row=0, column=0, padx=10, pady=10)

        self.username = Entry(frame, font=("Arial", 12), width=25)
        self.username.grid(row=0, column=1)

        Label(
            frame,
            text="Password",
            bg="white",
            font=("Arial", 12)
        ).grid(row=1, column=0, padx=10, pady=10)

        self.password = Entry(
            frame,
            show="*",
            font=("Arial", 12),
            width=25
        )
        self.password.grid(row=1, column=1)

        Button(
            root,
            text="Login",
            width=20,
            bg="green",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.login
        ).pack(pady=10)

        Button(
            root,
            text="Exit",
            width=20,
            bg="red",
            fg="white",
            font=("Arial", 12, "bold"),
            command=root.destroy
        ).pack()

    def login(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == "admin" and pwd == "admin123":

            self.root.destroy()

            root = Tk()
            main.AttendanceManagementSystem(root)
            root.mainloop()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )


if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()