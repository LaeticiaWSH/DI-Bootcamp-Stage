print("Welcome to TIC TAC TEO!")
board = [ " " for x in range(9)]
def display_board():
    row1 = "_{}_|_{}_|_{}_".format(board[0], board[1], board[2])
    row2 = "_{}_|_{}_|_{}_".format(board[3], board[4], board[5])
    row3 = " {} | {} | {} ".format(board[6], board[7], board[8])
                
    print("***************")
    print("*             *")
    print("*    |   |    *")
    print("*" ,row1, "*")
    print("*    |   |    *")
    print("*" ,row2, "*")  
    print("*    |   |    *")
    print("*" ,row3, "*")
    print("*             *")
player_1 = input("Enter your name player 1: ")
player_2 = input("Enter your name player 2: ")