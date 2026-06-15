"""for i in range (10):
    print("*")
    if i==3:
        break"""

#output
"""
*
*
*
*

"""

#The output of the above code executes only 4 times exactly
#After when the condition in if becomes true then we exit from the loop
#This is how break statement works

#lets do continue statement 

for i in range (1,10):
    
    if i==3:
        continue

    print(i)    

#output

"""
1
2
4
5
6
7
8
9

"""

#In continue statement a when a specific condition becomes true then the iteration is skipped
#unlike break the rest of the iteration is completed
#In the above output 3 is the number missing


#lets do pass statement

num=3
if num==3:
    pass
else:
    print("Not the right number")


#Here we use pass as a placeholder in which we can write the code later
#In the if statement we use pass instad of a code so that there will be no error 
#and can fill the place later 