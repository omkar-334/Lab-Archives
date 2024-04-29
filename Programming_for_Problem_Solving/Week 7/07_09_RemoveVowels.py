a=str(input("Enter word"))
x=[*a]
y=['a','e','i','o','u']
for i in x:
    for j in y:
        if(i==j):
            x.remove(i)
b = ''.join(map(str, x))
print(b)
