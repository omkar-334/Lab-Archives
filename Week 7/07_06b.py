t=('zero','one','two','three','four','five','six','seven','eight','nine')
x=int(input('enter a number :'))
a=[]
r=0
string=""
while(x>0):
    r=x%10
    r=t[r]
    x=x//10
    a.insert(0,r)
for i in a:
    string=string +" "+i
print(string)
