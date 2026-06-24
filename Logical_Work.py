#Electricity bill calculator

units=int(input("Enter The Units Consumed : "))
if units <100:
    total_bill=units*5
elif units < 200:
    slab=units-100
    total_bill=(100*5)+(slab*5)

else:
    slab=units-200
    total_bill=(100*5)+(100*7)+(slab*10)

print ("Total Bill : ",total_bill)
    
#Menu Driven Calculator

num1=int(input("Enter The First Number : "))
num2=int(input("Enter The Second Number : "))
while True:
    print("1.Addition \n2.Substraction\n3.Multiplication\n4.Division")
    choice=int(input("Enter Your Choice : "))
    if choice == 1:
        print(f"Result : {num1+num2}")
    elif choice == 2:
        print(f"Result : {num1-num2}")
    elif choice == 3:
        print(f"Result : {num1*num2}")
    elif choice == 4:
        print(f"Result : {num1//num2}")
    else:
        print("Invalid Input !!!")
    
    temp=input("Do You Want to Continue (yes/no)").lower()
    if temp=="yes":
        continue
    else:
        break


#Student Grade System

grade=[]
total=0
for i in range (0,5):
    grade.append(int(input(f"Enter Mark of {i+1}th Subject : ")))
    total+=grade[i]

average=total/5
print("Total Mark : ",total)
print("Average Mark : ",average)
if total>400:
    print("Distinction")

elif total>300:
    print("First Class")

else:

    print("Second Class")

  #Voting Eligibility Checker

n=int(input("Enter the number of peoples to be checkes : "))
for i in range (5):
    name=input("Enter Your Name : ")
    age=int(input("Enter Your Age : "))
    if age>=18:
        print(f"{name} is Eligible for Voting")
    else:
        print(f"{name} is  Not Eligible for Voting")

#Number Guessing Game

secret_number=5

while True:
    num=int(input("Guess a Number Below 10 : "))
    if num == secret_number:
        print("You Have Gussed the Correct Number : ")
        break
    elif num>secret_number:
        print("Entered Number is too high")

    else:
        print("Entered Number is too low")
    print("Guess The Number Again  ")

#Student Attendence Status Checker

limit= int(input("Enter The Number of Students : "))
for i in range(1,limit):
    if i%3 == 0 and i%5 ==0 :
        print("Attendence Warning")

    elif i%3==0:
        print("Low Attendence")
    elif i%5==0:
        print("Eligible for Next Exam ")
    else:
        print("Roll Number : ",i)

#Traffic Signal Simulator

limit= int(input("Enter The Number of Seconds : "))
for i in range(1,limit):
    if i%3 == 0 and i%5 ==0 :
        print("YELLOW")

    elif i%3==0:
        print("RED")
    elif i%5==0:
        print("GREEN")
    else:
        print("Second Number : ",i)

#Online Order Proccesing System
    
limit1= int(input("Enter Starting Order id : "))
limit2= int(input("Enter Ending Order id : "))
for i in range(limit1,limit2):
    if i%3 == 0 and i%5 ==0 :
        print("Premium Customer Offer")

    elif i%3==0:
        print("Express Delivery")
    elif i%5==0:
        print("Discount Applied")
    else:
        print("Order ID : ",i)

#Library Book Categorization

limit= int(input("Enter Ending Order id : "))
for i in range(1,limit):
    if i%3 == 0 and i%5 ==0 :
        print("Reference Book")

    elif i%3==0:
        print("Science Book")
    elif i%5==0:
        print("Literature Book")
    else:
        print("General Book")

#Electricity Bill Alert System

limit1= int(input("Enter Starting Range : "))
limit2= int(input("Enter Ending Range : "))
for i in range(limit1,limit2):
    if i%3 == 0 and i%5 ==0 :
        print("Service Suspension Warning")

    elif i%3==0:
        print("High Usage Alert")
    elif i%5==0:
        print("Payment Due")
    else:
        print("Customer ID : ",i)