x=int(input("Enter number"))
y=[]
z=[]
s=0
while(x>0):
    a=x%10
    y.append(a)
    z.append(a)
    x=x//10
    s=s+1
y.reverse()
for i in range(0,s):
    if(z[i]==y[i]):
        s=s-1
if(s==0):
    print("palindrome")
else:
    print("not a palindrome")
    
    
