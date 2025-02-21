def factorialwithrecursion(num):
    if num==0:
        return 1
    return num * factorialwithrecursion(num-1)


result = factorialwithrecursion(5)
print(result)