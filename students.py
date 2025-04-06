from Class import Student, students

class StudentMethods:
    #Saves students array information to .txt file
    @staticmethod
    def save_students_to_file(filename="info.txt"):
        with open(filename, "w") as file:
            for student in students:
                file.write(f"{student.get_student_number()},{student.get_first_name()},{student.get_last_name()},{student.get_DOB()},{student.get_gender()},{student.get_nationality()}\n")
    #loads student information from .txt file to student array
    @staticmethod
    def load_students_from_file(filename="info.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    student_data = line.strip().split(",")
                    student_number, first_name, last_name, DOB, gender, nationality = student_data
                    Student(student_number, first_name, last_name, DOB, gender, nationality)
        except FileNotFoundError:
            print("No saved data found.")