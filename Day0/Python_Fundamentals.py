# Variable ante data store cheyyadaniki oka container (box).

name = "Prasanth"
salary = 500000

Student_Name = "Raj"
Student_Roll_Number = 12
Student_Marks = 89
Student_Grade = "A"
print(type(name))
x = 10
print(x)
print(type(x))
x = "Prasanth"
print(x)
print(type(x))
is_active = True
print(type(is_active))

Product_Name = "Laptop"
Product_Price = 55000.75
Product_Quantity = 5
In_Stock = True

print(
    f"The Available Product is {Product_Name} and the actual Price is "
    f"{Product_Price}. Available Qty in Store is {Product_Quantity} Units "
    f"Stock {In_Stock}"
)
print(type(Product_Name))
print(type(Product_Price))
print(type(Product_Quantity))
print(type(In_Stock))

print(f"My name is {Student_Name} and bearing a RollNo.{Student_Roll_Number} and I have secured {Student_Grade} Grade with {Student_Marks} Marks")

employee_name = input("Enter Employee Name: ")
employee_id = int(input("Enter Employee ID: "))
salary = float(input("Enter Salary: "))

print(f"Employee Name : {employee_name}")
print(f"Employee ID : {employee_id}")
print(f"Salary : {salary}")

Student_Name = input("Enter your name : ")
Student_Roll_Number = int(input("Enter your roll no. : "))
Student_Marks = int(input("Enter your marks : "))
print(f"Welcome {Student_Name}, your marks are {Student_Marks}")


print(10 // 3)
print(10 // 4)
print(14 // 5)
print(24 // 5)

# Task 1 🚀 : Create a Simple Shopping Bill Program

Product_Price = int(input("Enter Product Price :"))
Quantity = int(input("How much quantity do you need :"))
Total_Amount = Product_Price * Quantity
print(f"Total Bill = {Total_Amount}")

Salary = int(input("Enter your salary here :"))
if Salary > 30000 :
    print(True)
else :
    print(False)

for i in name :
    print(i)

for i in str(salary) :
    print(salary)

name = "Prasanth"
# Each character has a position called Index.
#  P  r  a  s  a  n  t  h
#  0  1  2  3  4  5  6  7
print(name[0]) # P
print(name[0]) # S

#  P  r  a  s  a  n  t  h
# -8 -7 -6 -5 -4 -3 -2 -1
print(name[-1])

# String Length :
name = "Prasanth"
print(len(name)) #8
print(name.upper()) # PRASANTH
print(name.upper())

name = "prasanth kumar"
print(name.title()) # Prasanth Kumar

# String Replace 

city = "Vizag"
print(city.replace("Vizag", "Hyderabad"))

# String Concatenation :
first_name = "Prasanth"
last_name = "Kumar"
print(first_name + " " + last_name)

# Membership Operator : Check whether text exists.
email = "prasanth@gmail.com"
print("@gmail" in email)

email = input("Enter Email: ")
print("@gmail.com" in email)

# Employee Email Generator 
employee_name = input("Enter Name: ")
email = employee_name.lower() + "@company.com"
print(email)

Enter_First_Name = input("Enter Your First Name")
Enter_Last_Name = input("Enter Your Last Name")
print(f"{Enter_First_Name} {Enter_Last_Name}")
result = Enter_First_Name + " " + Enter_Last_Name
print(result)
print(result.lower())
print(result.upper())
print(result.title())
print(len(result))

# A List : [] is a collection of multiple values stored in a single variable.

# without List : 
student1 = "Raj"
student2 = "Ram"
student3 = "Ravi"

# with List :
students = ["Raj", "Ram", "Ravi"]
print(students[0])
print(len(students))

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])   # First Fruit
print(fruits[1])   # Second Fruit
print(fruits[-1])  # Last Fruit
print(len(fruits)) # Count

cart = ["Laptop", "Mouse"]
cart.append("Keyboard")
print(cart)

cart = ["Laptop", "Mouse"]
cart.append(["Keyboard", "Monitor"])
print(cart)
print(len(cart))

# Method	            Removes
# remove("Mouse")	    By Value
# pop(1)	            By Index

cart = ["Laptop", "Mouse", "Keyboard"]
cart.remove("Mouse")
print(cart)

# pop() : Remove using index. 
cart = ["Laptop", "Mouse", "Keyboard"]
cart.pop(0)
print(cart)

cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]
cart.remove("Mouse")
cart.pop(2)
cart[1] = "Gaming Mouse"
print(cart)

employees = ["Raj", "Ram", "Ravi"]
employees[1] = "Prasanth"
employees.append("Kumar")
employees.remove("Ravi")
print(employees)

# List Slicing :

# list[start:end] // End index include avvadu.

employees[0:3] # ['Raj', 'Prasanth', 'Kumar']     0 included
                                                # 1 included
                                                # 2 included
                                                # 3 excluded
employees[1:4] # from index 1 to 3
employees[:3] # first three 
employees[2:] # includes second index elements
employees[-2:] # last two elements

orders = [101, 102, 103, 104, 105]
print(orders[-3:]) # last three elements

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:3])
print(numbers[-2:])
print(numbers[1:4])

cart = ["Laptop", "Mouse", "Keyboard"]
cart.append("Monitor")
cart[1] = "Gaming Mouse"
cart.remove("Keyboard")
print(cart[:2])
print(cart)
print(len(cart))

# Tuples : ()

employees = ("Raj", "Ram", "Ravi")
print(employees[0])
print(employees[0])  # TypeError --> Tuple is Immutable

countries = ("India", "USA", "Japan", "Australia")
print(countries[0])
print(countries[-1])
print(len(countries))

# Tuple Methods : append(), remove(), pop(), insert()

