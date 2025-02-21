# Create functions


def update(x):
    print(id(x))
    x=8
    print("x = ",x)

a = 10
update(a)
print(id(a))
print("a =",a)


#Arguments


def add(a,b):
    c=a+b
    print(c)


add(10,15) #actual argument

def person(age,name):
    print(age)
    print(name)

def sum(a,*b):
    c=a
    for i in b:
        c=c+i;
    print(c)

sum(10,15,16,17)

def personDetails(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


personDetails("Akshay",age=20,city="mumbai",mob=9876543210)



#postion
#keyword => person(age=28,name="Akshay")
#default => providing default value to the parameters
#variable length => add(a, *b) => b will accept multiple values in Tuple


#Pass list to functions in python


