x=int(input("Enter year"))
if(x%100==0):
    if(x%400==0):
        print("The year is a leap  year")
    else:
        print("The year is not a leap year")
else:
    if(x%4==0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
