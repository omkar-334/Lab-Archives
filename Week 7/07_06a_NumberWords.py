b={"0":"Zero",
   "1":"One",
   "2":"Two",
   "3":"Three",
   "4":"Four",
   "5":"Five",
   "6":"Six",
   "7":"Seven",
   "8":"Eight",
   "9":"Nine"}
n=int(input("Enter number"))
s=0
xt=()
z=()
while(n>0):
    a=n%10
    z=(a,)
    n=n//10
    s=s+1
    xt=xt+z
nt=xt[::-1]
print(nt)

for i in range(1,s+1):
    c=nt[i-1]
    print(b[str(c)],end=" ")
