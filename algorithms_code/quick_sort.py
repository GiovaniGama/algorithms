def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    elif(arr == []):
        return 0
    
    pivo = arr[0]
    menores = [i for i in arr[1:] if i <= pivo]
    maiores = [i for i in arr[1:] if i > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)


print(quick_sort([3,1,4,6,21,2323,54,122]))