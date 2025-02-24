# Bubble sort

list = [5,3,8,6,7,2]

for i in range(len(list)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)


#Selection sort

list1 = [5,3,8,6,7,2]

for i in range(len(list1)):
    minpos = i
    for j in range(i,6):
        if list1[j] < list1[minpos]:
            minpos = j

    temp = list1[i]
    list1[i] = list1[minpos]
    list1[minpos]= temp

print(list1)