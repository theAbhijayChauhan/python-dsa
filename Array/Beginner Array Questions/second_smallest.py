def second_smallest(arr):
    size = len(arr)
    smallest = float('inf')
    s_smallest = float('inf')
    
    for num in arr:
        if num < smallest:
            s_smallest = smallest
            smallest = num
        elif num < s_smallest and num != smallest:
            s_smallest = num
    
    print(s_smallest)



arr = [5,0,3,2,1,9,8]
second_smallest(arr)