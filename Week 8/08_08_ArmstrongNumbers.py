a=[x for x in range(1,400)]
finout=[]
print(a)
for i in a:
    pr=0
    xl=[*str(i)]
    for j in xl:
        pr+=int(j)**3
    if str(pr)==str(i):
        finout.append(i)
print(finout)
