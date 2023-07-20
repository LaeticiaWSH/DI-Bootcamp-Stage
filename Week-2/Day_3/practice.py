# def Calculation(a,b):
#     add = a + b
#     sub = a - b
#     print(f"{a} + {b} = {add}")
#     print(f"{a} - {b} = {sub}")
#     return (add,sub)


# res =Calculation(10,6)
# print("The addition and substration of the numbers =",res)
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered = list(filter(lambda name: len(name)<= 4 , people))
filtered = list(map(lambda name: 'hello ' + name,filtered))
print(filtered)