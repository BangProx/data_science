class Employee:
    def __init__(self,emp_name,emp_id,emp_salary,emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self,hours_worked):
        salary = self.emp_salary
        overtime = hours_worked - 50
        return int(salary + overtime*(salary/50))

    def assign_department(self,dpt):
        self.emp_department = dpt
    
    def print_emp_details(self):
        print('name : ', self.emp_name)
        print('id : ', self.emp_id)
        print('salary : ', self.emp_salary)
        print('department : ', self.emp_department)

a = Employee('ADAMS','E7876',50000,'ACCOUNTING')
j = Employee('JONES','E7499',45000,'RESEARCH')
m = Employee('MARTIN','E7900',50000,'SALES')
s = Employee('SMITH','E7698',55000,'OPERATIONS')

a.print_emp_details() 
print('This month salary is ', a.calculate_emp_salary(70))
a.assign_department('R&D')
a.print_emp_details()