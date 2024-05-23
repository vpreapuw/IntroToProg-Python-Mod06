# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Vugee Preap,05/22/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")

    # CSV Answer
    # for row in file.readlines():
    #     # Transform the data from the file
    #     student_data = row.split(',')
    #     student_data = {"FirstName": student_data[0],
    #                     "LastName": student_data[1],
    #                     "CourseName": student_data[2].strip()}
    #     # Load it into our collection (list of lists)
    #     students.append(student_data)

    # JSON Answer
    students = json.load(file)

    file.close()
except Exception as e:
    print("Error: There was a problem with reading the file.")
    print("Please check that the file exists and that it is in a json format.")
    print("-- Technical Error Message -- ")
    print(e.__doc__)
    print(e.__str__())
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            # CSV answer
            # for student in students:
            #     csv_data = f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n'
            #     file.write(csv_data)

            # # JSON answer
            json.dump(students, file)

            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str = ''
students: list = []

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    FileProcessor.read_data_from_file(FILE_NAME, students)
except Exception as e:
    IO.output_error_messages("Error: There was a problem with reading the file.", e)

class FileProcessor:
    """Handles file processing tasks."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file into the student data list."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except Exception as e:
            IO.output_error_messages("Error reading from file", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes student data to a file."""
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file)
                IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("Error writing to file", e)

class IO:
    """Handles input and output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages with optional exception details."""
        print(message)
        if error:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error)

    @staticmethod
    def output_menu(menu: str):
        """Outputs the program menu."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Prompts the user for a menu choice and returns it."""
        return input("What would you like to do: ")

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user for student data and adds it to the list."""
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should only contain alphabets.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should only contain alphabets.")
            course_name = input("Enter the name of the course: ")
            student_data.append({"FirstName": first_name, "LastName": last_name, "CourseName": course_name})
        except ValueError as e:
            IO.output_error_messages("Invalid input", e)

    @staticmethod
    def output_student_courses(student_data: list):
        """Outputs student course information."""
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")

# Present and Process the data
while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)
    elif menu_choice == "2":
        IO.output_student_courses(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")


