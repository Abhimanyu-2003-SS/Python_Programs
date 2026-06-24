"""store_data=open("newfile.txt","w")
store_data.write("Welcome to Python Programming")
store_data.close()
read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()
print(store_data)

append_data=open("newfile.txt","a")
append_data.write("\n Python is a interpreted language.")
print(append_data)
append_data.close()

read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()

#using contex manager 

with open("newfile.txt","r") as f:
    print("Current Position : ",f.tell())
    f.read(6)
    print("After Read Posirion : ",f.tell())
    f.seek(4)
    print("After seek : ",f.tell())
    print(f.read())
    
with open("car.jpg","rb") as data:
    image_read=data.read()
    print(image_read)

#tryout pip install pillow and use its functions

tech=open("delete_file.txt","x")
print(tech)
tech.close()

filepath="delete_file.txt"

import os
if os.path.exists(filepath):
    os.remove(filepath)
else:
    print("File does not exits .")

#Serializarion 

#dump used for file dumps used for memory(serialization)

#pickle and json are used for serialization

import pickle

data={
    "students":["Arun","Manu","Sanu"],
    "marks" :(20,50,35),
    "subjects":{"English","Maths","Hindi"}

}

#serialization - saving data to file

with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
    
print("Data is serialized into user details ",data)

with open("user_details.pkl","rb") as file:
    loaded_data=pickle.load(file)
    print(loaded_data)
"""

#Serialization using memory location
import pickle
data={
    "students":["Arun","Manu","Sanu"],
    "marks" :(20,50,35),
    "subjects":{"English","Maths","Hindi"}

}

dump_data=pickle.dumps(data)
print("Data is serialized to bytes : ",dump_data)

load_data=pickle.loads(dump_data)
print("Deserialized data : ",load_data)





