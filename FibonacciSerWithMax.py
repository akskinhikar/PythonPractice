def generatFibonacciSerWithMax(num):
    first = 0
    second = 1
    third = 0
    print(first)
    print(second)
    while third<num:
        third = first + second
        first = second
        second = third
        if third<num:
            print(third)


generatFibonacciSerWithMax(100)