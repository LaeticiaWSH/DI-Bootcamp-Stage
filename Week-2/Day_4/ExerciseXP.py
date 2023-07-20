#EX 1
# def display_message():
#     message = "I am currently learning the python course."
#     print(message)

# display_message()

# #EX 2
# def favorite_book(title):
#     message = "One of my favorite books is " + title
#     print(message)
# title = input("Enter your favorite book: ")
# favorite_book(title)

# #EX 3
# def describe_city(city,country = "Iceland"):
#     print(city,"is in",country)
# describe_city("Ottawa")

#EX 4
# import random
# def randomize(n1):
#     n2 = (random.randint(1,100))
#     if n2 == n1 :
#         print("Success! You've suceeded!")
#     else:
#         print("OH nooo!---Better luck next time.")
#     print("The number was",n2,",your number was",n1)
# n1 = int(input("Enter your number :"))
# randomize(n1)

#EX 5
# def make_shirt(size,text = "I love python"):
#     message = "The size of the shirt is  " + size + " and the text is '" + text + "'."
#     print(message)

# make_shirt()
#EX 6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians():
#     for magician in magician_names:
#         print("Name :",magician)
# show_magicians()
# def make_great():
#     for magician in range(len(magician_names)):
#         text = " the Great"
#         magician_names[magician] =magician_names[magician] + text
#     print(magician_names)
# make_great()
# show_magicians()

#EX 7
# import random
# def get_random_temp(season):
#     if season.lower == "winter":
#         num = random.randint(-10,16)
#     else:
#         num = random.randint(-10,40)
#     return num
    
# def main():
#     season = input("Enter a season e.g summer/winter/autumn/fall:")
#     n =(get_random_temp(season))
#     print("The temperature right now is",n,"degrees celcius.")
#     if n < 0 :
#         print("Brrr, that's freezing! Wear some extra layers today")
#     elif 0<= n <= 16 :
#         print("Quite chilly! Don’t forget your coat")
#     elif 16< n <= 23 :
#         print("Cover your head with a hat")
#     elif 23< n <= 32 :
#         print("Cool yourself down.")
#     elif 32< n <= 40 :
#         print("Time to go for a swim.")
# main()
# #------BONUS PART-------
# import random
# def get_random_temp(season):
#     if season == "winter":
#         num = random.randint(-10,16)
#     else:
#         num = random.randint(-10,40)
#     return num
    
# def main():
#     month = input("Enter a season e.g January/February:")
#     if month.lower() == "january" or month.lower() == "february" or month.lower() == "december" :
#         season = "winter"
#     if month.lower() == "march" or month.lower() == "april" or month.lower() == "may" :
#         season = "spring"
#     if month.lower() == "june" or month.lower() == "july" or month.lower() == "august" :
#         season = "summer"
#     if month.lower() == "september" or month.lower() == "october" or month.lower() == "november" :
#         season ="autumn"
    
#     n =float(get_random_temp(season))
#     print("The temperature right now is",n,"degrees celcius.")
#     if n < 0 :
#         print("Brrr, that's freezing! Wear some extra layers today")
#     elif 0<= n <= 16 :
#         print("Quite chilly! Don’t forget your coat")
#     elif 16< n <= 23 :
#         print("Cover your head with a hat")
#     elif 23< n <= 32 :
#         print("Cool yourself down.")
#     elif 32< n <= 40 :
#         print("Time to go for a swim.")
# main()
 #EX 5
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# wrong_ans = [ ]
# wrong_quest = [ ]
# def StarWars():
#     correct_answer = 0
#     incorrect_answer = 0
#     for datas in data:
#         print(datas["question"])
#         answer =input("Enter your answer:")
#         if answer.lower() == datas["answer"].lower():
#             correct_answer += 1
#         else:
#             incorrect_answer += 1
#             wrong_ans.append(answer)
#             wrong_quest.append(datas["question"])
#     print("Your score is",correct_answer ,"/ 6\n")
#     # print(wrong_list)
#     i = 0
#     for items in wrong_ans:
#         print("Your wrong answer was",items, "to the question",wrong_quest[i])
#         i += 1
#     if incorrect_answer >= 3 :
#         print("Do you want to play again ?")
# StarWars()
