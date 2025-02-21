

#function to travers list and find count of evens and odds
def count(lst):
    even =0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

# empty list
lst1=[]
#getting list from user
size = int(input("Enter size of the list = "))
for i in range(size):
    ele = int(input("Provide the List Numbers :"))
    lst1.append(ele)

print(lst1)

even,odd = count(lst1)
print(even)
print(odd)



