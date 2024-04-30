def findMaxMin(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    mid = (low + high) // 2
    
    maxLeft, minLeft = findMaxMin(arr, low, mid)
    maxRight, minRight = findMaxMin(arr, mid + 1, high)
    
    max_val = max(maxLeft, maxRight)
    min_val = min(minLeft, minRight)
    
    return max_val, min_val

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))

max_val, min_val = findMaxMin(arr, 0, n - 1)

print(f"Maximum element: {max_val}")
print(f"Minimum element: {min_val}")