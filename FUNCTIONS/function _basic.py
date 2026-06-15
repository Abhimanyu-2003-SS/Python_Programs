# Syntax
"""
def function_name(parameters):
    code to be Executed
"""
"""
def greeting(username,age):
    print(f"Welcome {username} you are {age} Years old")

username=input("Enter your name : ")
age=int(input("Enter Age : "))
greeting(username,age)

def addition(num1,num2):
    return num1+num2

num1=int(input("Enter First Number : "))
num2 = int (input("Enter second number : "))

result=addition(num1,num2)
print("Result : ",result)


def multiply():
    num1=int(input("Enter First Number : "))
    num2 = int (input("Enter second number : "))
    return num1*num2

result=multiply()

print(result)

"""

"""
    Functions
    
    Types : User-Defined , Pre-Defined
    User_Defined -2 Types : With Args ,Without Args

            With Arguments -3 Types : Positional,Keyword,Default  Args



#Positional Args

def Book_Ticket(movie_name,customer_name,seats,ticket_price):
    total=seats*ticket_price
    return f"{customer_name} booked {seats} tickets for {movie_name} : Total Amount : {total}"

print(Book_Ticket("Avatar","Abhi",5,200))



#Keyword Arguments

def customer_details(name,age,city):
    print(f"Customer Name : {name} ")
    print(f"Customer Age : {age}")
    print(f"Customer City : {city}")

customer_details(name="Abhi",city="Kollam",age=23)


#Default Arguments

def booking_status(customer_name="Abhi",status="Confirmed",screen="Screen 1",):
    print(f"{customer_name} 's booking status : {status} ")
    print(f"Screen allocated : {screen}")

booking_status()
booking_status("Abhi","Pending","Screen 3")
    


#Multiple Arguments

def calculate_bill(ticket_prices):
    print(f"Ticket Prices : {ticket_prices}")
    print(f"Total Bill : {sum(ticket_prices)}")

calculate_bill([10,20,30,40,50])

    # we can give arguments as list while calling the function

def calculate_bill(*ticket_prices):
    print(f"Ticket Prices : {ticket_prices}")
    print(f"Total Bill : {sum(ticket_prices)}")

calculate_bill(10,20,30,40,50)
    # we can use * to store multiple values in a single parameter


# Multiple keyword Arguments

def passenger_info(**details):
    print(f"Passenger Information :  ")
    for key,value in details.items():
       print(f"{key} : {value}")
passenger_info(name="Abhi",seats=23,destination="kollam",payment_status="pending")

#Build_in Functions

print(len("hello world"))
print(sum([10,20]))
print(max(10,20,60,90,70))
print(min(-1,30,-2,0,10))
print(sorted([20,-2,0,-2,50]))
print(sorted([20,-2,0,-2,50],reverse=True))


languages=["Malayalam","Hindi","English","Tamil"] #Sorted in Alphabetic Order
print(sorted(languages))
print(sorted(languages,reverse=True))
print(sorted(languages,key=len)) #Based on length
print(sorted(languages,key=len,reverse=True))

#Enumerate(),How it works in a loop

#LEGB rule = Local Enclosing Global Buildin

def student_details():
    name="Abhi" #Local Variable
    print("Student Name : ",name)
student_details()


collage_name="CEP" #Global Variable
def display():
    print("College Name : ",collage_name)

display()


def department():
    department_name="Computer Science" #Enclosed Variable
    def student():
        print("Department Name : ",department_name)
    student()
department()


#Billing System

tax=50   #Global Variable
def shopping():
    discount=100 #Enclosing Variable
    def billing():
        amount=1000 #Local Variable
        total_amount=(amount-discount)+tax
        print("Total Bill : ",total_amount)
    billing()

shopping()


#Factorial using Recurssion

def factorial (num):
    if num ==1 :
        return 1
    else:
        return num*factorial(num-1)
    
n=int(input("Enter The Number : "))
print(factorial(n))

#Direct Way

num=int(input("Enter The Number : "))

def Factoril():
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    print(f"Factorial Of {num} : {fact}")
Factoril()
"""

def add(a,b):
    return a+b

print(add(1,2))

#lambda () Syntax

"""
    lambda arguments:expression

"""

add=lambda a,b:a+b
print(add(10,20))














