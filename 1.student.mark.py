# Input the number of students in a class
def input_num_students():
    return int(input("Enter the number of students in the class: "))

# Input student information: id, name, DoB
def input_student_info():
    student = {}
    student["id"] = input("Enter student ID: ")
    student["name"] = input("Enter student name: ")
    student["DoB"] = input("Enter student date of birth: ")
    return student

# Input the number of courses
def input_num_courses():
    return int(input("Enter the number of courses: "))

# Input course information: id, name
def input_course_info():
    course = {}
    course["id"] = input("Enter course ID: ")
    course["name"] = input("Enter course name: ")
    return course

# Input marks for students in a specific course
def input_student_marks(students, course):
    marks = {}
    for student in students:
        while True:
            mark = float(input(f"Enter the mark for student {student['name']} in course {course['name']}: "))
            if mark <= 4.0:
                marks[student["id"]] = mark
                break
            else:
                print("Invalid mark! Maximum allowed mark is 4.0.")
    return marks

# List all the courses
def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

# List all the students
def list_students(students):
    print("List of students:")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}")

# Show student marks for a given course
def show_student_marks(students, marks, course):
    print(f"Student marks for course {course['name']}:")
    for student in students:
        student_id = student["id"]
        if student_id in marks:
            mark = marks[student_id]
            print(f"Student ID: {student_id}, Student Name: {student['name']}, Mark: {mark}")
        else:
            print(f"Student ID: {student_id}, Student Name: {student['name']}, Mark: Not available")

# Main function for the program
def main():
    # Initialize lists and variables
    students = []
    courses = []
    marks = {}

    # Define the list of operations
    operations = [
        ("Exit", None),
        ("Input number of students", input_num_students),
        ("Input student information", input_student_info),
        ("Input number of courses", input_num_courses),
        ("Input course information", input_course_info),
        ("Input marks for a course", input_student_marks),
        ("List all courses", list_courses),
        ("List all students", list_students),
        ("Show student marks for a course", show_student_marks)
    ]

    while True:
        # Display the menu
        print("Menu:")
        for i, (operation, _) in enumerate(operations):
            print(f"{i}. {operation}")

        choice = int(input("Select an operation by entering its number: "))

        if choice == 0:
            break

        # Execute the selected operation
        _, operation = operations[choice]
        if operation is not None:
            operation(students, courses, marks)

# Call the main function
if __name__ == "__main__":
    main()