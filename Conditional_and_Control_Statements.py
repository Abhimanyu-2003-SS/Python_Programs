#syntax if-else

"""if condition:
     Code to be executed
    else:
        Code to be executed"""

#if-elif-else

"""if condition:
    Code to be executed
elif condition:
    Code to be executed
else:
    Code to be executed"""

#To check wheather a number is positive or negative

"""num=int(input("Enter the number : "))
if num>0:
    print("Positive Number")
else:
    print("Negative Number")

#To check wheather a character is vowel or not

vowel_check=input("Enter a Character : ")
if vowel_check in 'aeiouAEIOU':
    print("vowel")
else:
    print("Consonent")

#To check wheather a number is even or odd

odd_even=int(input("Enter a Number : "))
if odd_even%2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

#To check wheather a person is child teenager adult or senior citizen

age=int(input("Enter the age : "))
if age<=13:
    print("Child")
elif age<=18:
    print("Teenager")
elif age<=60:
    print("Adult")
else:
    print("Senior citizen")

#To check wheather the given number is positive and even or positive and odd otherwise negative using nested if

num=int(input("Enter the number : "))
if num>0:
    if num%2==0:
        print("Number is Positive And  Even")

    else:
        print("Number is Positive And   Odd")
else:
    print("Number is Negative")

#To check wheather the number is 3 digit or not

num=int(input("Enter The Number : "))
if num>99 and num<1000:                 #or 99>num<1000
    print("The Entered Number Is 3 Digits")
else:
    print("The Entered Number Is Not 3 Digits")"""

#simple atm program

balance_amount=50000
withdraw_amount=int(input("Enter the Withdraw Amount : "))
if withdraw_amount<balance_amount:
    print("Withdrawal Successfull")
else:
    print("Insufficent Balance")
