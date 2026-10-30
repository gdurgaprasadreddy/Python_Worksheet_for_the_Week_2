class Employee:

    def __init__(self,employee_id,employee_name,salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Salary:", self.salary)

emp1 = Employee(1001, "Sai", 25000)
emp2 = Employee(1023, "Kumar", 30000)
emp3 = Employee(1012, "Ravi", 35000)

emp1.display_details()
print()
emp2.display_details()
print()
emp3.display_details()
