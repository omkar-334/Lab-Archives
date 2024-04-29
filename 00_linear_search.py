def linear_search(list,a):
    for i,v in enumerate(list):
        if v==a:
            return f"Element found at index {i}"
    return "Element not found"
list=[1,2,3,4,5,6]
a=2
print(linear_search(list,a))