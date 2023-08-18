# Which of the following is not a mutable data type in Python?
# Ans = tuple

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers
squ_list = []
for i in range(1,11):
    if i % 2 == 0:
        squ_list.append(i**2)
print(squ_list)

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3
n_list = [1,2,3,4,5,6,7,8,9,10]
for i in n_list:
    if i % 2 == 0 and i % 3 == 0:
        print(i)

# Loop through the provided list of dictionaries and print the names and ages:
student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]

for i in range(len(student_list)):
    x = student_list[i]["name"]
    y = student_list[i]["age"]
    print(f"Name = {x} , age = {y}")


# Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided. 
def combine_words(*args,**kwargs):
# ---Without the expected output--
    a = ""
    for arg in args:
        a += arg + " "
    for key,value in kwargs.items():
        a += value + " "
    return a 
## ---Expected output----
    # a = ""
    # for arg in args:
    #     a += arg + " "
    # for key,value in kwargs.items():
    #     if key == "first":
    #         b = value
    #     elif key == "second":
    #         c = value
    #     elif key == "third":
    #         d = value
    # return f"{a}. {b} {c} {d}"
    
print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# ----- OOP ------
# Create a class Vehicle with string attributes type, brand, and integer attribute year. Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.

class Vehicle():
    def __init__(self,type,brand,year):
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"""
The vehicle is a {self.type} of brand {self.brand} made in year {self.year} .
"""
    

sarah_veh = Vehicle("car","toyota",2345)
# print(sarah_veh)

class Car():
    def __init__(self,brand,model,mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def __str__(self):
        return f"""
Car info : 
brand = {self.brand}
model = {self.model}
mileage = {self.mileage}
"""

# car1 = Car("kia","hybrid",27000)
# print(car1)
class ElectricCar(Car):
    def __init__(self,brand,model,mileage,battery_capacity):
        Car.__init__(self,brand,model,mileage)
        self.__battery_capacity = battery_capacity
    def __str__(self):
          return f"""
Car info : 
brand = {self.brand}
model = {self.model}
mileage = {self.mileage}
battery capacity = {self.__battery_capacity}
 """
    @battery_capacity.setter
    def setbattery_capacity(self,battery_capacity):
        if battery_capacity > -1 :
            self.__battery_capacity = battery_capacity

car4 = ElectricCar("Kia","Hybrid",27000,35)
print(car4)

class BankAccount():
    