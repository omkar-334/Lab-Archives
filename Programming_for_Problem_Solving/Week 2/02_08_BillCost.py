'''
8. Ask for the total price of the bill,then ask how many diners there are.
Divide the total bill by the number of diners.
show how much each person must pay.
'''


bill=int(input("What is the total cost of the bills?"))
people=int(input("How many people are there?"))
each=bill/people
print("Each person should pay $", each)
