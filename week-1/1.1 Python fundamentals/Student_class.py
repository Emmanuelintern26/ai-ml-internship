import pandas as pd
import json

class Student:

    def __init__(self,name,student_id,grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
        self.gpa = 0

    def calculate_gpa(self):
        print(self.grades)
        grade_dict = json.loads(self.grades.iloc[0])
        print(grade_dict)
        for value in grade_dict.values():
            self.gpa += value/len(grade_dict.values())
    