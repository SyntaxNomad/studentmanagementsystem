from Class import Student
from students import StudentMethods

def main():
    message = ""
    while True:
        print("Welcome to the student information system")
        print("1. Write student data to a file")
        print("2. Read student data from a file")
        print("3. Add a new student")
        print("4. Find a student by student number")
        print("5. Show all students")
        print("6. Show all students born in a given year")
        print("7. Modify student record")
        print("8. Delete student")
        print("9. Quit")

        if message:
            print(message)
            message = ""

        choice = input("Enter your choice: ")

        # First choice: Write student data to a file
        if choice == "1":
            StudentMethods.save_students_to_file()
            message = "Student data written to file."
        
        # Second choice: Read student data from a file
        elif choice == "2":
            StudentMethods.load_students_from_file()
            message = "Student data read from file and array has been populated."
        
        # Third choice: Add a new student
        elif choice == "3":
            Student.add_student()
            message = "New student added."
        
        # Fourth choice: Find a student by student number
        elif choice == "4":
            studentnumber = input("Enter your student number: ")
            student = Student.find_student_by_number(studentnumber)
            if student:
                print("\n" + "=" * 80)
                print(f"{'Student Number':<15}{'Name':<25}{'DOB':<15}{'Gender':<10}{'Nationality':<15}{'Age':<5}")
                print("-" * 80)
                print(f"{student.get_student_number():<15}{student.get_first_name()} {student.get_last_name():<25}{student.get_DOB():<15}{student.get_gender():<10}{student.get_nationality():<15}{student.get_age():<5}")
                print("=" * 80)
                message = "Student search completed."
            else:
                message = "Student not found."
        
        # Fifth choice: Show all students
        elif choice == "5":
            Student.show_all_students()
            message = "Displayed all students."
        
        # Sixth choice: Show all students born in a given year
        elif choice == "6":
            year = input("Enter the year: ")
            Student.show_students_by_year(year)
            message = "Displayed students born in the given year."
        
        # Seventh choice: Modify student record
        elif choice == "7":
            Student.modify_student()
            message = "Student record modified."
        
        # Eighth choice: Delete student
        elif choice == "8":
            studentno = input("Enter student number: ")
            Student.delete_student(studentno)
            message = "Student deleted."
        
        # Ninth choice: Quit
        elif choice == "9":
            break

if __name__ == "__main__":
    main()