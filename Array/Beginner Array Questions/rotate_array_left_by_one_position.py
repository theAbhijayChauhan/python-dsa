def rotate_array(arr):
    size = len(arr)
    temp = arr[0]
    for i in range(size-1):
        arr[i] = arr[i+1]

    arr[size-1] = temp
    print(arr)


arr = [1,2,3,4,5,6]
rotate_array(arr)