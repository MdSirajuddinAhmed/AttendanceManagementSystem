import sqlite3

DATABASE_NAME = "attendance.db"


# -------------------------------
# Database Connection
# -------------------------------
def get_connection():
    return sqlite3.connect(DATABASE_NAME)


# -------------------------------
# Create Tables
# -------------------------------
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_no TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        semester TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        attendance_date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# Student Functions
# -------------------------------
def add_student(roll_no, name, department, semester):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students
    (roll_no, name, department, semester)
    VALUES (?, ?, ?, ?)
    """, (roll_no, name, department, semester))

    conn.commit()
    conn.close()


def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students
    ORDER BY roll_no
    """)

    rows = cursor.fetchall()

    conn.close()
    return rows


def update_student(student_id, roll_no, name, department, semester):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET roll_no=?,
        name=?,
        department=?,
        semester=?
    WHERE id=?
    """, (roll_no, name, department, semester, student_id))

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()


# -------------------------------
# Attendance Functions
# -------------------------------
def mark_attendance(student_id, attendance_date, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attendance
    (student_id, attendance_date, status)
    VALUES (?, ?, ?)
    """, (student_id, attendance_date, status))

    conn.commit()
    conn.close()


def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        attendance.id,
        students.roll_no,
        students.name,
        attendance.attendance_date,
        attendance.status
    FROM attendance
    JOIN students
        ON students.id = attendance.student_id
    ORDER BY attendance.attendance_date DESC
    """)

    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_attendance(attendance_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM attendance WHERE id=?",
        (attendance_id,)
    )

    conn.commit()
    conn.close()


# -------------------------------
# Search Student
# -------------------------------
def search_student(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    WHERE
        roll_no LIKE ?
        OR name LIKE ?
        OR department LIKE ?
    """,
    (
        '%' + keyword + '%',
        '%' + keyword + '%',
        '%' + keyword + '%'
    ))

    rows = cursor.fetchall()

    conn.close()
    return rows


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    create_tables()
    print("Database Created Successfully")