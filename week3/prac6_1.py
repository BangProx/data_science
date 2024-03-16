class Student:
    def __init__(self,name,mark):
        self.student_name = name
        self.student_mark = mark

s = Student('Kim',90)

print(s.student_name, "gets mark of ",s.student_mark)

s.student_mark = 80

print(s.student_mark)