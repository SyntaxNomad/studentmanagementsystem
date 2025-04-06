# Description: This file contains the Student class and its methods.
#This import will be used to find the age later
from datetime import datetime

students = []

class Student:
    def __init__(self, student_number, first_name, last_name, DOB, gender, nationality):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__DOB = DOB
        self.__gender = gender
        self.__nationality = nationality
        students.append(self)


    
    # Setter Methods
    def set_student_number(self, student_number):
        self.__student_number = student_number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_DOB(self, DOB):
        self.__DOB = DOB
        
    def set_gender(self, gender):
        self.__gender = gender

    def set_nationality(self, nationality):
        self.__nationality = nationality

    # Getter Methods
    def get_first_name(self): 
        return self.__first_name
    
    def get_last_name(self): 
        return self.__last_name
    
    def get_student_number(self):
        return self.__student_number
    
    def get_DOB(self): 
        return self.__DOB
    
    def get_gender(self):
        return self.__gender
    
    def get_nationality(self):    
        return self.__nationality 

    def get_age(self): 
        # Calculate age based on DOB and current date works as mentioned previously
        today = datetime.now()
        dob_parts = self.__DOB.split("/")
        birth_month = int(dob_parts[0])
        birth_day = int(dob_parts[1])
        birth_year = int(dob_parts[2])   
        
        age = today.year - birth_year
        # Adjust age if birthday hasn't occurred yet this year
        if (today.month < birth_month) or (today.month == birth_month and today.day < birth_day):
            age -= 1
        return age
    #Add a new student instance to the students array
    @staticmethod
    def add_student():
        #if students array is full(more than 100), then do not add any more student instances
        if len(students)>=100:
            print("Cannot add more students. (The array is full)")
        studentno = input("Enter student number: ")
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        birthday = input("Enter Date of Birth (MM/DD/YYYY): ")
        gndr = input("Enter gender: ")
        nation = input("Enter nationality: ")
        student = Student(studentno, firstname, lastname, birthday, gndr, nation)
        print("Student added successfully.")
        #Table Formatting
        print("\n" + "=" * 80)
        print(f"{'Student Number':<15}{'Name':<25}{'DOB':<15}{'Gender':<10}{'Nationality':<15}{'Age':<5}")
        print("-" * 80)
        print(f"{student.get_student_number():<15}{student.get_first_name()} {student.get_last_name():<25}{student.get_DOB():<15}{student.get_gender():<10}{student.get_nationality():<15}{student.get_age():<5}")
        print("=" * 80)

    # Method to find a student by student number
    @staticmethod
    def find_student_by_number(student_number):
        for student in students:
            if student.get_student_number() == student_number:
                return student  # Returns the Student object
        return None  # Returns None if not found

    # Method to show all students
    @staticmethod
    def show_all_students():
        if not students:
            print("No students available.")
            return
        
        print("\n" + "=" * 80)
        print(f"{'Student Number':<15}{'Name':<25}{'DOB':<15}{'Gender':<10}{'Nationality':<15}{'Age':<5}")
        print("-" * 80)
    
        for student in students:
            print(f"{student.get_student_number():<15}{student.get_first_name()} {student.get_last_name():<25}{student.get_DOB():<15}{student.get_gender():<10}{student.get_nationality():<15}{student.get_age():<5}")
    
        print("=" * 80)
        print(f"Total students: {len(students)}")

    # Method to show students born in a specific year
    @staticmethod
    def show_students_by_year(year):
        found = False
        #More table formatting
        print("\n" + "=" * 80)
        print(f"{'Student Number':<15}{'Name':<25}{'DOB':<15}{'Gender':<10}{'Nationality':<15}{'Age':<5}")
        print("-" * 80)
        for student in students:
            if student.get_DOB().split("/")[-1] == year: 
                print(f"{student.get_student_number():<15}{student.get_first_name()} {student.get_last_name():<25}{student.get_DOB():<15}{student.get_gender():<10}{student.get_nationality():<15}{student.get_age():<5}")
                found = True
        
        if not found:
            print(f"No students born in {year} found.")
        print("=" * 80)

    # Method to modify a student's data
    @staticmethod
    def modify_student():
        student_number = input("Enter the student number: ")
        student = Student.find_student_by_number(student_number)

        if not student:
            print("Student not found")
            return False
        #Field to be modified chosen by user 
        field = input("Enter the field to modify (first_name, last_name, DOB, gender, nationality): ").lower()
        new_value = input(f"Enter new {field}: ")

        if field == "first_name":
            student.set_first_name(new_value)
        elif field == "last_name":
            student.set_last_name(new_value)
        elif field == "dob":
            student.set_DOB(new_value)
        elif field == "gender":
            student.set_gender(new_value)
        elif field == "nationality":
            student.set_nationality(new_value)
        else:
            print("Invalid field")
            return False

        print("Student record updated successfully.")
        return True

    # Method to delete a student
    @staticmethod
    def delete_student(student_number):
        student = Student.find_student_by_number(student_number)
        if student:
            students.remove(student)
            print("Student deleted successfully.")
            return True
        print("Student not found.")
        return False