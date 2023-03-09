n=int(input("Enter number of elements"))
x=[]
max=0
for i in range(1,n+1):
    a=int(input("Enter value"))
    x.append(a)
    if max<a:
        max=a
print(max)
