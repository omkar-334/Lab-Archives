def partition(arr,low,high):
    curr,pivot=low-1,arr[high]
    for i in range(low,high):
        if arr[i]<=pivot:
            curr+=1
            arr[i],arr[curr]=arr[curr],arr[i]
    arr[curr+1], arr[high] = arr[high], arr[curr+1]
    return curr+1

def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

arr=[7,1,2,5,3,4]
size=len(arr)

quicksort(arr,0,size-1)
print(arr)
