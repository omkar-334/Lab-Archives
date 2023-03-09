n=int(input("Enter number of elements"))
x=[]
y=[]
for i in range(0,n):
    a=int(input("Enter value"))
    x.append(a)
for i in x:
    c=x.count(i)
    y.append(c)
print("   List   - ", x)
print("Frequency - ", y)
    
