x=input("Enter character")
y=ord(x)
if(y>=48 and y<=57):
    print("Character is a number")
elif(y>=65 and y<=90):
    print("Character is an alphabet")
elif(y>=97 and y<=122):
    print("Character is an alphabet")
elif(y==32):
    print("Character is a space")
