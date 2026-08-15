def remove_duplicates(arr):
    size = len(arr)
    i = 0
    for j in range(0, size-1):
        if arr[j] != arr[j+1]:
            i +=1

    return i+1


arr = [1,1,2,2,2,3,3,3,3]
print(remove_duplicates(arr))