Customer_Name = input("Enter Customer Name : ")
Atm_Card_Num = int(input("Enter Your ATM Card Number : "))
Pin_Number = int(input("Enter The Pin Number : "))
Account_Type = input("Enter The Account Type : ")
Available_Balance = float(input("Enter Available Balance : "))
Withdraw_Amount = float(input("Enter The Withdraw Amount : "))

Account=["Savings","Current"]
if Account_Type in Account:
    print("Account Valid : True")
else:
    print("Account Valid : False")

Stored_pin = 1234

if Stored_pin==Pin_Number:
    print("Pin Verified : True")

if Withdraw_Amount <= Available_Balance and Available_Balance > 0:
    print("Sufficent Balance : True")

if Stored_pin==Pin_Number and Account_Type in Account and  Withdraw_Amount<=Available_Balance and Available_Balance > 0:
    print("Transaction successfull...")
else:
    print("Transaction error....")

account1=Account_Type
account2=Account_Type

Remaining_Balance = Available_Balance - Withdraw_Amount

print("Remaining Balance : ",Remaining_Balance)

print("Data Type Of Customer Name : ",type(Customer_Name))
print("Data Type Of Pin : ",type(Pin_Number))
print("Data Type of Withdraw Amount : ",type(Withdraw_Amount))
print("Data Type Of Account Type : ",type(Account_Type))


print("is Available Balance is float : ",isinstance(Available_Balance,float))
print("is Withdraw Amount is float : ",isinstance(Withdraw_Amount,float))
print("is Customer Name is float : ",isinstance(Customer_Name,str))

print("Id of Available Balance : ",id(Available_Balance))
print("Id of Remaining Balance : ",id(Remaining_Balance))
print("Id Of Account Type : ",id(Account_Type))

print("Account1 is Account2",account1 is account2)
print("Account1 isnot Account2 : ",account1 is not account2)



    
