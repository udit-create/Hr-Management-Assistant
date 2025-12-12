import pandas as pd


def show_salary(file_path, emp_id):
    df = pd.read_csv(file_path)
    emp_id = int(emp_id)

    emp = df[df['EmpID'] == emp_id]
    if not emp.empty:
        name = emp.iloc[0]['Name']
        salary = emp.iloc[0]['Salary']
        return f"Salary Slip\n\nEmployee ID: {emp_id}\nName: {name}\nSalary: ₹{salary:.2f}"
    else:
        raise ValueError("Employee not found.")