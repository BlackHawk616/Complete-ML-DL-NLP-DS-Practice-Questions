# 5️⃣ Employee Payroll System Create an employee system that calculates salary based on role, working hours, or fixed pay using OOP concepts.

class Employee:
    def __init__(self, name, role, working_hours=0, fixed_pay=0):
        self.name = name
        self.role = role
        self.working_hours = working_hours
        self.fixedpay = fixed_pay

    def calculate_salary(self):
        if self.role == "Manager":
            return self.fixedpay
        elif self.role == "Developer":
            return self.working_hours * 20  # Assuming $20 per hour
        else:
            return 0
        
employee1 = Employee("John Doe", "Manager", fixed_pay=5000)
employee2 = Employee("Jane Smith", "Developer", working_hours=160)
print(f"{employee1.name} ({employee1.role}) Salary: ${employee1.calculate_salary()}")
print(f"{employee2.name} ({employee2.role}) Salary: ${employee2.calculate_salary()}")
