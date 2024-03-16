class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def set_Name(self,name):
        self.name = name
    def print_Name(self):
        print(self.name)

s = Student('brian', 'A')
s.print_Name()
s.set_Name('Peter')
s.print_Name()
