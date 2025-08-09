import random
import time

board0 = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
                        ]
board_ = [row[:] for row in board0]

probBoard = [0,0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,6,6]

think_depth = 5  # Depth for the minimax-like algorithm
row_n = len(board0)
col_n = len(board0[0])
dir = [[1,0], [1,1], [0,1], [-1,1],
       [-1,0], [-1,-1],[0,-1], [1,-1]]

debug = False
benchMarking = False

# Function to check if there is a winning condition on the board
def isWin(board, side):
    for c in range(col_n):
        for r in range(row_n):
            for i in range(len(dir)):
                conn4 = True
                for step in range(4):
                    cc = c + dir[i][0] * step
                    rr = r + dir[i][1] * step
                    if (cc not in range(0, col_n)) or (rr not in range(0, row_n)) or board[rr][cc]!=side:
                        conn4 = False
                        break
                if conn4:
                    return True
    return False

def isDraw(board):
    for i in range(len(board[0])):
        if board[0][i] == 0:
            return False
    return True


def drop(board, col, side):
    if not legal(board, col):
        return False
    for i in range(len(board)-1, -1, -1):
        if board[i][col] == 0:
            board[i][col] = side
            return True


def legal(board, col):
    if board[0][col] == 0:
        return True
    return False


def retrieve(board, col):
    for i in range(len(board)):
        if board[i][col] != 0:
            board[i][col] = 0
            return
        if board[5][col] == 0:
            return

def printBoard(board):
    print("\n")
    print(" 0  1  2  3  4  5  6 ")
    print("---------------------")
    for row in board:
        for col in row:
            if col == 0:
                print(" . ", end="")
            elif col == 1:
                print(" X ", end="")
            elif col == 2:
                print(" O ", end="")
        print("\n")


def PvE(board):
    while True:
        printBoard(board)
        dropInput = int(input("Player 1 drop a piece (0-6): "))
        while legal(board, dropInput) == False:
            print("\n"+"Illegal Move! Try again."+"\n")
            dropInput = int(input("Player 1 drop a piece (0-6): "))
        drop(board, dropInput, 1)
        printBoard(board)        
        if isWin(board, 1):
            printBoard(board)
            print("Player 1 wins!")
            return
        before = time.time()
        aiPlayer(board, 2 if debug else 5, 2)
        print("Time used: " + str(time.time() - before) + " s")
        if isWin(board, 2):
            printBoard(board)
            print("Player 2 wins!")
            return
        if isDraw(board):
            printBoard(board)
            print("Draw game!")
            return

# def evaluate(side):
#     swarm_score = 0
#     intconc_score = 0
#     for i in range(len(board0)):


steps = 0
def minimax(board, depth, player):
    board = [row[:] for row in board]  # Create a copy of the board
    global steps
    ratings = [0,0,0,0,0,0,0]
    if depth > 0:
        steps += 1
        for i in range(len(board[0])):
            if board[0][i] == 0:
                drop(board, i, player)
                if isWin(board, player):
                    ratings[i] = 1
                else:
                    ratings[i] = -minimax(board, depth-1, 3-player)[0]
                retrieve(board, i)
            else:
                ratings[i] = float('-inf')
        if debug:
                print("Depth:", depth, "Player:", player,"Score & Index:",max(ratings), ratings.index(max(ratings)), ratings)
                printBoard(board)
        return max(ratings), ratings.index(max(ratings)), ratings
    else:
        steps += 1
        return 0, 0, ratings
    
def aiPlayer(board, depth, side):
    value, index, ratings = minimax(board, depth, side)
    if all(item == 0 for item in ratings):
        r = random.randint(0, len(probBoard)-1)
        drop(board, probBoard[r], side)
    else:
        drop(board, index, side)
    
    return str(r) if all(item == 0 for item in ratings) else str(index), \
        "You are Winning." if max(ratings) == -1 else "You are Losing." if max(ratings) == 1 else "Your Turn..."


if __name__ == '__main__':
    PvE(board0)






