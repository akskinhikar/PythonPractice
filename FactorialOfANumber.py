def factorialofnum(num):
    factorial = 1
    while num>0 :
        factorial = num * factorial
        num-=1

    print(factorial)


factorialofnum(4)

def factorialofnum1(num1):
    factorial = 1
    for i in range(1,num1+1):
        factorial = factorial * i

    print(factorial)

factorialofnum1(5)