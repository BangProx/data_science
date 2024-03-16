class Student:
    def __init__(self,name,mark):
        self.student_name = name
        self.student_mark = mark
    def set_Name(self,name):
        self.student_name = name
    def print_Name(self):
        print(self.student_name)

s = Student('Brian',90)
print(s.student_name, int(s.student_mark))
s.student_mark = 80
print(s.student_name, int(s.student_mark))

s.print_Name()
s.set_Name('V')
s.print_Name()