x=str(input("Enter string"))

y=list(x.lower())
z=['a','e','i','o','u']
a=0
for i in y:
   if(i in z):
       a=a+1
print(a)
