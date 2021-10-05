def sum(m):
    if m==0:
        return 0
    
    return m + sum(m-1)

print(sum(9))