array = [1,2,3,4,5]

def minMaxSum(arr):
    max_sum = 0
    min_sum = 0
    arrayValue = []

    for i in range(len(arr)):
        current_sum = sum([x for j, x in enumerate(arr) if j != i])
        arrayValue.append(current_sum)

    max_sum = max(arrayValue)
    min_sum = min(arrayValue)  
    print(min_sum, max_sum )

print(minMaxSum(array))