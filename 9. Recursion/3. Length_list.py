def length(arr):
    if arr == []:
        return 0
    return 1 + length(arr[1:])

print(length([1,2,3,4]))