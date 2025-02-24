class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.company = "HP"
            self.model = "T302"
            self.ram = "5T"

        def show(self):
            print(self.company,self.model,self.ram)


s1 = Student("Akshay", 3)
s2 = Student("Ameya", 5)

s1.show()
