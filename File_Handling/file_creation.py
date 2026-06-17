store_data=open("newfile.txt","w")
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


