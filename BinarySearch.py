
def binarysearch(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid = (l + u)//2
        if list[mid] == n:
            return True
        else:
            if list[mid]< n:
                l = mid+1
            else:
                u = mid-1
    return False



list = [4,5,8,10,45,99]
n= 45
if binarysearch(list,n):
    print("Found")
else:
    print("Not Found")