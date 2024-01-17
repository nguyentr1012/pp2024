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

    while True:
        # Display the menu
        print("Menu:")
        print("0. Exit")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input marks for a course")
        print("6. List all courses")
        print("7. List all students")
        print("8. Show student marks for a course")

        choice = int(input("Select an operation by entering its number: "))

        if choice == 0:
            break

        match choice:
            case 1:
                input_num_students()
            case 2:
                input_student_info()
            case 3:
                input_num_courses()
            case 4:
                input_course_info()
            case 5:
                input_student_marks(students, courses)
            case 6:
                list_courses(courses)
            case 7:
                list_students(students)
            case 8:
                show_student_marks(students, marks)
            case _:
                print("Invalid choice. Please try again.")