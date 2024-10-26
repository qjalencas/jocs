import random

playerToken = "X"
computerToken = "O"
board = [""] * 9
isPlayerTurn = None

def draw_board(board):
    s = ""

    for i in range(len(board)):
        
        if i %3 == 0:
            s += "\n"

        if board[i] == "":
            s += "-"
        else:
            s += board[i]

    print(s)

def choose_initial_player():
    initial = random.randint(0, 1)

    if initial == 0:
        print("Computer starts")
    else:
        print("Player starts")

    return bool(initial)

def player_turn(board, token):

    while True:

        turn = int(input("Choose position:"))
        if turn > 8:
            print("Not a position")
        elif board[turn] != "":
            print("The position is already occupied")
        else:
            board[turn] = token
            return board

def computer_turn(board, token):

    voidPositions = []
    for i in range(len(board)):
        if board[i] == "":
            voidPositions.append(i)
    computerChoice = random.choice(voidPositions)
    board[computerChoice] = token
    return board

def check_winner(board):

    win = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]
    
    for token in set(board):
        if token != "":

            tokenPositions = []
            for i in range(len(board)):
                if board[i] == token:
                    tokenPositions.append(i)
            
            for element in win:
                if set(element).issubset(set(tokenPositions)):
                    return True
                

    return False


isPlayerTurn = choose_initial_player()
draw_board(board)

while check_winner(board) is False:
    
    if isPlayerTurn is True:
        board = player_turn(board, playerToken)

    else:
        board = computer_turn(board, computerToken)

    draw_board(board)  
    isPlayerTurn = not isPlayerTurn 
        
if isPlayerTurn:
    print("Computer wins !!!!!!!")
else:
    print("Player wins !!!!!!")

