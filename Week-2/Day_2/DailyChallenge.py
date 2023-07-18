#Challenge 1
# list = []
# number = int(input("Enter a number: "))
# length = int(input("Enter a length: "))
# for x in range(1,length + 1):
#     mult =  x * number
#     list.append(mult)
# print(list)

#Challenge 2
list = []
word = input("Enter a word :")
list = word.split
for x in range(len(word)):
    print(x)
    if word[x] == word[x + 1]:
        del list[x]

print(list)