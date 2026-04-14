from db.main_db import create_table
from db.queries import add_student, get_students, update_student, delete_student

create_table()

add_student("Ali", 20, "A")
add_student("Beka", 19, "B")

print("Список студентов:")
for s in get_students():
    print(s)

update_student(1, "Ali", 21, "A+")

delete_student(2)

print("После изменений:")
for s in get_students():
    print(s)