numbers = (10, 20, 10, 30)
print(numbers.count(10)) # 2

numbers = (10, 20, 30)
print(numbers.index(20)) # 1

employee_ids = (
    101,
    102,
    103,
    104,
    101
)
print(employee_ids.count(101))
print(employee_ids.index(103))

# Sets : A Set is a collection of "unique values".
    # No Duplicates 
    # Unordered 
    # Mutable

numbers = {10, 20, 30, 10, 20}
print(numbers) # {10, 20, 30}

cities = {
    "Vizag",
    "Hyderabad",
    "Vizag",
    "Chennai",
    "Hyderabad"
}
print(cities)
print(len(cities))

skills = {"Python", "React", "MongoDB"}
skills.add("NodeJS")
skills.remove("React")
print(skills)
print(len(skills))

# Dictionaries : Key-Value Pair [JSON, JS Object, MongoDB Documents]
employee = {
    "name": "Prasanth",
    "age": 26,
    "salary": 50000
}
print(employee["name"])
print(len(employee))

student = {
    "name": "Raj",
    "roll_no": 101,
    "marks": 89
}
print(student["name"])
print(student["roll_no"])
print(student["marks"])
print(len(student))

#updating dictionary

student["marks"] = 95
print(student)

# Add New Key-Value Pair :
student["grade"] = "A"
print(student)

# Remove Key-Value Pair :
del student["marks"]
print(student)

#using get() :

student.get("city") # None

employee = {
    "name": "Prasanth",
    "age": 26,
    "salary": 50000
}
employee["salary"] = 60000
employee["Department"] = "IT"
del employee["age"]
print(employee)

# keys() and values() :
print(employee.keys())
print(employee.values())

# items() : Returns both key and value.
print(employee.items())

product = {
    "name": "Laptop",
    "price": 55000,
    "stock": 10
}
print(product.keys())
print(product.values())
print(product.items())

# for loop :
for i in range(5):
    print("Hello")

employees = ["Raj", "Ram", "Prasanth"]
for employee in employees:
    print(employee)

marks = [80, 90, 70, 95]
for mark in marks:
    print(mark)

emails = [
    "a@gmail.com",
    "b@gmail.com",
    "c@gmail.com"
]

for email in emails:
    print("Sending email to", email)

for i in range(5):   # range(start=0, stop=5)
    print(i)  # Output : 0 1 2 3 4

for i in range(1,6):
    print(i)

for i in range(10, 5):
    print(i)

skills = ["Python", "React", "MongoDB", "NodeJS"]

for skill in skills :
    print(skill)

# Loop with Index using enumerate()  : index is auto generated using this enumerate[0-n]

skills = ["Python", "React", "MongoDB"]

for index, skill in enumerate(skills) :
    print(index, skill)

for index, skill in enumerate(skills, start=1): #Default is 0 and if you change index starting from custom index value
    print(index, skill)

employees = ["Raj", "Ram", "Prasanth", "Kumar"]

for index, employee in enumerate(employees) :
    print(index, employee)

for employee in employees:
    print(employee)

    if employee == "Prasanth":
        break

for index,value in enumerate(range(1, 6)):
    if index == 4:
        break
    print(index,value)

employees = ["Raj", "Ram", "Absent", "Prasanth"]

for employee in employees:

    if employee == "Absent":
        continue

    print(f"Processing {employee}")

employee_name = "Prasanth"
employee_id = 101
salary = 50000
searchedchar = []

for char in employee_name :
    if(char == "s") :
        searchedchar.append(char)
        if (searchedchar == ['s']) :
            print(f"{employee_id} - {employee_name} kumar ")
            break
        else : 
            print("Details Not Found..")
else : 
    print("Mismatching Character Search")

# Print Numbers

for i in range(10):
    print(i+1)

# Print Even Numbers
even_nums = []
for i in range(2, 21) :
        if i % 2 == 0 : 
            even_nums.append(i)
print(even_nums)

# Print Multiplication Table 
multiples_of_five = []
for i in range(5,61) :
    if i % 5 == 0 :
        multiples_of_five.append(i)
print(multiples_of_five)

# Count Characters

text = "Programming"
count = {}

for char in text :
    if char in count :
        count[char] += 1
    else :
        count[char] = 1
print(count)

# Reverse a String :

string = "Prasanth"
rev_str = ""

for char in string :
    rev_str = char + rev_str
print(rev_str)

# Find Maximum Number

numbers = [45, 23, 89, 12, 56, 34]
maximum = numbers[0]
print(maximum)

for num in numbers :
    # print(num)
    if num > maximum :
        maximum = num 
print(maximum)

# Sum of Numbers
n = 10

for num in range(0,n) :
    # print(num)
    n += num
print(n)

# Factorial

n = 5

for num in range(1,n) :
    # print(num)
    n = n*num                                                               
print(n)

n = 5
result = 1
for num in range(1,n+1) :
    # print(num)
    result = result*num                                                               
print(result)

# #  Fibonacci Series

n = 7

fab = 0
fab_1 = 1

for num in range(n) :
    print(fab , end=" ")
    next_num = fab + fab_1 
    fab = fab_1
    fab_1 = next_num

# Prime Number Checker

num1= 17
is_prime = True

if num1 < 2:
    is_prime = False
else :
    for i in range(2, num1) :
        if num1 % i == 0 :
            is_prime = False
            break
if is_prime :
    print(f"\n {num1} is a Prime Number")
else :
    print(f"\n {num1}is not a Prime Number")

# Multiplication Matrix :
    # Print a 5x5 multiplication table
    # Expected Output:
    # 1  2  3  4  5
    # 2  4  6  8  10
    # 3  6  9  12 15
    # ...


# Star Pattern - Triangle :

#  Star Pattern - Diamond :

# Find Duplicate Numbers :








