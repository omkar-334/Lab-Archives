
y=str(input("Enter temperature ")).split()

if y[1]=="c":
    print("The temperature in Fahrenheit is  ", (1.8*int(y[0])+32))
else :
    print("The temperature in Celcius is  ", (int(y[0])-32)/1.8)
