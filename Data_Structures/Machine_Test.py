#College Admission Management System

courses = ("BCA", "BSc", "BCom", "BA", "BTech")


names = []
cities = set()
students = {}

total_marks = 0


for i in range(10):
    print(f"\nEnter details of Student {i+1}")

    name = input("Name: ")
    age = int(input("Age: "))
    city = input("City: ")
    course = input("Course: ")
    marks = float(input("Marks: "))

    names.append(name)
    cities.add(city)

    students[name] = {
        "Age": age,
        "City": city,
        "Course": course,
        "Marks": marks
    }

    total_marks += marks


average = total_marks / 10
print("\nAverage Marks:", average)


topper = max(students, key=lambda x: students[x]["Marks"])
lowest = min(students, key=lambda x: students[x]["Marks"])

print("\nTopper:")
print(topper, "-", students[topper]["Marks"])

print("\nLowest Scorer:")
print(lowest, "-", students[lowest]["Marks"])


sorted_students = sorted(
    students.items(),
    key=lambda x: x[1]["Marks"],
    reverse=True
)

print("\nStudents Sorted by Marks:")
for name, details in sorted_students:
    print(name, "-", details["Marks"])


search_name = input("\nEnter student name to search: ")

if search_name in students:
    print("Student Found:")
    print(students[search_name])
else:
    print("Student not found.")


print("\nStudents Eligible for Admission:")
for name, details in students.items():
    if details["Marks"] >= 75:
        print(name, "-", details["Marks"])


print("\nNames List:")
print(names)

print("\nAvailable Courses Tuple:")
print(courses)

print("\nUnique Cities Set:")
print(cities)


#Online Shooping Management System

categories = ("Electronics", "Clothing", "Books", "Groceries")


products = {}


brands = set()


cart = []

n = int(input("Enter number of products: "))


for i in range(n):
    print(f"\nProduct {i+1}")

    pname = input("Product Name: ")
    price = float(input("Price: "))
    brand = input("Brand: ")

    products[pname] = price
    brands.add(brand)


print("\nAvailable Products:")
for product, price in products.items():
    print(product, "-", price)


m = int(input("\nHow many products to add to cart? "))

for i in range(m):
    item = input("Enter product name: ")

    if item in products:
        cart.append(item)
    else:
        print("Product not found!")


total = 0

for item in cart:
    total += products[item]

print("\nTotal Bill =", total)


discount = 0

if total >= 5000:
    discount = total * 0.20
elif total >= 3000:
    discount = total * 0.10
elif total >= 1000:
    discount = total * 0.05

final_bill = total - discount

print("Discount =", discount)
print("Final Bill =", final_bill)


sorted_products = sorted(products.items(), key=lambda x: x[1])

print("\nProducts Sorted by Price:")
for product, price in sorted_products:
    print(product, "-", price)


search = input("\nEnter product name to search: ")

if search in products:
    print("Product Found")
    print("Price =", products[search])
else:
    print("Product Not Found")


print("\n----- PURCHASE SUMMARY -----")
print("Items Purchased:", cart)
print("Total Amount:", total)
print("Discount:", discount)
print("Amount Payable:", final_bill)

print("\nCategories:", categories)
print("Unique Brands:", brands)

    
# Library Book Management System


categories = ("Fiction", "Science", "History", "Technology")


books = []


authors = set()


book_qty = {}


book_category = {}

n = int(input("Enter number of books: "))


