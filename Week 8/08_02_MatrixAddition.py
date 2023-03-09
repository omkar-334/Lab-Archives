rowsA=int(input("Enter the number of rows of A"))
colsA=int(input("Enter the number of cols of A"))
rowsB=int(input("Enter the number of rows of B"))
colsB=int(input("Enter the number of cols of B"))


a=[]
b=[]
sum=[]
a=[[0 for x in range(colsA)] for y in range(rowsA)]
b=[[0 for x in range(colsB)] for y in range(rowsB)]
sum=[[0 for x in range(colsB)] for y in range(rowsB)]
for i in range(rowsA):
    for j in range(colsA):
        a[i][j]=int(input("Enter A element at "+str(i)+"*"+str(j)+" - "))
for i in range(rowsB):
    for j in range(colsB):
        b[i][j]=int(input("Enter B element at "+str(i)+"*"+str(j)+" - "))
for i in range(rowsB):
    for j in range(colsB):
        sum[i][j]=a[i][j]+b[i][j]
for i in sum:
    print(i)
