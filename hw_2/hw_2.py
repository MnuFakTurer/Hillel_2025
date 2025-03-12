students = [
    {
        "id": "7",
        "name": "Adas",
        "mark": [4, 5, 5, 7, 1],
        "info": "The Dark King",
    },
    {
        "id": "8",
        "name": "Anakin",
        "mark": [4, 5, 5, 7, 1],
        "info": "Darth Vader",
    },
    {
        "id": "4",
        "name": "Ajunta Pall",
        "mark": [4, 5, 5, 7, 1],
        "info": "First Dark Lord",
    },
]


CONSOLE_COMMANDS = (
    "\n 1->Show students:\n 2->Show student ID:\n 3->Add student:\n 4->Exit:"
)


def show_students():
    for student in students:
        print(
            f"ID: {student['id']}, Name: {student['name']},"
            f"Mark: {student['mark']}, Info: {student['info']}"
        )


def show_student(name):
    found = False
    for student in students:
        if student["id"] == name:
            print(
                f"ID: {student['id']}, Name: {student['name']},"
                f"Mark: {student['mark']}, Info: {student['info']}"
            )
            found = True
            break
    if not found:
        print(f"There is no student: {name}")


def student_add(id_add: int, name_add: str, info_add: str):
    if (
        isinstance(id_add, int)
        and isinstance(name_add, str)
        and not name_add.isdigit()
        and isinstance(info_add, str)
    ):
        student = {"id": id_add, "name": name_add, "mark": [], "info": info_add}
        students.append(student)
    else:
        print("Incorrect input!")


def main():
    print(
        f"{"#"* 40}\n\n"
        f"Welcome to the digital jurnal:\n"
        f"Command to Enter:{CONSOLE_COMMANDS}\n\n{"#"* 40}\n"
    )
    try:
        while True:
            user_input = input("\nEnter the comand: ")

            if user_input == "1":
                show_students()
            elif user_input == "2":
                student_id = input("Search by ID: ")
                show_student(student_id)
            elif user_input == "3":
                add_id = int(input("Enter ID: "))
                add_name = str(input("Enter name: "))
                add_info = str(input("Enter Info: "))
                student_add(add_id, add_name, add_info)
            elif user_input == "4":
                break
            else:
                print("Incorrect action!")

    except ValueError as e:
        print(f"Inkorrect input!. {e}")
    finally:
        print("End program\n")


main()
