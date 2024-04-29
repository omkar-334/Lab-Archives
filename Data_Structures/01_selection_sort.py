def selectionsort(arr,size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return f"Sorted list is {arr}"

arr=[7,1,2,5,3,4]
size=len(arr)

selectionsort(arr,size)
print(arr)
