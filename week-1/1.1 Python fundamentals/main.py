# MINI STUDENT RECORD & GRADE MANAGEMENT SYSTEM
# TODOS: 
#       - Student class with attributes (name,student id,grades dictionary) 
#           and method (to calculate GPA/average)
#       - A function that reads students records from a file and handles
#           FileNotFound with a try/except
#       - A loop that allows adding student entries and 
#           analyzing the dataset using list and dictionaries

import pandas as pd
import json
from Student_class import Student
from student_functions import edit_record,read_records
    
def main():

    record = "./student_records.csv"
    print("="*50)
    print("Welcome to the MINI STUDENT RECORD & GRADE MANAGEMENT SYSTEM")
    print("="*50)

    while True:
        print("\nWhat will like to do today: ")
        print("[1] Read Student records \n[2] Calculate GPA \n[3] Edit Student records (staff only) \n[6] Exit")

        ans = int(input(":=> "))
        df = pd.read_csv(record)
        if ans == 3:
            edit_record(record)
            
        elif ans == 2:
            student = str(input("Enter student ID: "))
            try:
                stud_data = df[df["student_id"]== student]

                stud = Student(stud_data["name"],stud_data["student_id"],stud_data["grades"])
                stud.calculate_gpa()
                print(f"\n{stud_data["name"].iloc[0]} has an average score of {round(stud.gpa,2)}\n")
            except:
                print(f"Student with ID {student} doesn't exist")
        elif ans == 1:
            data = read_records(record)
            print(data)
        else:
            break


main()

