customer_name=input("Enter Customer Name : ")
mobile_number=int(input("Enter Your Mobile Number : "))
food_item_name=input("Enter The Name Of The Food Item : ")
quantity=int(input("Enter The Quantity : "))
price_per_item=(float(input("Enter The Price Per Item : ")))
delivery_distance=int(input("Enter Delivery Distance : "))
membership=input("Premium Membership Status (True or False) : ")
print("----FOOD ORDER BILL----")
def calculate_food_amount(quantity,price_per_item):
    total_amount=quantity*price_per_item
    return total_amount

def calculate_delivery_charge(delivery_distance):
    if delivery_distance< 5:
        delivery_charge=40
    else:
        delivery_charge=80
    return delivery_charge

def calculate_discount(bill_amount,membership):
    discount=0
    if membership=="True":
        if bill_amount > 1000:
            discount-=150

    return discount

def generate_bill(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

food_amount=calculate_food_amount(quantity,price_per_item)

generate_bill(customer_name=customer_name,mobile=mobile_number,item=food_item_name)

def restaurant_details(name="FoodHub"):
    print("Restaurant Name : ",name)

def add_extra_items(*items):
    print(f"Extra items : {items}\n")

#def customer_details(**details):
bill_amount=food_amount+delivery_distance

delivery_charge=calculate_delivery_charge(delivery_distance)
discount_amount=calculate_discount(bill_amount,membership)
final_bill=bill_amount-discount_amount

print("Food Amount : ",food_amount)
print("Delivery Charge : ",delivery_charge)
print("Discount : ",discount_amount)
print("\n")

print("Final Bill Amount : ",final_bill)
print("/n")
print(type(quantity))
print(type(price_per_item))
print(type(membership))
print("\n")
print(isinstance(quantity,int))
print(isinstance(price_per_item,float))
print(isinstance(membership,bool))
print("\n")

print(id(food_amount))
print(id(final_bill))
print("\n")

def display_offer():
    print("offer:Flat 50% Off On Softdrinks Purchases Above 1000")

display_offer()

def get_offer():
    return "Offer starts soon"

menu=["pizza","burger","sandwich","hotdog"]

def search_food(menu,food_item_name):
    if food_item_name in menu:
        return food_item_name
    else:
        return 0
    
result=search_food(menu,food_item_name)
print(f"Food Search Result : {result}")

    