def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    elif(arr == []):
        return 0
    
    pivo = arr[0]
    menores = [i for i in arr[1:] if i <= pivo]
    maiores = [i for i in arr[1:] if i > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)

def binarySearch(list, element, start=0, end=None):
    if end == None:
        end = len(list) - 1
    
    if start > end:
        return -1

    arr = quick_sort(list)

    middle = (end+start) // 2

    if arr[middle] == element:
        return middle
    elif arr[middle] > element:
        return binarySearch(list, element, start, middle-1)
    elif arr[middle] < element:
        return binarySearch(list, element, middle+1, end)
    

arr = [3,1,4,6,21,2323,54,122]
item = 122

print(binarySearch(arr, item))
