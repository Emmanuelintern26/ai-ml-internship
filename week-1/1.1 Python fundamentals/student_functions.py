import pandas as pd
import json


def read_records(student_records):

    try:
        file = pd.read_csv(student_records)
        print("File ready")
        return file
        
    except:
        print("Record file does not exit")


def edit_record(student_record):
    df = pd.read_csv(student_record)
    print('Enter Student Data: ')
    name = input("Student Name: ")
    math = int(input("Math Score: "))
    english = int(input("English score: "))
    science = int(input("Science score: "))\
    
    new_data = pd.DataFrame(
        [
            {
                "name":name,
                "student_id":f"STU00{df.shape[0]+1}",
                "grades" : json.dumps({"math": math,"english":english,"science":science})
            }
        ]
    )
    
    new_data.to_csv(student_record,mode="a",header=False, index=False)
    print("Students record updated")
    