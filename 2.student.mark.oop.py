class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_course_name(self, course_name):
        self.__course_name = course_name


class Marks:
    def __init__(self):
        self.__marks = {}

    def add_mark(self, student_id, course_id, mark):
        if student_id not in self.__marks:
            self.__marks[student_id] = {}

        self.__marks[student_id][course_id] = mark

    def get_mark(self, student_id, course_id):
        student_marks = self.__marks.get(student_id)
        if student_marks:
            return student_marks.get(course_id)
        return None

    def get_all_marks(self):
        return self.__marks.copy()


class Utils:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Marks()

    def input_number_of_students(self):
        num_students = int(input("Enter the number of students: "))
        return num_students

    def input_student_information(self):
        for _ in range(self.__num_students):
            student_id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student date of birth: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_number_of_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        return num_courses

    def input_course_information(self):
        for _ in range(self.__num_courses):
            course_id = input("Enter the course ID: ")
            course_name = input("Enter the course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        student_id = input("Enter the student ID: ")
        course_id = input("Enter the course ID: ")
        mark = float(input("Enter the mark: "))
        self.marks.add_mark(student_id, course_id, mark)

    def display_student_information(self):
        print("Student Information:")
        for student in self.students:
            print(
                f"Student ID: {student.get_student_id()}, Name: {student.get_name()}, DOB: {student.get_dob()}"
            )

    def display_course_information(self):
        print("Course Information:")
        for course in self.courses:
            print(f"Course ID: {course.get_course_id()}, Name: {course.get_course_name()}")

    def display_marks(self):
        print("Marks:")
        all_marks = self.marks.get_all_marks()
        for student_id, courses in all_marks.items():
            for course_id, mark in courses.items():
                print(f"Student ID: {student_id}, Course ID: {course_id}, Mark: {mark}")


class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__utils = Utils()

    def input_number_of_students(self):
        self.__num_students = self.__utils.input_number_of_students()

    def input_student_information(self):
        self.__utils.input_student_information()

    def input_number_of_courses(self):
        self.__num_courses = self.__utils.input_number_of_courses()

    def input_course_information(self):
        self.__utils.input_course_information()

    def input_marks(self):
        self.__utils.input_marks()

    def display_students(self):
        self.__utils.display_student_information()

    def display_courses(self):
        self.__utils.display_course_information()

    def display_marks(self):
        self.__utils.display_marks()

# Main function for the program
def main():
    university = University()

    while True:
        print("Menu:")
        print("0. Exit")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input marks")
        print("6. Display student information")
        print("7. Display course information")
        print("8. Display marks")

        choice = int(input("Enter your choice: "))

        match choice:
            case 0:
                break
            case 1:
                university.input_number_of_students()
            case 2:
                university.input_student_information()
            case 3:
                university.input_number_of_courses()
            case 4:
                university.input_course_information()
            case 5:
                university.input_marks()
            case 6:
                university.display_students()
            case 7:
                university.display_courses()
            case 8:
                university.display_marks()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()