import random
print("-------------MENU--------------\n")
print("(s) ---> Play a new game.")
print("(x) ---> Show scores and exit.\n")
print("--------------------------------")

class win :
    def __init__(self,output):
        self.output = output
        list = ['rock','paper','scissors']
        self.choice = random.choice(list)
        self.game_lost = 0
        self.game_win = 0
        print(f"The opponent chose {self.choice}")
    

    def winner(self):
        G_list =[['rock','paper'],['paper','scissors'],['scissors','rock']]
        if self.output == self.choice:
            print("____It's a tie!____")
        else:
            for j in range(len(G_list)):
                if self.output in G_list[j] and self.choice in G_list[j]:
                    if self.output == G_list[j][0]:
                        self.game_lost += 1
                        print("You have lost")
                        
                    else:
                        self.game_win += 1
                        print("You have won! --- congrats.")


    def winlose(self):
        print(f"The number of games won = {self.game_win} and the number of game lost = {self.game_lost}\n")
                 
inp = input("Press s/x :")

while inp.lower() == "s":
    player1 = (input("\nSelect rock,paper,scissors: "))
    out = win(player1)
    out.winner()
    inp = input("\nPress s/x :")
out.winlose()





