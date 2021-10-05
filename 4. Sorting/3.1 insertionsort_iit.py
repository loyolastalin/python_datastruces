def sort(arr):
    for i in range(len(arr)):
        pos = i

        while pos > 0 and arr[pos] < arr[pos-1]:
            (arr[pos], arr[pos-1]) = (arr[pos-1], arr[pos])
            pos = pos -1
    return arr

print(sort([3,1,9,7,5]))