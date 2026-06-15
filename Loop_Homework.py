#Employee Salary Report Generator
sum=0
for i in range (1,6):
    salary=int(input(f"Enter Salary Of Employee {i} : " ))
    sum+=salary
print("Total Salary Expenditure : ",sum)

#Student Attendence Counter
present=0
absent=0
for i in range(1,11):
    attendence=input(f"Student {i} Attendence : ")
    if attendence == 'P':
        present+=1
    else:
        absent+=1

print("Total Present Student : ",present)
print("Total Absent Student : ",absent)

#Supermarket Billing System
totalprice=0
for i in range(1,6):
    price=int(input(f"Item {i} Price : "))
    totalprice+=price
print("Total Bill Amount : ",totalprice)

#Cricket Score Analyzer
totalruns=0
for i in range(1,7):
    runs=int(input(f"Ball {i} Runs : "))
    totalruns+=runs
print("Total Runs Scored : ",totalruns)

#Library Book Collection Counter
totalnum=0
for i in range(1,8):
    num=int(input(f"Section {i} Books : "))
    totalnum+=num
print("Total Books in Library : ",totalnum)


#Online Exam Marks Calculator
totalmarks=0
for i in range(1,6):
    marks=int(input(f"Subject {i} Marks : "))
    totalmarks+=marks
print("Total Marks : ",totalmarks)
print("Average Marks : ",totalmarks/5)

#Daily Temperature Monitor

Biggest=int(input("Day 1 Temperature : "))
for i in range (2,8):
    temp=int(input(f"Day {i} Temperature : "))
    if temp>Biggest:
        Biggest=temp

print("Highest Temperature : ",Biggest)

#Mobile Recharge Collection System

totalcollection=0
for i in range(1,11):
    collection=int(input(f"Customer {i} Recharge : "))
    totalcollection+=collection
print("Total Marks : ",totalcollection)


#Water Consumption Tracker

totalwater_consumption=0
for i in range(1,8):
    consumption=int(input(f"Day {i} Consumption : "))
    totalwater_consumption+=consumption
print(f"Total Water Consumed :{ totalwater_consumption} Litres")

#Factory Production Report
annual_production=0
for i in range(1,13):
    production=int(input(f"Month {i} Production : "))
    annual_production+=production
print(f"Total Annual Production :{annual_production} Units")
