##__EX 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# x = zip(keys,values)
# print(dict(x))

##__EX 2
# Tcost = 0
# family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for member,age in family.items():
#     if age < 3 :
#         Tcost += 0
#         cost = 0
#     elif (3<= age <=12):
#         Tcost += 10
#         cost = 10
#     else:
#         Tcost += 15
#         cost = 15
#     print(member,"has to pay $",cost)
# print("The total cost is = $",Tcost)
# #-------EX 2---BONUS----------------
# family ={}
# name = []
# age =[]
# Tcost = 0
# s = input("Press start/end/next:")
# while (s.lower() == "start" or s.lower() == "next"):
#     n = input("Enter name: ")
#     a = input("Enter age :")
#     name.append(n)
#     age.append(a)
#     s = input("Press end/next:")
# print(name,age)
# family = zip(name,age)
# print(dict(family))

##__Ex 3
# brand ={
#     "name": "Zara",
#     "creation_date": "1975",
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ['men', 'women', 'children', 'home'],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000 ,
#     "major_color": {
#        "France": "blue", 
#         "Spain": "red", 
#         "US": "pink, green"
#     }
# }
# ##Part 3 --Change the number of stores to 2.
# brand["number_stores"] = 2
# print(brand)
# ##Part 4
# clients = ",".join(brand["type_of_clothes"])
# print(f"Zara has a variety of clients namely {clients}")
# ##Part 5
# brand.__setitem__("country_creation", "Spain")
# print(brand)
# ##Part 6
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
# print(brand)
# ##Part 7
# brand.pop("creation_date")
# print(brand)
##Part 8
# last = brand["international_competitors"][-1]
# print(last)
# ##Part 9
# print(brand["major_color"]["US"])
# ##Part 10
# print(len(brand.items()))
# ##Part 11
# print(brand.keys())
# ##Part 12
# more_on_zara = {
#     "creation_date": "1975",
#     "number_stores": "10 000"
#  }
# ##Part 13
# brand |= more_on_zara
# print(brand)
# ##Part 14
# print(brand["number_stores"])
# # #---The "number_stores" = 10 000 # #

##__Ex 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
##Part 1
disney_users = [ ]
for index in users:
    disney = int(input("Enter disney users :"))
    disney_users.append(disney)
disney_users_A = zip(users,disney_users)
print(dict(disney_users_A))

# Part 2
disney_users_B = zip(disney_users,users)
print(dict(disney_users_B))

#Part 3
disney_users_C = sorted(list(zip(users, disney_users)), key=str)
print(disney_users_C)

#Part 4
# i = 0
# j = { }
# count = len(users)
# for index in users:
#     print(index)
#     while i <  len(index):
#         print(users[i - 1])
#         i += 1
#         if users[i] == "i":
#             j.append(users[index])
#         else :
#             if users
# print(j)

