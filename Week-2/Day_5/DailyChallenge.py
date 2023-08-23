#Challenge 1 : Sorting
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Use List Comprehension
phrase = input("Enter a comma separated sequence of words: ")
string = phrase.split(",")
string.sort()
word = ""
for i in string :
    word += i + ","
print(word)

#Challenge 2 : Longest Word
#Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word. 
#Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

sentence = input("Enter a sentence : ")
my_string = sentence.split(" ")
max = my_string[0]
m = 0
max = " "
for i in my_string:
    x = len(i)
    if m < x:
        max = i
        m = x
print(f"The longest word = {max}")