for i in range(n):
    print(f"\nBook {i+1}")

    title = input("Book Title: ")
    author = input("Author: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))

    books.append(title)
    authors.add(author)

    book_qty[title] = quantity
    book_category[title] = category


search = input("\nEnter book title to search: ")

if search in books:
    print("Book Found")
    print("Available Copies:", book_qty[search])
else:
    print("Book Not Found")


print("\nAvailable Books:")
for book in books:
    if book_qty[book] > 0:
        print(book, "-", book_qty[book], "copies")


books.sort()

print("\nBooks Sorted Alphabetically:")
for book in books:
    print(book)


issue = input("\nEnter book title to issue: ")

if issue in book_qty and book_qty[issue] > 0:
    book_qty[issue] -= 1
    print("Book Issued Successfully")
else:
    print("Book Not Available")


ret = input("\nEnter book title to return: ")

if ret in book_qty:
    book_qty[ret] += 1
    print("Book Returned Successfully")
else:
    print("Book does not belong to this library")


print("\nBooks in Each Category:")

for cat in categories:
    count = 0

    for book in book_category:
        if book_category[book] == cat:
            count += 1

    print(cat, ":", count)


print("\n----- LIBRARY REPORT -----")

print("Total Books:", len(books))

print("\nBook Quantities:")
for book, qty in book_qty.items():
    print(book, "-", qty)

print("\nUnique Authors:")
for author in authors:
    print(author)

print("\nCategories:")
print(categories)
    
# Employee Performance Evaluation System


departments = ("HR", "Finance", "IT", "Marketing", "Sales")


employee_names = []


designations = set()


employees = {}

n = int(input("Enter number of employees: "))

total_score = 0


for i in range(n):
    print(f"\nEmployee {i+1}")

    name = input("Name: ")
    department = input("Department: ")
    designation = input("Designation: ")
    score = float(input("Performance Score: "))

    employee_names.append(name)
    designations.add(designation)

    employees[name] = {
        "Department": department,
        "Designation": designation,
        "Score": score
    }

    total_score += score


average = total_score / n
print("\nAverage Performance Score:", average)


best_employee = max(employees, key=lambda x: employees[x]["Score"])

print("\nBest Performing Employee:")
print(best_employee, "-", employees[best_employee]["Score"])


sorted_employees = sorted(
    employees.items(),
    key=lambda x: x[1]["Score"],
    reverse=True
)

print("\nEmployees Sorted by Score:")
for name, details in sorted_employees:
    print(name, "-", details["Score"])


search = input("\nEnter employee name to search: ")

if search in employees:
    print("\nEmployee Found:")
    print("Department:", employees[search]["Department"])
    print("Designation:", employees[search]["Designation"])
    print("Score:", employees[search]["Score"])
else:
    print("Employee not found.")


print("\nEmployee Categories:")

for name, details in employees.items():

    score = details["Score"]

    if score >= 85:
        category = "Excellent"
    elif score >= 60:
        category = "Good"
    else:
        category = "Needs Improvement"

    print(name, "-", category)


print("\n----- EMPLOYEE REPORT -----")

print("Employee Names:", employee_names)
print("Departments:", departments)
print("Unique Designations:", designations)

print("\nEmployee Details:")
for name, details in employees.items():
    print(name, ":", details)

# Movie Rating and Recommendation System

# Genres (Tuple)
genres = ("Action", "Comedy", "Drama", "Thriller", "Sci-Fi")

# Movie Names (List)
movies = []

# Unique Actors (Set)
actors = set()

# Ratings Dictionary
ratings = {}

n = int(input("Enter number of movies: "))

total_rating = 0

# Input Movie Details
for i in range(n):
    print(f"\nMovie {i+1}")

    movie = input("Movie Name: ")
    actor = input("Lead Actor: ")
    rating = float(input("Rating (out of 10): "))

    movies.append(movie)
    actors.add(actor)
    ratings[movie] = rating

    total_rating += rating

# Calculate Average Rating
average = total_rating / n

print("\nAverage Rating:", average)

# Highest Rated Movie
highest_movie = max(ratings, key=ratings.get)

print("\nHighest Rated Movie:")
print(highest_movie, "-", ratings[highest_movie])

# Sort Movies by Rating
sorted_movies = sorted(
    ratings.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nMovies Sorted by Rating:")
for movie, rating in sorted_movies:
    print(movie, "-", rating)

# Search Movie
search = input("\nEnter movie name to search: ")

if search in ratings:
    print("Movie Found")
    print("Rating:", ratings[search])
else:
    print("Movie Not Found")

# Movies Above Average Rating
print("\nMovies Above Average Rating:")

for movie, rating in ratings.items():
    if rating > average:
        print(movie, "-", rating)

# Recommendation Results
print("\nRecommended Movies:")

for movie, rating in ratings.items():
    if rating >= 8:
        print(movie, "-", rating)

# Report
print("\n----- MOVIE REPORT -----")

print("Movies:", movies)
print("Genres:", genres)
print("Unique Actors:", actors)

print("\nMovie Ratings:")
for movie, rating in ratings.items():
    print(movie, "-", rating)

# Hospital Patient Record System

# Departments (Tuple)
departments = ("Cardiology", "Neurology", "Orthopedics", "Pediatrics", "General")

# Patient Names (List)
patient_names = []

# Unique Diseases (Set)
diseases = set()

# Patient Information (Dictionary)
patients = {}

n = int(input("Enter number of patients: "))

# Input Patient Details
for i in range(n):
    print(f"\nPatient {i+1}")

    name = input("Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    disease = input("Disease: ")

    patient_names.append(name)
    diseases.add(disease)

    patients[name] = {
        "Age": age,
        "Department": department,
        "Disease": disease
    }

# Search Patient Record
search = input("\nEnter patient name to search: ")

if search in patients:
    print("\nPatient Found")
    print("Age:", patients[search]["Age"])
    print("Department:", patients[search]["Department"])
    print("Disease:", patients[search]["Disease"])
else:
    print("Patient not found")

# Count Patients per Department
print("\nPatients per Department:")

for dept in departments:
    count = 0

    for patient in patients:
        if patients[patient]["Department"] == dept:
            count += 1

    print(dept, ":", count)

# Sort Patients by Age
sorted_patients = sorted(
    patients.items(),
    key=lambda x: x[1]["Age"]
)

print("\nPatients Sorted by Age:")

for name, details in sorted_patients:
    print(name, "-", details["Age"])

# Oldest Patient
oldest = max(patients, key=lambda x: patients[x]["Age"])

# Youngest Patient
youngest = min(patients, key=lambda x: patients[x]["Age"])

print("\nOldest Patient:")
print(oldest, "-", patients[oldest]["Age"])

print("\nYoungest Patient:")
print(youngest, "-", patients[youngest]["Age"])

# Patient Statistics
print("\n----- PATIENT STATISTICS -----")

print("Total Patients:", len(patient_names))

print("\nPatient Names:")
print(patient_names)

print("\nDepartments:")
print(departments)

print("\nUnique Diseases:")
print(diseases)

print("\nPatient Records:")
for name, details in patients.items():
    print(name, ":", details)

# Banking Transaction Management System

# Account Types (Tuple)
account_types = ("Savings", "Current", "Fixed Deposit")

# Transaction Amounts (List)
transactions = []

# Unique Branches (Set)
branches = set()

# Customer Records (Dictionary)
customers = {}

n = int(input("Enter number of customers: "))

# Input Customer Details
for i in range(n):
    print(f"\nCustomer {i+1}")

    acc_no = input("Account Number: ")
    name = input("Customer Name: ")
    branch = input("Branch Name: ")
    acc_type = input("Account Type: ")

    balance = float(input("Initial Balance: "))

    t = int(input("Number of Transactions: "))

    for j in range(t):
        amount = float(input(f"Transaction {j+1}: "))
        transactions.append(amount)
        balance += amount

    branches.add(branch)

    customers[acc_no] = {
        "Name": name,
        "Branch": branch,
        "Account Type": acc_type,
        "Balance": balance
    }

# Highest and Lowest Transaction
highest = max(transactions)
lowest = min(transactions)

print("\nHighest Transaction:", highest)
print("Lowest Transaction:", lowest)

# Search Customer Account
search = input("\nEnter Account Number to Search: ")

if search in customers:
    print("\nCustomer Found")
    print(customers[search])
else:
    print("Customer Not Found")

# Sort Customers by Balance
sorted_customers = sorted(
    customers.items(),
    key=lambda x: x[1]["Balance"],
    reverse=True
)

print("\nCustomers Sorted by Balance:")

for acc_no, details in sorted_customers:
    print(acc_no, "-", details["Name"], "-", details["Balance"])

# Account Summary
print("\n----- ACCOUNT SUMMARY -----")

for acc_no, details in customers.items():
    print("\nAccount Number:", acc_no)
    print("Name:", details["Name"])
    print("Branch:", details["Branch"])
    print("Account Type:", details["Account Type"])
    print("Balance:", details["Balance"])

print("\nTransaction List:")
print(transactions)

print("\nAvailable Account Types:")
print(account_types)

print("\nUnique Branches:")
print(branches)

# Exam Result Processing System

# Subject Names (Tuple)
subjects = ("English", "Maths", "Science", "Social", "Computer")

# Student Names (List)
student_names = []

# Unique Grades (Set)
grades = set()

# Results Dictionary
results = {}

n = int(input("Enter number of students: "))

# Input Student Details
for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter student name: ")
    student_names.append(name)

    total = 0
    fail = False

    # Input marks for 5 subjects
    for subject in subjects:
        mark = int(input(f"Enter marks in {subject}: "))

        total += mark

        if mark < 40:
            fail = True

    average = total / 5

    # Grade Calculation
    if fail:
        grade = "F"
    elif average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    grades.add(grade)

    results[name] = {
        "Total": total,
        "Average": average,
        "Grade": grade,
        "Result": "Fail" if fail else "Pass"
    }

# Sort Students by Total Marks
rank_list = sorted(
    results.items(),
    key=lambda x: x[1]["Total"],
    reverse=True
)

print("\nStudents Sorted by Total Marks:")
for name, details in rank_list:
    print(name, "-", details["Total"])

# Search Student
search = input("\nEnter student name to search: ")

if search in results:
    print("\nStudent Found")
    print(results[search])
else:
    print("Student Not Found")

# Pass/Fail Statistics
pass_count = 0
fail_count = 0

for details in results.values():
    if details["Result"] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("\nPass Students:", pass_count)
print("Fail Students:", fail_count)

# Rank List
print("\n----- RANK LIST -----")

rank = 1
for name, details in rank_list:
    print(
        "Rank", rank,
        "-", name,
        "- Total:", details["Total"],
        "- Grade:", details["Grade"]
    )
    rank += 1

# Result Summary
print("\n----- RESULT SUMMARY -----")

print("Subjects:", subjects)
print("Student Names:", student_names)
print("Unique Grades:", grades)

print("\nStudent Results:")
for name, details in results.items():
    print(name, ":", details)

# Travel Booking Management System

# Available Destinations (Tuple)
destinations = ("Goa", "Delhi", "Kerala", "Manali", "Jaipur")

# Traveler Names (List)
travelers = []

# Unique Travel Agencies (Set)
agencies = set()

# Booking Details (Dictionary)
bookings = {}

n = int(input("Enter number of travelers: "))

total_revenue = 0

# Input Booking Details
for i in range(n):
    print(f"\nTraveler {i+1}")

    name = input("Traveler Name: ")
    destination = input("Destination: ")
    agency = input("Travel Agency: ")
    cost = float(input("Package Cost: "))

    travelers.append(name)
    agencies.add(agency)

    bookings[name] = {
        "Destination": destination,
        "Agency": agency,
        "Cost": cost
    }

    total_revenue += cost

# Search Booking
search = input("\nEnter traveler name to search: ")

if search in bookings:
    print("\nBooking Found")
    print(bookings[search])
else:
    print("Booking Not Found")

# Sort Travelers by Package Cost
sorted_travelers = sorted(
    bookings.items(),
    key=lambda x: x[1]["Cost"],
    reverse=True
)

print("\nTravelers Sorted by Package Cost:")
for name, details in sorted_travelers:
    print(name, "-", details["Cost"])

# Find Most Popular Destination
destination_count = {}

for details in bookings.values():
    dest = details["Destination"]

    if dest in destination_count:
        destination_count[dest] += 1
    else:
        destination_count[dest] = 1

popular_destination = max(
    destination_count,
    key=destination_count.get
)

print("\nMost Popular Destination:", popular_destination)

# Total Revenue
print("\nTotal Revenue:", total_revenue)

# Travel Report
print("\n----- TRAVEL REPORT -----")

print("Traveler Names:")
print(travelers)

print("\nAvailable Destinations:")
print(destinations)

print("\nUnique Travel Agencies:")
print(agencies)

print("\nBooking Details:")
for name, details in bookings.items():
    print(name, ":", details)

print("\nMost Popular Destination:", popular_destination)
print("Total Revenue:", total_revenue)

# Restaurant Order Management System

# Categories (Tuple)
categories = ("Starter", "Main Course", "Dessert", "Beverage")

# Menu Items (Dictionary)
menu = {}

# Unique Customers (Set)
customers = set()

# Ordered Items (List)
orders = []

n = int(input("Enter number of menu items: "))

# Input Menu
for i in range(n):
    item = input("\nEnter Item Name: ")
    price = float(input("Enter Price: "))

    menu[item] = price

# Customer Details
customer = input("\nEnter Customer Name: ")
customers.add(customer)

# Place Order
m = int(input("How many items to order? "))

bill = 0

for i in range(m):
    item = input("Enter item name: ")

    if item in menu:
        orders.append(item)
        bill += menu[item]
    else:
        print("Item not available")

# Apply Discount
discount = 0

if bill >= 2000:
    discount = bill * 0.20
elif bill >= 1000:
    discount = bill * 0.10

final_bill = bill - discount

# Search Menu Item
search = input("\nEnter menu item to search: ")

if search in menu:
    print("Item Found")
    print("Price:", menu[search])
else:
    print("Item Not Found")

# Sort Menu by Price
sorted_menu = sorted(menu.items(), key=lambda x: x[1])

print("\nMenu Sorted by Price:")
for item, price in sorted_menu:
    print(item, "-", price)

# Most Ordered Item
order_count = {}

for item in orders:
    if item in order_count:
        order_count[item] += 1
    else:
        order_count[item] = 1

if len(order_count) > 0:
    most_ordered = max(order_count, key=order_count.get)
    print("\nMost Ordered Item:", most_ordered)

# Order Summary
print("\n----- ORDER SUMMARY -----")

print("Customer Name:", customer)
print("Ordered Items:", orders)
print("Total Bill:", bill)
print("Discount:", discount)
print("Amount Payable:", final_bill)

print("\nCategories:")
print(categories)

print("\nUnique Customers:")
print(customers)

# Cricket Tournament Analysis System

# Match Types (Tuple)
match_types = ("Test", "ODI", "T20")

# Player Names (List)
players = []

# Unique Teams (Set)
teams = set()

# Player Scores (Dictionary)
player_scores = {}

n = int(input("Enter number of players: "))

total_runs = 0

# Input Player Details
for i in range(n):
    print(f"\nPlayer {i+1}")

    name = input("Player Name: ")
    team = input("Team Name: ")
    runs = int(input("Runs Scored: "))

    players.append(name)
    teams.add(team)

    player_scores[name] = {
        "Team": team,
        "Runs": runs
    }

    total_runs += runs

# Total Runs
print("\nTotal Tournament Runs:", total_runs)

# Highest Scorer
highest_scorer = max(
    player_scores,
    key=lambda x: player_scores[x]["Runs"]
)

print("\nHighest Scorer:")
print(highest_scorer, "-", player_scores[highest_scorer]["Runs"])

# Sort Players by Runs
sorted_players = sorted(
    player_scores.items(),
    key=lambda x: x[1]["Runs"],
    reverse=True
)

print("\nPlayers Sorted by Runs:")
for name, details in sorted_players:
    print(name, "-", details["Runs"])

# Search Player Statistics
search = input("\nEnter player name to search: ")

if search in player_scores:
    print("\nPlayer Found")
    print("Team:", player_scores[search]["Team"])
    print("Runs:", player_scores[search]["Runs"])
else:
    print("Player Not Found")

# Team-wise Report
print("\n----- TEAM-WISE REPORT -----")

for team in teams:
    team_runs = 0
    player_count = 0

    for player, details in player_scores.items():
        if details["Team"] == team:
            team_runs += details["Runs"]
            player_count += 1

    print(
        team,
        "- Players:", player_count,
        "- Total Runs:", team_runs
    )

# Tournament Summary
print("\n----- TOURNAMENT SUMMARY -----")

print("Match Types:")
print(match_types)

print("\nPlayers:")
print(players)

print("\nTeams:")
print(teams)

print("\nTotal Runs:", total_runs)

print("Highest Scorer:",
      highest_scorer,
      "-",
      player_scores[highest_scorer]["Runs"])

print("\nPlayer Statistics:")
for player, details in player_scores.items():
    print(player, ":", details)

# Smart City Survey Analysis System

# Survey Categories (Tuple)
categories = (
    "Roads",
    "Water Supply",
    "Electricity",
    "Healthcare",
    "Cleanliness"
)

# Citizen Names (List)
citizens = []

# Unique Locations (Set)
locations = set()

# Responses (Dictionary)
responses = {}

n = int(input("Enter number of citizens: "))

# Input Survey Responses
for i in range(n):
    print(f"\nCitizen {i+1}")

    name = input("Enter Name: ")
    location = input("Enter Area/Location: ")
    category = input("Enter Survey Category: ")
    feedback = input("Enter Feedback: ")
    rating = int(input("Enter Rating (1-10): "))

    citizens.append(name)
    locations.add(location)

    responses[name] = {
        "Location": location,
        "Category": category,
        "Feedback": feedback,
        "Rating": rating
    }

# Count Category-wise Responses
print("\nCategory-wise Response Count:")

for cat in categories:
    count = 0

    for details in responses.values():
        if details["Category"] == cat:
            count += 1

    print(cat, ":", count)

# Search Citizen Feedback
search = input("\nEnter Citizen Name to Search: ")

if search in responses:
    print("\nFeedback Found")
    print(responses[search])
else:
    print("Citizen Record Not Found")

# Calculate Area Ratings
area_ratings = {}

for details in responses.values():
    area = details["Location"]
    rating = details["Rating"]

    if area in area_ratings:
        area_ratings[area] += rating
    else:
        area_ratings[area] = rating

# Sort Areas by Ratings
sorted_areas = sorted(
    area_ratings.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nAreas Sorted by Ratings:")
for area, rating in sorted_areas:
    print(area, "-", rating)

# Highest Rated Area
highest_area = max(area_ratings, key=area_ratings.get)

# Lowest Rated Area
lowest_area = min(area_ratings, key=area_ratings.get)

print("\nHighest Rated Area:", highest_area)
print("Lowest Rated Area:", lowest_area)

# Final Survey Report
print("\n----- FINAL SURVEY REPORT -----")

print("Citizen Names:")
print(citizens)

print("\nSurvey Categories:")
print(categories)

print("\nUnique Locations:")
print(locations)

print("\nArea Ratings:")
for area, rating in area_ratings.items():
    print(area, "-", rating)

print("\nHighest Rated Area:", highest_area)
print("Lowest Rated Area:", lowest_area)

print("\nCitizen Responses:")
for name, details in responses.items():
    print(name, ":", details)

