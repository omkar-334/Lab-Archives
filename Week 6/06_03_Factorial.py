n=int(input("Enter n value"))
product=1
if(n==0):
    print("0 factorial is 1")
else:
    for i in range(1,n+1):
        product=product*i
        i=i+1
    print(n, "factorial is ", product)
