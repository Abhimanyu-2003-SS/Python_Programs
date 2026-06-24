student=open("student_details.txt","x")
student.close()

with open("student_details.txt","w") as student:
    student.write("Name : Abhi \n Age : 23 \n Place : Kollam")
with open("student_details.txt","a") as append_stud:
   append_stud.write("\n Currently Learning Python")

with open("student_details.txt","r") as append_stud:
    print(append_stud.read())
    print(append_stud.readline())
    print(append_stud.readline())
    print("File Name : \n",append_stud.name)
    print("File Mode : \n",append_stud.mode)
    print("File Closed Status : \n",append_stud.closed)
    append_stud.seek(5)
    print("Current Pointer : ",append_stud.tell())



import pickle

stud_data={
    "English": "71",
    "Maths"  : "70",
    "Science" : "72",
    "Social_Studies" : "75"
}

with open("stud_details.pkl","wb") as f:
    print(pickle.dump(stud_data,f))
    
with open("stud_details.pkl","rb") as file:
    print(pickle.load(file))

import json

with open("stud_details.pkl","w") as f:
   print(json.dump(stud_data,f))
    




  
