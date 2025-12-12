import pandas as pd

def update_performance(file_path, emp_id, rating):
    df = pd.read_csv(file_path)
    emp_id = int(emp_id)

    if emp_id in df['EmpID'].values:
        df.loc[df['EmpID'] == emp_id, 'Performance'] = rating
        df.to_csv(file_path, index=False)
        return True
    else:
        raise ValueError("Employee not found.")
