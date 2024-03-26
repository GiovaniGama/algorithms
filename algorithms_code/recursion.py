def sum(arr):
    if(len(arr) == 1):
        return arr[0]
    elif(arr == []):
        return 0
    
    return arr[0] + sum(arr[1:])

print(sum([5,3,4]))


def count(arr):
    if(arr == []):
        return 0
    
    return 1 + count(arr[1:])

print(count([5,3,4]))

def max(arr):
    if(len(arr) == 2):
        return arr[0] if arr[0] > arr[1] else arr[1]
    elif(len(arr) == 1):
        return arr[0]
    
    sub_max = max(arr[1:])
    print("sub_max",sub_max)
    return arr[0] if arr[0] > sub_max else sub_max

print(max([5,4,10]))