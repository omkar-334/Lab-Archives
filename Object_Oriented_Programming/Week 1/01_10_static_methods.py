class choice:
    def __init__(self,var,check):
        self.var=var
        self.check=check
    def display(self):
        print(self.var-self.check)
    @staticmethod
    #Static method doesn't take self argument
    def validate(var,check):
        if var==check:
            print("Validated")
        else:
            print("Try again")

var=int(input())
check=3409
object=choice(var,check)
object.display()
object.validate(var,check)


#INPUT - 123
#OUTPUT -
'''
123
-3286
Try again
'''