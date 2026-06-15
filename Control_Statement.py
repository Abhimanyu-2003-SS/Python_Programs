#syntax for loop

"""
for variable in sequence:
    code to be executed



word=input("Enter the Word : ")
for letter in word :
    print(letter,end=" ")
    

for element in [1,2,3,4,5]:
    print(element)

#using range function


for variable in range(start,stop,skip):
    code to be executed



for element in range(11):
    print(element)

for element in range(5,16):
    print(element)
for element in range(5,26,5):
    print(element)

for element in range(1,10,-1): # doesn't work
    print(element)

#To reverse the iteration

for element in range(17,3,-3): 
    print(element)

#multiplication table of a number

num=int(input("Enter a Number : "))
for i in range(1,11):
   # print(i,"*",num,"=",num*i)
    print(f"{i} * {num} = {num*i}") #Printing using Formating string
"""

# syntax While loop

"""
while condition :

    code to be executed




value=1

while value<=10:
    print(value)
    value+=1
 


i=0
iteration =int(input("Enter the number of iterations : "))
sum=0
while i<=iteration:
    sum+=i
    i+=1

print(sum)

#Reverse of a number 

num=int(input("Enter a Number : "))
rev=0
while num > 0 :
    rem=num % 10
    rev= (rev*10)+rem
    num//=10

print(rev)

# Getting last digit 
# Remove the last digit
# Reverse code
# Print rev 

rem=0
count=0
for i in range(1,100):
    num=i
    while num > 0:
        rem=num%10
        if rem == 9:
            count+=1
        num= num // 10

print("Total representation of 9 : ",count)

"""
n=int(input("Enter a Number : "))
for i in range(n+1):
    print(i)


