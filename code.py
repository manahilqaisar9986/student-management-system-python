# ==========================================
#       STUDENT MANAGEMENT SYSTEM
# ==========================================

# List to store student records
students = []


# ------------------ Add Student ------------------
def add_student():
    print("\n--- Add New Student ---")

    name = input("Enter Student Name: ").strip()
    roll_no = input("Enter Roll Number: ").strip()

    # Check if roll number already exists
    for student in students:
        if student["roll_no"] == roll_no:
            print("Error: Roll Number already exists!")
            return

    # Validate marks
    while True:
        try:
            marks = int(input("Enter Marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Marks should be between 0 and 100.")

        except ValueError:
            print("Please enter valid numeric marks.")

    # Create dictionary
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


# ------------------ View Students ------------------
def view_students():

    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    print("-" * 40)
    print("Roll No\tName\t\tMarks")
    print("-" * 40)

    for student in students:
        print(f"{student['roll_no']}\t{student['name']}\t\t{student['marks']}")

    print("-" * 40)
    print("Total Students:", len(students))


# ------------------ Search Student ------------------
def search_student():

    print("\n--- Search Student ---")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent Found")
            print("------------------")
            print("Name     :", student["name"])
            print("Roll No  :", student["roll_no"])
            print("Marks    :", student["marks"])
            return

    print("Student not found.")


# ------------------ Delete Student ------------------
def delete_student():

    print("\n--- Delete Student ---")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# ------------------ Main Menu ------------------
while True:

    print("\n===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

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
        print("Thank you for using the Student Management System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")