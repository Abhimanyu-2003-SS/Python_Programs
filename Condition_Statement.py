#Smart ATM Authentication System
"""pin=1234
account_balance=10000
user_pin=int(input("Enter The Pin : "))
if user_pin == pin:
    withdraw_amount=int(input("Enter Withdrawal Amount : "))
if withdraw_amount<account_balance:
    print("Withdraw Succesful")
    remaining_balance=account_balance-withdraw_amount
    print("Remaining Balance : ",remaining_balance)
else:
    print("Insufficent Balance")

#Online Shopping Discount Calculator

purchase_amount=int(input("Enter Purchase Amount : "))
premium=bool(input("Premium Member (yes/no) : "))
discount=25*(purchase_amount/100)
total_price=purchase_amount-discount
print("Discount Applied 25%")

if premium==True:
    final_price=total_price-1000
    print("Final Bill Amount : ",final_price)
else:
    print("Final Bill Amount : ",total_price)

#University Admission Eligibility Checker

higher_secondery_percentage=float(input("Enter Higher Secondry Mark Percentage : "))
maths=float(input("Enter marks percentage of mathematics : "))
entrance=float(input("Enter Enterence Exam Score : "))

print("Pass Percentage = 70")

if higher_secondery_percentage>=70 and maths>=70 and entrance>=70:
    print("Admission Status : Eligible")
    print("Suggested course : Computer Science")
else:
    print("Admission Status : Not Eligible")

#Loan Approval System

age=int(input("Enter the age : "))
salary=int(input("Enter the salary : "))
credit_score=int(input("Enter credit score : "))
loan_status=input("Existing Loan (yes/no) : " )
if age<50 and salary>2000 and credit_score>500 and loan_status== 'no':
    print("Loan Status : Approved")
else:
    print("Loan Status : Rejected")

#Hospital Patient Priority System

age=int(input("Enter your age : "))
severity_level=input("Enter Condition (critical/severe/mild) : ")

if severity_level=='critical':
    print("Priority Category : High Priority")
elif severity_level=='severe':
    print("Priority Category : Very High Priority")
else:
    print("Priority Category : Low Priority")"""

#Employee Bonus Management System

years=int(input("Enter The Years Of Service : "))
rating=input("Enter Performent Rating : ")
attendence=int(input("Enter Attendance : "))
if attendence>70:
    if rating == 'excellent':
         print("Bonus Percentage : 20%")
         print("Bonus Amount : 10000")
    else:
        print("Bonus Percentage : 10%")
        print("Bonus Amount : 5000")





