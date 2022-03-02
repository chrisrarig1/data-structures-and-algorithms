def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        x = i-1

        while x >= 0 and temp < arr[x]:
            arr[x+1] = arr[x]
            x = x-1
        
        arr[x + 1] = temp

arr = [25, 1, 16, 5]
insert_sort(arr)
for i in range(len(arr)):
    print(arr[i])