def binary_search(arr,low,high,a):
    mid=(low+high)//2

    if high>=low:
        if arr[mid]==a:
            return f"Element found at index {mid}"
        elif arr[mid]>a:
            return binary_search(arr,low,mid-1,a)
        else:
            return binary_search(l,mid+1,high,a)
    else:
        return "Element not found"

l=list(range(1,100,2))
a=47
print(binary_search(l,0,len(l)-1,a))

