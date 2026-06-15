Customer_name=input("Enter the customer name : ")
Vehicle_Number=input("Enter the vehicle number : ")
Fuel_Type=input("Enter fuel type : ")
Number_litres=float(input("Enter the Quantity in litres"))
Price_per_litre=float(input("Enter the price per litre : "))
Premium_card=bool(input("Premium card(True or False)"))

print("-----PETROL BILL-----/n")
Total_fuel_Amount=Price_per_litre*Number_litres
Gst_amount=Total_fuel_Amount*(5/100)
Final_amount=Total_fuel_Amount+Gst_amount
if(Premium_card=='True'and Total_fuel_Amount>3000):
    Total_fuel_Amount-=200

print("Customer Name : ",Customer_name)
print("Vehicle number",Vehicle_Number)
print("Fuel type : /n",Fuel_Type)

print("Fuel Amount : ",Total_fuel_Amount)
print("Gst amount : ",Gst_amount)
print("Final bill amount : ",Final_amount)


print("Data type of litre : ",type(Price_per_litre))
print("Data type of premium card : ",type(Premium_card))
print("Is liters float : ",isinstance(Number_litres,float) )
print("Is premium petrol boolean : ",isinstance(Premium_card,bool))
print("Id of Total Amount",id(Total_fuel_Amount))
print("Id of final amount : ",id(Final_amount))
