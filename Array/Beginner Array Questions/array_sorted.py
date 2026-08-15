def array_sorted(arr):
    size = len(arr)
    is_sorted = True
    for i in range(size-1):
        if arr[i] > arr[i+1]:
            is_sorted = False
    if is_sorted == False:
        print("array is not sorted !")
    else:
        print("array is sorted !")
            


arr = [0,1,2,3,4,5,6]
array_sorted(arr)