import tkinter as tk
from tkinter import messagebox

from employee import add_employee
from attendance import mark_attendance
from leave import apply_leave
from salary import show_salary
from performance import update_performance

file_path = 'database.csv'

# ------------------------- Add Employee -------------------------
def add_employee_form():
    form = tk.Toplevel(root)
    form.title("Add Employee")

    labels = ["Employee ID", "Name", "Age", "Department", "Salary"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(form)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    def submit():
        try:
            emp_id = entries[0].get()
            name = entries[1].get()
            age = entries[2].get()
            dept = entries[3].get()
            salary = entries[4].get()
            add_employee(file_path, emp_id, name, age, dept, salary)
            messagebox.showinfo("Success", "Employee added successfully!")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add employee: {e}")

    tk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

# ------------------------- Mark Attendance -------------------------
def mark_attendance_form():
    form = tk.Toplevel(root)
    form.title("Mark Attendance")

    tk.Label(form, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(form)
    entry.grid(row=0, column=1, padx=10, pady=5)

    def submit():
        emp_id = entry.get()
        try:
            mark_attendance(file_path, emp_id)
            messagebox.showinfo("Success", "Attendance marked successfully!")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(form, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

# ------------------------- Apply Leave -------------------------
def apply_leave_form():
    form = tk.Toplevel(root)
    form.title("Apply Leave")

    tk.Label(form, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(form)
    entry.grid(row=0, column=1, padx=10, pady=5)

    def submit():
        emp_id = entry.get()
        try:
            apply_leave(file_path, emp_id)
            messagebox.showinfo("Success", "Leave applied successfully!")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(form, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

# ------------------------- Show Salary -------------------------
def show_salary_form():
    form = tk.Toplevel(root)
    form.title("Show Salary")

    tk.Label(form, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
    entry = tk.Entry(form)
    entry.grid(row=0, column=1, padx=10, pady=5)

    def submit():
        emp_id = entry.get()
        try:
            slip = show_salary(file_path, emp_id)
            display_salary_slip(slip)
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(form, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

def display_salary_slip(slip_text):
    slip_window = tk.Toplevel(root)
    slip_window.title("Salary Slip")
    text = tk.Text(slip_window, width=50, height=15)
    text.pack(padx=10, pady=10)
    text.insert(tk.END, slip_text)
    text.config(state=tk.DISABLED)

# ------------------------- Update Performance -------------------------
def update_performance_form():
    form = tk.Toplevel(root)
    form.title("Update Performance")

    tk.Label(form, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
    emp_id_entry = tk.Entry(form)
    emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form, text="Performance Rating").grid(row=1, column=0, padx=10, pady=5)
    rating_var = tk.StringVar()
    rating_menu = tk.OptionMenu(form, rating_var, "Excellent", "Good", "Average", "Poor")
    rating_menu.grid(row=1, column=1, padx=10, pady=5)
    rating_var.set("Average")

    def submit():
        emp_id = emp_id_entry.get()
        rating = rating_var.get()
        try:
            update_performance(file_path, emp_id, rating)
            messagebox.showinfo("Success", "Performance updated successfully!")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(form, text="Submit", command=submit).grid(row=2, column=0, columnspan=2, pady=10)

# ------------------------- Main GUI -------------------------
def start_gui():
    global root
    root = tk.Tk()
    root.title("HR Management Assistant")
    root.geometry("400x450")
    root.config(bg="#f0f0f0")

    tk.Label(root, text="HR Management Assistant", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)

    tk.Button(root, text="Add Employee", width=30, command=add_employee_form).pack(pady=5)
    tk.Button(root, text="Mark Attendance", width=30, command=mark_attendance_form).pack(pady=5)
    tk.Button(root, text="Apply Leave", width=30, command=apply_leave_form).pack(pady=5)
    tk.Button(root, text="Show Salary", width=30, command=show_salary_form).pack(pady=5)
    tk.Button(root, text="Update Performance", width=30, command=update_performance_form).pack(pady=5)
    tk.Button(root, text="Exit", width=30, command=root.destroy).pack(pady=20)

    root.mainloop()

# ------------------------- Run the GUI -------------------------
if __name__ == "__main__":
    start_gui()
