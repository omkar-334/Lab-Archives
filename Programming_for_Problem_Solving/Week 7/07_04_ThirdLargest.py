n=int(input("Enter number of elements"))
x=[]
for i in range(0,n):
    a=int(input("Enter value"))
    x.append(a)
x.sort()
print(x[-3])
