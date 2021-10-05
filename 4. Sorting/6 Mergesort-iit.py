def merge(first, second):
    (newSeq, m, n) = ([], len(first), len(second) )
    (i, j) = (0,0)

    while m+n > i+j:
        if m == i:
            newSeq.append(second[j])
            j+=1
        elif n == j:
            newSeq.append(first[i])
            i+=1
        
        elif first[i] <= second[j]:
            newSeq.append(first[i])
            i+=1
        
        elif second[j] < first[i]:
            newSeq.append(second[j])
            j+=1
    return newSeq  
def mergeSort(seq, stat, end):
    if end -stat <=1:
        return seq[stat:end]
    if end -stat > 1:
        mid = (end + stat) // 2
        L = mergeSort(seq, stat, mid)
        R = mergeSort(seq, mid, end)
        return merge(L, R)
l = [1,4,3,8,6]
print(mergeSort(l,0, len(l)))
# print(merge([1,5,6], [9,7,11]))