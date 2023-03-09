z={0:"Zero",
   1:"One",
   2:"Two",
   3:"Three",
   4:"Four",
   5:"Five",
   6:"Six",
   7:"Seven",
   8:"Eight",
   9:"Nine"}
x=int(input("Enter number"))
s=0
y=[]
while(x>0):
    a=x%10
    y.append(a)
    x=x//10
    s=s+1
y.reverse()
for i in range(1,s+1):
    c=y[i-1]
    print(z[c],end=" ")