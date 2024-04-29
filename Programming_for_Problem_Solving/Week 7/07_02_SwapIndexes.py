n=int(input("Enter number of elements - "))
x=[]
for i in range(0,n):
    a=int(input("Enter value - "))
    x.append(a)
j=int(input("Enter swap index 1 - "))
k=int(input("Enter swap index 2 - "))
x[j],x[k]=x[k],x[j]
print(x)

