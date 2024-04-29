'''
11. Task the user to enter a number over 100 and then enter a number under 10 and tell them
how many times the smaller number goes into the larger number in a user-friendly format.
'''


larger=int(input("Enter a number above 100"))
smaller=int(input("Enter a number below 10"))
answer=larger//smaller
print(smaller, " goes into ", larger, answer, " times")
