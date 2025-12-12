import pandas as pd
import os

def add_employee(file_path, emp_id, name, age, dept, salary):
    # Create file with headers if it doesn't exist
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=[
            'EmpID', 'Name', 'Age', 'Department', 'Salary', 'Attendance', 'Leaves', 'Performance'
        ])
    else:
        df = pd.read_csv(file_path)

    new_row = {
        'EmpID': int(emp_id),
        'Name': name,
        'Age': int(age),
        'Department': dept,
        'Salary': float(salary),
        'Attendance': 0,
        'Leaves': 0,
        'Performance': 'Average'
    }

    df = df._append(new_row, ignore_index=True)
    df.to_csv(file_path, index=False)