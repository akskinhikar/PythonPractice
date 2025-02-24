#Method Overriding

from multipledispatch import dispatch


class A:
    def show(self):
        print("In Class A show method")


class B(A):
    #pass

    def show(self):
        print("In Class B show method")


b1 = B()
b1.show()


#Method Overloading

class Addition:
    def add(self,a=None,b=None,c=None):
        if a != None and b != None and c == None:
            s = a + b
            print(s)
        else:
            s = a + b + c
            print(s)

a1 = Addition()
a1.add(10,20)
a1.add(10,20,30)


class Multiplication:
    @dispatch(int,int)
    def mul(self,a,b):
        m=a*b
        print(m)

    @dispatch(int,int,int)
    def mul(self,a,b,c):
        m=a*b*c
        print(m)

    @dispatch(float,float)
    def mul(self,a,b):
        m=a*b
        print(m)

    @dispatch(float,int,int)
    def mul(self,a,b,c):
        m=a*b*c
        print(m)



m1=Multiplication()
m1.mul(2,3)
m1.mul(2,3,4)
m1.mul(2.1,2,3)
m1.mul(2.1,2.1)

