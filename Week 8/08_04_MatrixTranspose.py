rowsA=int(input("Enter the number of rows of A"))
colsA=int(input("Enter the number of cols of A"))
a=[]
b=[]
a=[[0 for x in range(colsA)] for y in range(rowsA)]
b=[[0 for x in range(colsA)] for y in range(rowsA)]
for i in range(rowsA):
    for j in range(colsA):
        a[i][j]=int(input("Enter A element at "+str(i)+"*"+str(j)+" - "))
        b[j][i]=a[i][j]
for i in a:
    print(i)
print("\n")
for i in b:
    print(i)
