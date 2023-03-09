n=int(input("enter number of elements in list"))
l=[]
c=0
for i in range(0,n):
    x=int(input("Enter the element"))
    l.append(x)
y=int(input("enter element to be searched"))
ind=l.copy()
print(l)
l.sort()

while len(l)>1:
    if len(l)==0:
        mid=len(l)//2
    else:
        mid=(len(l)+1)//2
       
    if l[mid]<=y:
        l=l[mid:]
    else:
        l=l[:mid]
    
    print(l)
for f in range(0,len(ind)):
    if ind[f]==l[0]:
        fin=f
if (l[0])==y:
    print('element found at index', fin)
else:
    print('element not found')
