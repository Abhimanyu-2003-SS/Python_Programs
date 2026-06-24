# Prime Number or not
"""
n=int(input("Enter The Number : "))

if n<=1:
    print("Not Prime")
else:
    is_prime=True

for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
    
if is_prime==True:   
    print("The Number is Prime")
else:
    print("Number is Not Prime")

# Try using count and floor division



#fibonacci series

a=0
b=1
num=int(input("Enter The Number Of Terms : "))

for i in range(1,num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c



#Palendrome or not

num=int(input("Enter the Number to Check : "))
rem=0
rev=0
check=num
while num>0:

    rem=num%10
    rev=(rev*10)+rem
    num=num//10

if rev==check:
    print("Number is Palendrome")
else:
    print("Number is Not Palendrome : ")


#Count the number of digit
count=0
num=int(input("Enter The Number : "))
temp=abs(num)
if temp==0:
    count=+1
else:
    while temp>0:
        temp=temp//10
        count+=1

print(f"Number of Digits : {count}")
  

#Sum of digits

num=int(input("Enter The Digit : "))
temp=abs(num) 
sum=0 

while temp>0:

    rem=temp%10
    sum+=rem
    temp//=10

print(sum)



#Product of Digits

num=int(input("Enter The Digit : "))
temp=abs(num) 
sum=0 

while temp>0:

    rem=temp%10
    sum*=rem
    temp//=10

print(sum)


balance=50000
correct_pin=1234
attempt=0
while attempt<3:
    pin=int(input("Enter The Pin : "))
    if pin==correct_pin:
        print("Login Successfull !!!")
        while True:
            print("\n1. Balance Check")
            print("2.Withdraw")
            print("3.Deposite")
            print("4.Exit")
            choice=int(input("Enter Your Choice : "))
            if choice==1:
                print("Balance : ",balance)
            elif choice == 2:
                amount=int(input("Enter The withdrawal amount : "))
                if amount <= balance:
                    balance-=amount
                else:
                    print("Insufficent Balannce")
            elif choice ==3 :
                amount= int(input("Enter the amount to be deposited : "))
                balance+=amount
                print("Amount deposited successfully")
            elif choice == 4:
                print("ThankYou")
                break
            else:
                print("Invalid Choice")
        break 
    else:
        attempt+=1
        print("Incorrect Pin")

else:
    print("Account Disabled !!!!")



#Seat Booking

available_seat=55
while available_seat>0:
    print("Available Seat : ",available_seat)
    seat=int(input("Number of Seats : "))
    abs(seat)
    if seat <= available_seat:
        available_seat-=seat
        print("Seat Booked Succesfully : ")
        print("Remening Seat : ",available_seat)
    else:
        print("Seat Not Available")
    choice=int(input("1.Book again \n 2: Exit\n"))
    if choice==1:
        continue
    else:
        break
print("Booking Closed !!!!")
        
   
#Pattern Print
for i in range(1,21):
    if i%3==0 and i%5==0:
        print("fizbuzz")
    elif i %3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
    

#Find the largest and smallest number in a list

num=[]

n=int(input("Enter the Number of Elements in a list : "))
for i in range(n):
    element=int(input(f"Enter {i}th Element : "))
    num.append(element)
largest =num[0]
smallest=num[0]
for i in num:
    if i>largest:
        largest=i
    if i<smallest:
    
        smallest=i

        
print("Smallest Number : ",smallest)
print("Largest Number : ",largest)

#Seperate positive and negative number from a list


   
numbers=tuple(map(int,input("Enter The Numbers to be Inserted : ").split()))
element=int(input("Enter the Elements to be Counted : "))
count=0
for item in numbers:
    if item==element:
        count+=1

print(f"Tuple Elements are : {numbers}")
print(f"Occurence of {element} in tuple is : {count}")

numbers=tuple(map(int,input("Enter The Numbers to be Inserted : ").split()))
target=int(input("Enter the Target Sum : "))
for i in  range(len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print((numbers[i],numbers[j]))

 """

#Reverse a dictionary
data={
    "a":1,
    "b":2,
    "c":3

}

reversed_data={}
keys=list(data.keys())
for key in keys[::-1]:
    reversed_data[key]=data[key]
print(reversed_data)








