print("Library Book Management System ")
book_names=["Wings_of _fire","Balarama","Kalikuduka"]
category=("Kids","Noval","Fantasy")
authors={"kalam","Anju","Hari"}
issued=["Avatar","Got","openhimer"]
returned=["openhimer","Hunger Games"]

quantity={

    "kids": 5,
    "noval": 3,
    "fantasy":6
}



print("\n")
print("----Library report----")
print("\n")
print(f"Available Books : {book_names}")
print("After Sorting : ",sorted(book_names))
print(f"Category Of Books : {category}")
print(f"Authors : {authors}")
print(f"Book Issued : {issued}")
print(f"Book Returned : {returned}")
search=input("Enter book to Search :")

if search in book_names:
    print("Book Available")
else:
    print("Book Not Avilable")

print(f"Books In kids Category : {quantity['kids']} ")
print(f"Books In Noval Category : {quantity['noval']} ")
print(f"Books In Fantasy Category : {quantity['fantasy']} ")
