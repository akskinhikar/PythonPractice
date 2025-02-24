from operator import index

pos = 0
posi = 0
def search(arr,n):
    i=0
    while i<len(arr):
        if arr[i]==n:
            globals()['pos'] = i
            return True
        i=i+1
    return False

def search2(arr,n):
    for i in arr:
        if i == n:
            globals()['posi'] = arr.index(i)
            return True
    return False



arr = [5,10,9,34,2]
n=9

if search2(arr,n):
    print("Found", posi)
else:
    print("Not Found")

