# list1 = [5, 10, 15, 20, 25, 50, 20]
# # list1[3]= 200
# # print(list1)

# print(list1.index(20, 0))
# n = list1.index(20,0)
# list1[n] = 200
# print(list1)

# a_tuple = (10, 20, 30, 40)
# w ,x, y, z = a_tuple
# print(w)
# print(x)
# print(y)
# print(z)

for n in "babanana":
    print(n)

#Multiplication table of 2
for n in range(1,13):
    print(n * 2)

#multiplication table of 2 with more details.
for n in range(1,13):
    x = n * 2
    print("2 *",n,"=",x)

#User prompt _choose your multiplication table.
#Method-- 1
y = int(input("Enter your number: "))
for n in range(1,13):
    x = n * y
    print(y,"x",n,"=",x)
#Method-- 2
a =int(input("Enter your number:"))
for num in range(1,13):
    mult = a * num
    print('{} x {} = {}'.format(a,num,mult))