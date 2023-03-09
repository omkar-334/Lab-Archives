n=int(input("enter number of elements in list"))
list1=[]
x=int(input("Enter the element"))
list1.append(x)
y=int(input("Enter the element"))
if x<y:
    list1.append(y)
else:
    list1.insert(0,y)
for i in range(2,n):
    x=int(input("Enter the element"))
    for j in range(1,len(list1)):
        if list1[j-1]<x:
            if list1[j]>=x:
                list1.insert(j,x)
print(list1)
