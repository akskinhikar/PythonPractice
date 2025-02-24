class Iterator:
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)

    print(next(myit))
    print(next(myit))
    print(next(myit))

    for i in mytuple:
        print(i)



