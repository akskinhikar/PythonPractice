

class Student:

    school = 'ModernSchool'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self):
        return (self.m1+self.m2+self.m3)/3

s1 = Student(35,56,33)
s2 = Student(54,32,55)

print("Average = " ,s1.average())
print("Average = " ,s2.average())

