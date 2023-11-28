
arr=[2,1,6,5,3,4]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        print(left,right)
        return quicksort(left) + [pivot] + quicksort(right)

print(f"Sorted array - {quicksort(arr)}")