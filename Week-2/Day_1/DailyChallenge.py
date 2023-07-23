import random
string = input(" Enter  a 10 character word:")
lenght = len(string)
if lenght == 10:
    print("Perfect string")
    print("first word=",string[0],"last word =",string[9])
    word = " "
    shuffle = list(string)
    shuffle = random.sample(shuffle,len(shuffle))
    shuffleword = " "
    for x in range(0,10):
        word += string[x]
        print(word)
        shuffleword += shuffle[x]
    print()
    print(shuffleword)
elif lenght < 10:
    print("String not long enough")
elif lenght > 10:
    print("String too long")