class Employee:
    def __init__(self,name,id,salary,department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
    def assign_department(self,department):
        self.department = department
    def print_employee_details(self):
        print(self.name,',',self.id,',',self.salary,',',self.department)
    def calculate_emp_salary(self,hours_worked):
        salary = self.salary
        overtime = hours_worked - 50
        overtime_amount = (overtime*(salary/50))
        if overtime > 0:
            salary = salary + overtime_amount
        print(salary)

emp1 = Employee('ADAMS','E7868',50000,'ACCOUNTING')
emp2 = Employee('JONES','E7499',45000,'RESEARCH')
emp3 = Employee('MARTIN','E7900',50000,'SALES')
emp4 = Employee('SMITH','E7698',55000,'OPERATIONS')

emp3.print_employee_details()
emp3.assign_department('ACCOUNTING')
emp3.print_employee_details()
emp1.calculate_emp_salary(60)
emp3.calculate_emp_salary(40)