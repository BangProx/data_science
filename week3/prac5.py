def sum_func(arr):
    total = 0
    for i in range(0,len(arr)):
        total += arr[i]
    return total

arrlist = [1,2,3,4,5]

print(sum_func(arrlist))