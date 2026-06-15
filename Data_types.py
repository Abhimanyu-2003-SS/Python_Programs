"""Student_name=input("Enter the student name: ")
Student_id=int(input("Enter the student id: "))
Student_mark=float(input("Enter the student mark: "))
is_Present=bool(input("T or F: "))
Languages_known=input("Enter the languages known: ").split(",")

print("Student name =",Student_name)
print("Student id =",Student_id)
print("Student mark =",Student_mark)
print("Present or not =",is_Present)
print("Languages known are ",Languages_known)

print(type(Student_name))
print(type(Student_id))
print(type(Student_mark))
print(type(is_Present))
print(type(Languages_known))"""

num1=10
num2=10

print(id(num1))
print(id(num2))

list1=[10,20]
list2=[10,20]
print(id(list1))
print(id(list2))

print(isinstance(num1,int))
print(isinstance(list1,list))