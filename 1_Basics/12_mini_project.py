# Tuple Mini Project

employees = [
    ("EMP001", "Ayush", 25),
    ("EMP002", "Rohan", 28),
    ("EMP003", "Harry", 28),
]

def print_employee(employee_list):
    for emp in employee_list:
        for element in emp:
            print(f"{element}\n");

print_employee(employees);

def print_salary(employee_list):
    total = 0;
    for el in employee_list:
        id, name, salary = el;
        total += salary;
    print(f"total salary: {total} thousand");
    print(f"Average Salary: {total/len(employee_list)} thousand")

print_salary(employees);