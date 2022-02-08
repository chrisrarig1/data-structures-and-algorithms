## Tested our whiteboard 
array = [2,4,6,7,-8]

def ArrayFunc(n):
    length = len(array)
    x = length/2
    print(x)
    if x % 1 != 0:
        x = x + 0.5
    
    
    return array
    
print(ArrayFunc(5))
