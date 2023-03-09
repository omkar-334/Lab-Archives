x=int(input("Enter number"))
y=x
sum=0
while x>0:
    a=x%10
    sum+=a**3
    x//=10
if sum==y:
    print("Armstrong Number")
else:
    print("Not an armstrong number")
