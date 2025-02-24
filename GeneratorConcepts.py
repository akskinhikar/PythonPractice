def topten():

    yield 1
    yield 2
    yield 3



values = topten()

print(values.__next__())
print(values.__next__())
print(values.__next__())