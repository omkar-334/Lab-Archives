x=str(input("Enter word"))
z=[*x]
y=[]
s=0
print(z)
for i in z:
    y.append(i)
    s=s+1
y.reverse()
for i in range(0,s):
    if(z[i]==y[i]):
        s=s-1
if(s==0):
    print("palindrome")
else:
    print("not a palindrome")
    
    
