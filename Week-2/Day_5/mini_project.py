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
    print("***************")

display_board()
player = print(input("Enter player index(1/2) : "))
def player_input(player):
    # player = print(input("Enter player index(1/2) : "))
    position =int(input("Enter your position(0 - 8) :"))
    if player == 1:
        symbol = "X"
    else: 
        if player == 2:
            symbol = "O"
    if board[position] == " ":
        board[position] = symbol
    else:
        print("That's not possible.")
    
win = [ ]
def check_win():
    win[
        (0,1,2)
        (3,4,5)
        (6,7,8)
        (0,4,8)
        (2,4,6)
        (0,3,6)
        (1,4,7)
        (2,5,8)
    ]
    for x in range(0,len(win)):
        if win[x] == "X":
            pass
   