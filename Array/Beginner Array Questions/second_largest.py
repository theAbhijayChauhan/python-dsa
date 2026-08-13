def largest_element(arr):
    size = len(arr)
    largest = arr[0]
    second_largest = arr[0]
    for i in range(size-1):
        if arr[i] > largest:
            second_largest = largest  # Old largest drops to second place
            largest = arr[i]          # Update to new largest
        
        # 2. If a number is smaller than largest, but bigger than second largest
        # OR if second_largest hasn't changed from the initial arr[0] yet
        elif arr[i] > second_largest or second_largest == largest:
            if arr[i] != largest:     # Skip duplicate largest numbers
                second_largest = arr[i]
    
    print(second_largest)
        
    
                

arr = [3, 5, 1, 7, 7, 2]
largest_element(arr)