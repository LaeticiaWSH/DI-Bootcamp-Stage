#Challenge 1
# list = []
# number = int(input("Enter a number: "))
# length = int(input("Enter a length: "))
# for x in range(1,length + 1):
#     mult =  x * number
#     list.append(mult)
# print(list)

#Challenge 2
# list = []
# word = input("Enter a word :")
# w = ' ' .join(word)
# list.append (w.split())
# for x in range(len(word)):
#     print(x)
#     # if word[x] == word[x + 1]:
#     #     l= word[x]
#     #     i = word[x + 1]
#     # print(l)
#     # list.append(l)
#     if list[x] == list[x + 1]:
#         list.remove[x]

# print(list)

word = input("Enter a word: ")
i = 0
j = 0
correctword = " "
while (j < len(word)):
    if word[i] == word[j]:
        j+=1
    elif ((word[j]!= word[i]) or (j == len(word) - 1)):
        correctword += word[i]
        i = j
        j += 1

correctword += word[j - 1]
print(correctword)