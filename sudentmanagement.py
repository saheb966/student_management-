import tkinter as tk
from tkinter import messagebox
import csv
import os

file_name = "student_data.csv"

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Labels and Entry Widgets
        tk.Label(root, text="Name").grid(row=0, column=0)
        tk.Label(root, text="Age").grid(row=1, column=0)
        tk.Label(root, text="Class").grid(row=2, column=0)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.class_var = tk.StringVar()

        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(root, textvariable=self.age_var).grid(row=1, column=1)
        tk.Entry(root, textvariable=self.class_var).grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Student", command=self.add_student).grid(row=3, column=0)
        tk.Button(root, text="View Students", command=self.view_students).grid(row=3, column=1)
        tk.Button(root, text="Clear", command=self.clear_entries).grid(row=3, column=2)

        self.display = tk.Text(root, height=10, width=50)
        self.display.grid(row=4, column=0, columnspan=3)

    def add_student(self):
        name = self.name_var.get()
        age = self.age_var.get()
        std_class = self.class_var.get()

        if not (name and age and std_class):
            messagebox.showwarning("Input Error", "Please fill all fields")
            return

        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            if os.stat(file_name).st_size == 0:
                writer.writerow(["Name", "Age", "Class"])
            writer.writerow([name, age, std_class])
        messagebox.showinfo("Success", "Student Added")
        self.clear_entries()

    def view_students(self):
        self.display.delete("1.0", tk.END)
        if not os.path.exists(file_name):
            self.display.insert(tk.END, "No data found.")
            return
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.display.insert(tk.END, f"{' | '.join(row)}\n")

    def clear_entries(self):
        self.name_var.set("")
        self.age_var.set("")
        self.class_var.set("")
        self.display.delete("1.0", tk.END)

root = tk.Tk()
app = StudentManagementApp(root)
root.mainloop()
