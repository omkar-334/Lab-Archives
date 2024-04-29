n=int(input("Enter number of elements"))
x=[]
for i in range(1,n+1):
    a=int(input("Enter value"))
    x.append(a)
min=10000
for i in x:
    if min>i:
        min=i
print(min)
for i in range(0,len(x)):
    if min==x[i]:
        print(i)
