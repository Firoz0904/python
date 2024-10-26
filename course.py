students = []

# Define the file path (update this to your desired path)
file_path = r"students.txt"  # Use raw string to handle backslashes

def load_students_from_file():
    try:
        with open(file_path, "r") as file:
            for line in file:
                name, age, grade = line.strip().split(", ")
                students.append({"name": name, "age": age, "grade": grade})
    except FileNotFoundError:
        print("No student data found. A new file will be created once you add a student.\n")

def save_students_to_file():
    with open(file_path, "w") as file:
        for student in students:
            file.write(f"{student['name']}, {student['age']}, {student['grade']}\n")

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    save_students_to_file()
    print(f"Student {name} added successfully!\n")

def view_students():
    if not students:
        print("No students available.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()

def search_student():
    name = input("Enter the name of the student to search: ")
    for student in students:
        if student['name'] == name:
            print(f"Found - Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    print("Student not found.\n")

def delete_student():
    name = input("Enter the name of the student to delete: ")
    for student in students:
        if student['name'] == name:
            students.remove(student)
            save_students_to_file()
            print(f"Student {name} deleted successfully!\n")
            return
    print("Student not found.\n")

def menu():
    print("Student Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

# Load existing students from file at program start
load_students_from_file()

# Main Program Loop
while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
