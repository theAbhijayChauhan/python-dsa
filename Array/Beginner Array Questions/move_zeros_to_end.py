def move_zeros(arr):
    size = len(arr)
    j = 0
    for i in range(size):
        if arr[i] !=0:
            arr[j],arr[i]=arr[i],arr[j]
            
            j = j+1
    print(arr)



arr = [1,0,2,3,0,7,4,9,8,4,0,4]
move_zeros(arr)
