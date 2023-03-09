evensum=0
oddsum=0
for i in range(0,101,2):
    evensum+=i
    i=i+1
for j in range(1,100,2):
    oddsum+=j
    j=j+1
print("the sum of odd numbers till 100 is ", oddsum)
print("the sum of even numbers till 100 is ", evensum)
    
    
