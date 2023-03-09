n=int(input("Enter number of elements"))
x=[]
s=0
for i in range(0,n):
    a=int(input("Enter value"))
    x.append(a)
    s=s+a
print(x)
print("The sum of elements is", s)
