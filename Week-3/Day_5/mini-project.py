import random
print("-------------MENU--------------\n")
print("(s) ---> Play a new game.")
print("(x) ---> Show scores and exit.\n")
print("--------------------------------")

class win :
    def __init__(self,output):
        self.output = output
        # self.list = []
        list = ['rock','paper','scissors']
        self.choice = random.choice(list)
        self.game_lost = 0
        self.game_win = 0
        # print(self.output)
        print(f"The opponent chose {self.choice}")
    

    def winner(self):
        # self.list.append(self.output)
        # self.list.append(self.choice)
        # print(self.list)
        # string = " "
        # game_win = 0
        # game_lost = 0
        G_list =[['rock','paper'],['paper','scissors'],['scissors','rock']]
        if self.output == self.choice:
            print("____It's a tie!____")
            # string = "____It's a tie!____"
        else:
            for j in range(len(G_list)):
                if self.output in G_list[j] and self.choice in G_list[j]:
                    if self.output == G_list[j][0]:
                        self.game_lost += 1
                        # string = "You have lost"
                        print("You have lost")
                        
                    else:
                        self.game_win += 1
                        # string = "You have won! --- congrats."
                        print("You have won! --- congrats.")
        # inp = input("Press s/x :")
        # return game_win,game_lost

                        
                    #print(G_list[j])
                    # if self.list in G_list[j]:
                        # if self.list[0] == G_list[j][0]:
                    #         print("You have lost")
                    # # else:
                    #          print("You have won! --- congrats.")
    # def play(self):
    #      inp = input("Press s/x :")
    #      return inp

    def winlose(self):
        print(f"The number of games won = {self.game_win} and the number of game lost = {self.game_lost}\n")
                 
# player1 = (input("Select rock,paper,scissors: "))
# out = win(player1)

inp = input("Press s/x :")

while inp.lower() == "s":
    player1 = (input("\nSelect rock,paper,scissors: "))
    out = win(player1)
    out.winner()
    # print(out.play())
    inp = input("\nPress s/x :")
out.winlose()





