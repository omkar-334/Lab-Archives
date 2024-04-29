import bisect

def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return f"Element found at index {i}"
    else:
        return "Element not found"

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

print(binary_search(arr, x))