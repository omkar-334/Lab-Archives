n=int(input("enter number of elements in list"))
list1=[]
c=0
for i in range(0,n):
    x=int(input("Enter the element"))
    list1.append(x)
y=int(input("enter element to be searched"))
for i in list1:
    if i!=y:
        c+=1
if c==n:
    print("element not found")
else:
    print("element found")
