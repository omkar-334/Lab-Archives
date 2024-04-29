type=input("Enter type of food - veg / nonveg - ")
x=0

if(type=="veg"):
	x=int(input("Enter number of veg combos - "))
	price=x*120
elif(type=="nonveg"):
	x=int(input("Enter number of nonveg combos - "))
	price=x*150
else:
	print("Bill amount = -1")


if(x<=1):
	print("")
else:
	distance=int(input("Enter distance(in km) from restaurant - "))
	if(distance<=0):
		print("Bill amount = -1")
	elif(distance<=3):
		print("Bill amount = ", price)
	elif(distance<=6):
		charge=(distance-3)*3
		print("Bill amount is ", price+charge)
	else:
		charge=9+(distance-6)*6
		print("Bill amount is ", price+charge)

	
	
	