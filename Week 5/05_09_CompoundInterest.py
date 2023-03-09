import math
p=int(input("Enter principle amount"))
t=int(input("Enter time period in years"))
n=int(input("Enter compound frequency per year"))
r=float(input("Enter interest rate"))
A=p*(pow((1+(r/n)),(n*t)))
print("The compound interest is ", A-float(p))


