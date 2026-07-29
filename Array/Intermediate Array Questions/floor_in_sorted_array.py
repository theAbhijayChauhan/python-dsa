

def floor_element(arr, target):
    low = 0
    high = len(arr)-1
    
    answer = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            answer = arr[mid]
            low = mid +1
        else:
            high = mid -1
    return answer

arr = [2, 5, 8, 12, 16]
print(floor_element(arr, 10))