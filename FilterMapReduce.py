from functools import reduce

print("Code without Lamda")
def is_even(n):
    return n%2==0


def double(n):
    return n*2

def addition(a,b):
    return a+b

nums= [3,2,6,8,4,6,29]

evens_nums = list(filter(is_even,nums))
doubles = list(map(double,evens_nums))
print(evens_nums)
print(doubles)

print("** Same code with Lamda **")

evens_nums_with_lamda = list(filter(lambda n:n%2==0,nums))
doubles_with_lamda = list(map(lambda n: n*2, evens_nums_with_lamda))

print(evens_nums_with_lamda)
print(doubles_with_lamda)

sums = reduce(addition,doubles)
print(sums)

sums_with_Lamda = reduce(lambda a,b:a+b,doubles_with_lamda)
print(sums_with_Lamda)