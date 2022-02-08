array = [2,4,6,7,8,10,12,15,16]
def binary_search(n,array):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = low +(high - low)//2
        if n == array[mid]:
            return mid
        if n < array[mid]:
            high = mid-1
        else:
            low  = mid + 1
    return -1
         
print(binary_search(15,array))