n=int(input("Enter n value"))
#b=[*str(n)]
b=[]
while n>0:
    a=n%10
    b.append(a)
    n//=10
b.sort()
print(b[-1])
