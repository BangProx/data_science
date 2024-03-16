class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
    
    def assign_department(self, department):
        self.department = department

    def print_employee_details(self):
        print('EMPLOYEE ID:',self.id)
        print('EMPLOYEE NAME:',self.name)
        print('EMPLOYEE SALARY:',self.salary)
        print('EMPLOYEE DEPARMENT:',self.department)

    def caculate_emp_salary(self, hours_worked):
        salary = self.salary
        overtime = hours_worked - 50
        return salary + (overtime-salary/50)

emp1 = Employee('ADAMS','E7876',50000,'ACCOUNTING')
emp2 = Employee('JONES','E7499',45000,'RESEARCH')
emp3 = Employee('MARTIN', 'E7900',50000,'SALES')
emp4 = Employee('SMITH','E7698',55000,'OPERATIONS')

emp1.print_employee_details()
emp1.assign_department('MARKETING')
emp1.print_employee_details()

print('This month salary is', emp1.caculate_emp_salary(60))