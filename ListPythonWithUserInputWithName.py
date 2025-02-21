def count(lst):
    for i in lst:
        if len(i) >= 5 :
            print(i)


lst = []
size = int(input("First provide the size of the list : "))
for i in range(size):
    ele = input("Provide the names : ")
    lst.append(ele)

count(lst)

