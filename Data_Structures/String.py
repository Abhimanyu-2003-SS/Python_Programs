#String is Immutable
#Cannot change the index position of string
#Takes copy to store in memory 

#usr_name="Abhimanyu"
# 0 1 2 3 4 5 6 7 8
# A b h i m a n y u # Positive indexing
#-9 -8 -7 -6 -5 -4 -3 -2 -1 #Negative indexing

#print(usr_name[-8])

#usr_name[0]="b"  #does not work
#print(usr_name)

"""
data="Python is a Programming Language"
print(data[1:8])

print(data[10:3:-2])

print(data[::-1]) s
print(data[9::-1])
print(data[::-2])


# Methods in string

car="Baleno is a car"
print(car.upper())
print(car.lower())
print(car.capitalize())
print(car.title())

print(car.startswith("B"))
print(car.endswith("r"))
print(car.replace("Baleno","Alto"))
print(id(car))
vehicle=car.upper()
print(id(vehicle))


#Methods of list

usr_data=[23,"Abhi","Kollam",9562727806,"Male"]
usr_data.insert(2,"Graduate")
usr_data.append("python")
usr_data.extend("Dayscholar")


usr_data.append(["English","Malayalam","Hindi"])
usr_data.extend(["HTML","Java","Python"])

print(usr_data)
print(usr_data[17][1])

usr_data.remove(23)
usr_data.pop(12)
print(usr_data)

usr_data.reverse()
print(usr_data)
 

number=[34,50,21,13]
print(number.sort())


#Tuple

tuple1=(10,20,30,40)
print(tuple1)
nested_tuple=((1,2,3,4),21,"abhi",23,"tvm")
print(nested_tuple)

#try out indexing and slicing

print(nested_tuple[0][1])
print(nested_tuple[0:3])


#Tuple unpacking
person=("Abhi",23,"Kollam")
name,age,place=person
print(place)
print(age)
print(name)


number=(10,20,30,40,50)
num=(10,20,(30,40,50))
a,b,c=num
print(a)
print(b)
print(c)

#Alternative way
number=(10,20,30,40,50)
a,b,*c=number
print(a)
print(b)
print(c)

d,*e,f=number
print(a)
print(e)
print(f)


values=(3,5,2,7,2,5,1,4,5,4,2,1,5,6,3,2,5,6,1,2)
print(len(values))
print(values.count(5))
print(values.index(3))
print(values[3])



#To find the count of a string
count=0
usr_data=input("Enter a String : ")
for i in usr_data:
    count+=1
print(count)


#To print first non repeting character

value=input("Enter The String : ")
count=0
for i in value:
    if value.count(i)==1:
        print(i)
        break
else:
        print("NO non repeating characters")

    
s = input("Enter a string: ")

for i in s:
    count = 0

    for j in s:
        if i == j:
            count += 1

    if count == 1:
        print("First non-repeating character:", i)
        break
else:
    print("No non-repeating character found")
   

#set

student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","JS"}   
student3={"Urdu","Python"} 

student1.add("C") #can only add one value
student1.update(["Css","Html"]) #can add multiple value to set



#student1.add(["C","Java"]) #will not work
student1.add("Malayalam") #cannot have duplicate values
student1.remove("Malayalam") #used to remove values
student1.pop()#pop random characters cannot predit

student1.discard("Javascript")#will not show error if the value  not found in set
print(student1)

student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","JS"}   

print(student1.union(student2))
print(student1.intersection(student2))
print(student1.difference(student2))


set1={1,2,3,4}
set2={9,8,7,5}
set3={5,4,7,6}

print(set1.isdisjoint(set2)) 


#Frozen set

fs1=frozenset("Abhi")
fs2=frozenset([23,12,53,11])
fs3=frozenset((30,45,60))
fs4=frozenset({1,2,3}) #Normal set
print(fs1)
print(fs2)
print(fs3)

#dictonary

student={

    "name":"Abhi",  #Key Value Pair
    "age":23,
    "place":"Kollam"

}
print(student)
print(student["name"]) #Acess using key

info=dict(city="Kollam",location="Mayyanad")
print(info.keys())
print(info.values())
print(info)
print(info.get("marks")) #to get the value
student["mark"]=50

      
#Try out update
student.update({"hobby":"reading","sports":"cricket"})
print(student.pop("place"))
del student["name"] 
print(student)
    
employee={
    "emp1":{
        "name":"Abhi",
        "age" : 23
    },
    "emp2":{
        "name":"Blessin",
        "age":21
    },
    "emp3":{
        "name":"Sidharth",
        "age":21
    },
    "emp4":{
        "name":"jijo",
        "age":21
    }


}

print(employee["emp3"]["name"])
"""

set1={1,2,3,4}
set1={0,1,3,4}
print(set1)
