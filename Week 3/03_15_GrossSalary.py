DA=int(input("Enter DA value"))
HRA=int(input("Enter HRA value"))
Basic=int(input("Enter Basic Pay value"))
PF= Basic/10
Gross=Basic+DA+HRA-PF
print("The Gross salary is ", Gross)
