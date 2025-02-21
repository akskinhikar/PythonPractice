


def count(lst):
    even =0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


lst = [20,25,34,21,45,67,29]
even,odd = count(lst)
print("Even : {} and Odd : {}".format(even,odd))


