from db.main_db import get_connection

def add_student(name, age, grade):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO student (name, age, grade) VALUES (?, ?, ?)",
        (name, age, grade)
    )

    conn.commit()
    conn.close()


def get_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    data = cur.fetchall()

    conn.close()
    return data


def update_student(student_id, name, age, grade):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE student SET name=?, age=?, grade=? WHERE id=?",
        (name, age, grade, student_id)
    )

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM student WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()