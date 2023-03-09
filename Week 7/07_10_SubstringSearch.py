a=str(input("Enter word"))
b=str(input("Enter substring"))
s=0
for i in a:
    if b in a:
        s=s+1
print(s)


