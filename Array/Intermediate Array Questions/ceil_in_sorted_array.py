# Problem : The ceil of a number is the smallest element greater than or equal to the target.

def ceil_element(arr, target):
    low = 0
    high = len(arr) -1
    answer = -1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] >= target:
            answer = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return answer

arr = [2, 5, 8, 12, 16]
print(ceil_element(arr, 10))