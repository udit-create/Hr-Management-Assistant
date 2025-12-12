import pandas as pd

def mark_attendance(file_path, emp_id):
    df = pd.read_csv(file_path)
    emp_id = int(emp_id)

    if emp_id in df['EmpID'].values:
        df.loc[df['EmpID'] == emp_id, 'Attendance'] += 1
        df.to_csv(file_path, index=False)
        return True
    else:
        raise ValueError("Employee not found.")