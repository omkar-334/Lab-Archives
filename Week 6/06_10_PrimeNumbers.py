n=int(input("Enter n value"))
j=0
for i in range(2,n):
    if(n%i!=0):
        j=j+1
if(j==0):
    print("n is prime")
else:
    print("n is not prime")



