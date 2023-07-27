import random
# # Ex 1 : Concatenate lists -- Write code that concatenates two lists together without using the + sign.
# list1 =['apple','orange','kiwi','pear']
# list2 = ['litchi','mango','tomatoes']
# for i in list1:
#     list2.append(i)
# print(list2)

# # Ex 2 :Range Of Numbers -- Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
# for i in range(1500,2501):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)

# # Ex 3 :Check The Index -- Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# name = input("Enter a name: ")
# for i in names:
#     if name.lower() == i.lower():
#         x = names.index(i)
        
# print("The index of the name: ",x)

# # Ex 4 : Greatest Number -- Ask the user for 3 numbers and print the greatest number.
# n1 = input("Input the 1st number: ")
# n2 = input("Input the 2nd number: ")
# n3 = input("Input the 3rd number: ")
# if (n1 > n2) and (n1 > n3):
#     print("The greatest number is :",n1)
# elif (n2 > n1) and (n2 > n3):
#     print("The greatest number is :",n2)
# else:
#     if (n3 > n2) and (n3 > n1):
#         print("The greatest number is :",n3)

# # Ex 5 :The Alphabet -- Create a string of all the letters in the alphabet.Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
# mystring = "abcdefghijklmnopqrstuvwxyz"
# for i in mystring:
#     if i in "aeiou":
#         print(f"{i} is a vowel.")
#     else:
#         print(f"{i} is a consonant.")


# # Ex 6 : Words And Letters
# -----Ask a user for 7 words, store them in a list named words.
# -----Ask the user for a single character, store it in a variable called letter.
# -----Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# -----If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
# words = []
# for i in range(0,7):
#     word = input("Enter a word: ")
#     words.append(word)

# letter = input("Enter a single character e.g a/b/C: ")
# for j in words:
#     if letter.lower() in j.lower():
#         x =words.index(j)
#         print(x)
#     else:
#         print(f"Sorry..There is no {letter} in {j}.")
    
# # Ex 7 -- Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
# mu_list = []
# for i in range(1,1000001):
#     mu_list.append(i)
# print(max(mu_list))
# print(min(mu_list))
# print(sum(mu_list))

# # Ex 8 : List And Tuple -- Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# num = input("Enter a sequence of numbers: ")
# number = num.split(",")
# print(number)
# tuple = tuple(dict.fromkeys(number))
# print(tuple)

# # Ex 9 : Random Number -- Ask the user to input a number from 1 to 9 (including).
# # --- Get a random number between 1 and 9. Hint: random module.
# # --- If the user guesses the correct number print a message that says Winner.
# # ---If the user guesses the wrong number print a message that says better luck next time.
# num = int(input("Enter a number between 1 and 9: "))
# while num < 1 or num > 9:
#     num = num = int(input("Enter a number between 1 and 9: "))
# randomNo = random.randint(1,9)
# if num == randomNo:
#     print("Winner")
# else :
#     print(" ----Try again better luck next time----")

#  # Bonus
# game_won = 0
# game_lost = 0
# press = input("Start or quit ? ")
# while press.lower() == "start":
#     num = int(input("Enter a number between 1 and 9: "))
#     while num < 1 or num > 9:
#         num = num = int(input("Enter a number between 1 and 9: "))
#     randomNo = random.randint(1,9)
#     if num == randomNo:
#         print("Winner")
#         game_won += 1
#     else :
#         print(" ----Try again better luck next time----")
#         game_lost += 1
#     press = input("Start or quit ? ")
# print("Game won =",game_won,"Game lost =",game_lost)


    
