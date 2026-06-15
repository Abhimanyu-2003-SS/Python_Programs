""""print("Arithamatic Operator")

price_per_book=500
Quantity=25
Total_price=price_per_book*Quantity
Average=Total_price/Quantity
Extra_Charge=50
Final_price=Total_price+Extra_Charge
Discount=25
Final_price-=Discount
Reminder=Final_price%Quantity
Floor_Division=Final_price//7
Squared_Value=Final_price**2

print("Price of one book : ",price_per_book)
print("Quantity Of Books : ",Quantity)
print("Total Price : ",Total_price)
print("Average Amount Of Book : ",Average)
print("Extra Charge : ",Extra_Charge)
print("Final Price : ",Final_price)
print("Discount : ",Discount)
print("Final Price After Discount : ",Final_price)
print("Reminder : ",Reminder)
print("Floor Division : ",Floor_Division)
print("Squared Value : ",Squared_Value)

print("Assignment Operator")

Score=1000
Score+=50
print(Score)
Score-=20
print(Score)
Score*=2
print(Score)

print("Logical Operator")

#And Operator

username="Abhimanyu s s"
password="1234"
entered_username=input("Enter the username : ")
entered_password=input("Enter the password : ")
if entered_username == username and entered_password == password :
    print("Login Successfull")
else:
    print("Invalid Credentials")

#Or Operator

Day=input("Enter the day : ")
if Day=="Sunday" or Day=="Saturday": 
    print("Holiday")
else:
    print("Working day")

# Not Operator

Logged_in=False
if not Logged_in:
    print("Welcome user")
else:
    print("Please login")

#Membership operator is used to check a element in a list

Movies=["Avatar","Openhimer","Spiderman"]
movie=input("Enter the movie name : ")
if movie in Movies:
    print("Movie Available")
else:
    print("Movie Not Available")

Employess=["Anand","sanal","Geetha"]
employee=input("Enter the employee name : " )
if employee not in Employess:
    print("Access denied")
else:
    print("Acess Gained")

#Identity Operator is to check if data in same memory location

a=10
b=10
c=20

print(a is b)
print(b is c)

List1=[1,2,3]
List2=[1,2,3]
List3=List1

print(List1 is List2)
print(List1 is List3)
print(List3[0] is List1[0])
print(1 is List1[0])

Language =["python","Java","C"]
selected_language=Language[0]
print(selected_language is Language[0])
print(selected_language is "python")#error
print(selected_language == "python")
print(selected_language == Language[0])"""

#Bitwise operators

a=5
b=3
print(bin(a))
print(bin(b))
print(a & b)
print(bin(a|b))
print(bin(a^b))
print(~a) #-(a+1)

#leftshift rightshift

a=5
print(a<<1)   #leftshift (a*2^1)
print(a>>1)   #rightshift (a/2^1)
