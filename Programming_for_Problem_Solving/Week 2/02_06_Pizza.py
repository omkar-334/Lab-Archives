'''
6. Ask how many slices of pizza the user started with and ask how many slices they have eaten.
Work out how many slices they have left and display the answer in a user-friendly format
'''


startNum=int(input("How may pices of pizza have you started with?"))
endNum=int(input("How many pieces of pizza have you eaten?"))
slicesLeft=startNum-endNum
print("You have ", slicesLeft, " slices remaining.")
