# Mini Student Record & Grade Management System

A simple Python console application that manages student records stored in a CSV file. The system allows users to view records, calculate a student's average score (GPA), and add new student records.
(This covers most python fundamentals - loops,functions, inputs/outputs, Classes, variables, data types,conditionals and so on)

## Features

- Read and display all student records
- Calculate a student's average score using their Student ID
- Add new student records (staff only)
- Store grades in JSON format within a CSV file
- Handle missing files using exception handling

## Technologies Used

- Python3
- Pandas
- JSON

## Project Structure

```
.
├── main.py      # Main application
├── student_records.csv        # Student database
├── Student_class.py   # Student class with attributes and methods 
├── student_functions.py  # functions to read and edit the database
└──README.md
```

## CSV Format

| Name | Student ID | Grades |
|------|------------|--------|
| Alice Smith | STU001 | `{"math":85,"english":92,"science":78}` |

## How to Run

1. Install the required dependency:

```bash
pip install pandas
```

2. Run the program:

```bash
python main.py
```

## Menu Options

| Option | Description |
|---------|-------------|
| `1` | Read all student records |
| `2` | Calculate GPA |
| `3` | Add a new student record |
| `6` | Exit the program |

## Example

```text
==================================================
Welcome to the MINI STUDENT RECORD & GRADE MANAGEMENT SYSTEM
==================================================

[1] Read Student records
[2] Calculate GPA
[3] Edit Student records (staff only)
[6] Exit
```

## Author

**Emmanuel Ahene Adjei**