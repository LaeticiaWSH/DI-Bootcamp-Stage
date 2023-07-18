#Ex 1
# my_fav_numbers = {8, 16 ,14 ,20}
# print(my_fav_numbers)
# my_fav_numbers.add(2003)
# my_fav_numbers.add(2007)
# print(my_fav_numbers)
# my_fav_numbers.remove(2007)
# print(my_fav_numbers)

# friend_fav_numbers ={26 ,7 ,2005}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# #Ex 2
#It's not possible to add integers to the tuple.

#Ex 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove(("Banana"))
# print(basket)
# basket.remove("Blueberries")
# basket.append("Kiwi")
# print(basket)
# basket.insert(0,"Apples")
# print(basket)
# count = 0
# for n in range (len(basket)):
#     if basket[n] == "Apples":
#         count = count + 1
# print("There is a total of",count,"apples in the basket.")
# basket.clear()
# print(basket)

#Ex 4
#list = []
# for n in range(3,11):
#     list.append(n / 2)
# print(list)


#Ex 5
# for x in range(1,21):
#     print(x)
# for x in range(1,21):
#     if x % 2 == 0
#         print(x)

#Ex 6
# my_name = "Laelae"
# name =input("what's your name ? ")
# while (my_name.lower() != name.lower() ) :
#    name =input("what's your name ? ")
# print("We have the same name")

#Ex 7
# found = False
# fruits = []
# f = input("Enter your favorite fruits e.g 'apple mango cherry': ").split()
# print(f)
# name = input("Enter the name of any fruit:")
# for x in fruits:
#     if name == fruits[x]:
#         print("You chose one of your favorite fruits! Enjoy!.")
#         found = True
# if found == False:
#     print("You chose a new fruit. I hope you enjoy.")
      
#Ex 8
# list = []
# print("Choose your toppings: Pepperoni(P)| Xcheese(X)| Mushroom(M)| Black Olives(BO)| Pineapples(PA)")
# extra = 0
# price = 0
# while  True:
#     toppings = input("Enter pizza topping(or type quit- to end): ")
#     if toppings.lower() == "quit":
#        break
#     else:
#         print("We'll add",toppings,"to your pizza!")
#         list.append(toppings)
#         extra = extra + 1
# print(list)
# price = 10 + ( extra * 2.5)
# print("Your total price is = $",price)

#Ex 9 part(1, 2, 3)
# Tcost = 0
# print("Tickets for how many people please: ")
# num= int(input())
# n = 1
# while (n <= num):
#         n = n + 1
#         age = int(input("Enter your age e.g 1 , 19, 27: "))
#         if age < 3:
#             Tcost = Tcost + 0
#         elif age in range(3,13):
#             Tcost = Tcost + 10
#         elif (age > 12):
#             Tcost = Tcost + 15
# print("The total cost of tickets will be: £",Tcost)
#Ex 9 part(4)
# list = [ ]
# Continue = input("Continue Y/N:")
# while Continue.lower() == "y":
#     name = input("Enter your name teenager! :")
#     list.append(name)
#     age = int(input("Enter your age e.g 1 , 19, 27: "))
#     if age < 16 or age > 21:
#         list.remove(name)
#     Continue = input("Continue Y/N:")

# print(list)

#Ex 10
#Part 1
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
#Part 2
finished_sandwiches = []
sandwich_orders.remove("Tuna sandwich")
finished_sandwiches.append("Tuna sandwich")
print(sandwich_orders)
print(finished_sandwiches)

sandwich_orders.remove("Avocado sandwich")
finished_sandwiches.append("Avocado sandwich")
print(sandwich_orders)
print(finished_sandwiches)

sandwich_orders.remove("Egg sandwich")
finished_sandwiches.append("Egg sandwich")
print(sandwich_orders)
print(finished_sandwiches)

sandwich_orders.remove("Chicken sandwich")
finished_sandwiches.append("Chicken sandwich")
print(sandwich_orders)
print(finished_sandwiches)

for x in finished_sandwiches:
    print("I made your",x)



