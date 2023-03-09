n=int(input("Enter n value"))
b=[]
j=0
while n>0:
    a=n%10
    b.append(a)
    n//=10
x=len(b)
for i in range(1,x):
    if(b[i-1]==b[x-1]):
        j=j+1
if(j!=0):
    print("n is a palindrome")
else:
    if(x==1):
        print("n is a palindrome")
    else:
        print("n is not a palindrome")
