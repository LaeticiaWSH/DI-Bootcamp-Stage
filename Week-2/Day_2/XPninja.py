import math
import numpy as maths
##-------ERROR  ERROR---------
# # # # Ex 1
# num = input("Enter a comma seperated string of numbers ")
# D = num.split(",")
# print(D)
# list =[]
# for i in D:
#      C = 50
#      H = 30
#      j = int(i)
#     #  list.append(j)
#      print(j)
#      Q = maths.sqrt([(2 * C * j)/H])
#      list.append(Q)
#      print(Q)
# array = (maths.sqrt(list))
# arr = list(map(int,Q))
# print(arr)
# print(list)
## -------THIS IS JUST A REMINDER OF THE HARD TIMES IN LIFE---------


num = input("Enter a comma seperated string of numbers ")
Slist = num.split(",")
D = list(map(int,Slist))
print(D)
list =[]
for i in D:
     C = 50
     H = 30
     print(i)
     Q = (2 * C * i)/H
     list.append(Q)
print(Q)
list = maths.sqrt(list)
list = [int(x) for x in list]
list = [str(x) for x in list]
print(list)
l = ','.join(list)
print(l)

# Ex 2
n_list =  [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
string = " "
for n in n_list:
     string += str(n) + " "
print(string)

n_list.sort(reverse = True)
print("Sorted list in descending order: ",n_list)
