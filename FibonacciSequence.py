


def gererateFiboonacciSeq(num):
    if num == 1:
        print(num)
    elif num <= 0 :
        print("Number {} cannot be negative or zero".format(num))
    else:
        first = 0
        second = 1
        print(first)
        print(second)
        for i in range(2,num):
            third = first + second
            first = second
            second = third
            num-=1
            print(third)


gererateFiboonacciSeq(10)
