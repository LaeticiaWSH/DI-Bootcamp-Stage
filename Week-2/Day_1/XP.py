# Ex1
#print("Hello world\n" * 4)
# Ex2
#print(99**3 *8)
# Ex3-done with terminal
#Ex4
#computer_brand = "Macbook Air"
#print("I have a " + computer_brand + " computer.")
# #Ex5
# print("Enter your name: ")
# name = input()
# print("Enter your age: ")
# age = input()
# print("Enter your shoe_size : ")
# shoesize = input()
# info = "I am human"
# print()
# print("My name is",name,",i am",age,"years old. I have shoe size of",shoesize,"and",info.lower(),".")
#Ex6
# print("Enter a number: ")
# a = input()
# print("Enter a number: ")
# b= input()
# if a > b:
#     print("Hello World.")
#Ex7
# print("Enter a number: ")
# n =int(input())
# if (n % 2) == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
#Ex8
#name = "Lorelei"
#print("Enter your name:")
#n = input()
#if n.lower() == name.lower():
    #print("OH! We have the same name!...THERE CAN BE ONLY ONE...")
#else:
    #  print("You're lucky.")
#Ex9
print("Enter your height(Inch): ")
print("Feet: ")
h_ft = int(input())
print("Inches: ")
h = h_ft * 12
height = round(h * 2.54,1)
if height > 145:
   print("Lucky you, you can ride the ride!")
else:
   print("Sorry! Not tall enough.")