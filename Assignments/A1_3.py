import sys
account_number=int(input("Enter Account number"))
if(account_number//1000==1):
        account_balance=int(input("Enter Account Balance"))
else:
        sys.exit("Invalid account number")

if(account_balance>=100000):
        salary=int(input("Enter Salary"))
else:
        sys.exit("Insufficient balance in account")

loan_type=str(input("Enter type of loan"))
loan_amount_expected=int(input("Enter expected loan amount"))
customer_emi_expected=int(input("Enter expected number of emis"))

def output():
        print("\n Account number - ", account_number)
        print("Eligible loan amount - ", loan)
        print("Requested loan amount - ", loan_amount_expected)
        print("Eligible number of emis - ", emi)
        print("Requested number of emis - ", customer_emi_expected)

def detail():
        
        
        if(loan_amount_expected>loan):
                sys.exit("Invalid loan amount")
        else:
                if(customer_emi_expected>emi):
                        sys.exit("Invalid number of emis")
                else:
                        if(salary<=loan):
                                output()


if(loan_type=="car" or "Car"):
        loan=5000000
        emi=36
        money=25000
elif(loan_type=="house" or "House"):
        loan=6000000
        emi=60
        money=50000
elif(loan_type=="business" or "Business"):
        loan=7500000
        emi=84
        money=75000
else:
        sys.exit("Invalid loan type")

detail()





                
