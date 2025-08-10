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

board1 = [
        [0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,2,1,0,0],
        [0,1,2,2,2,1,0]
                        ]

board_ = [row[:] for row in board0]

probBoard = [0,0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,6,6]
def randomize(o):
    o.append(3)
    if random.random() <0.5:
        o.append(2)
        o.append(4)
    else:
        o.append(4)
        o.append(2)
    if random.random() <0.5:
        o.append(1)
        o.append(5)
    else:
        o.append(5)
        o.append(1)
    if random.random() <0.5:
        o.append(0)
        o.append(6)
    else:
        o.append(6)
        o.append(0)
    return o

row_n = len(board0)
col_n = len(board0[0])

debug = False

# Function to check if there is a winning condition on the board
def isWin(board, side):
    for r in range(row_n):
        for c in range(col_n - 3):
            if board[r][c] == side and board[r][c+1] == side and board[r][c+2] == side and board[r][c+3] == side:
                return True
    for c in range(col_n):
        for r in range(row_n - 3):
            if board[r][c] == side and board[r+1][c] == side and board[r+2][c] == side and board[r+3][c] == side:
                return True
    for r in range(row_n - 3):
        for c in range(col_n - 3):
            if board[r][c] == side and board[r+1][c+1] == side and board[r+2][c+2] == side and board[r+3][c+3] == side:
                return True
    for r in range(3, row_n):
        for c in range(col_n - 3):
            if board[r][c] == side and board[r-1][c+1] == side and board[r-2][c+2] == side and board[r-3][c+3] == side:
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


count = 0
def PvE(board):
    global count
    while True:
        printBoard(board)
        dropInput = int(input("Player 1 drop a piece (0-6): "))
        while legal(board, dropInput) == False:
            print("\n"+"Illegal Move! Try again."+"\n")
            dropInput = int(input("Player 1 drop a piece (0-6): "))
        drop(board, dropInput, 1)
        count += 1
        printBoard(board)        
        if isWin(board, 1):
            printBoard(board)
            print("Player 1 wins!")
            return
        before = time.time()
        count += 1
        aiPlayer(board, 2 if debug else 8, 2)
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

# def skewedChoice(l):
#     leng = len(l) // 2 
#     offset = round((random.random() ** 2) * leng)
#     if random.random() < 0.5:
#         return leng - offset
#     else:
#         return leng + offset

def betterMax(l):
    pick1 = []
    pick2 = []
    for i in range(len(l)):
        if l[i] is not None:
            pick1.append(i)
            pick2.append(l[i])
    m = max(pick2)
    return m, pick1, pick2

def randMax(l):
    p1 = betterMax(l)[1]
    m = betterMax(l)[0]
    newL = []
    for i in p1:
        if l[i] == m:
            newL.append(i)
    return random.choice(newL)

now = time.time()
steps = 0
def minimax(board, depth, player, alpha=float('-inf')):
    global steps
    ratings = [0,0,0,0,0,0,0]
    depths = [0,0,0,0,0,0,0]
    max = float('-inf')
    if depth > 0:
        order = []
        randomOrder = randomize(order)
        for i in randomOrder:
            if board[0][i] == 0:
                drop(board, i, player)
                if isWin(board, player):
                    ratings[i] = 1
                else:
                    ratings[i] = -minimax(board, depth-1, 3-player, max)[0]
                retrieve(board, i)
                if ratings[i] > max:
                    max = ratings[i]
                    if -max < alpha:
                        return max, i, ratings
            else:
                ratings[i] = None
        if debug:
                print("Depth:", depth, "Player:", player,"Score & Index:",
                      max(ratings), ratings.index(max(ratings)), ratings)
                printBoard(board)
        sel = randMax(ratings)
        return ratings[sel], sel, ratings
    else:
        steps += 1
        return 0, 0, ratings

def aiPlayer(board, depth, side):
    value, index, ratings = minimax(board, 4, side)
    if count < 5 or 1 in ratings:
        drop(board, index, side)
        print(str(ratings)+"\n"+"AI Shallow-Thinking"+"("+str(4)+")")
    else:
        value, index, ratings = minimax(board, depth, side)
        drop(board, index, side)
        print(str(ratings)+"\n"+"AI Deep-Thinking"+"("+str(depth)+")")
    return str(index), "You are Winning." if betterMax(ratings)[0] == -1 else "You are Losing." if betterMax(ratings)[0] == 1 else "Your Turn..."
   
    # for i in range(len(ratings)):
    #     if 1 not in ratings and -1 not in ratings and ratings[i] == float('-inf'):
    #         for j in range(len(probBoard)-1, -1, -1):
    #             if probBoard[j] == i:
    #                 probBoard.pop(j)
    #         t = random.randint(0, len(probBoard)-1)
    #         drop(board, probBoard[t], side)
    #         return str(probBoard[t]), "You are Winning." if max(ratings) == -1 else "You are Losing." if max(ratings) == 1 else "Your Turn..."
    # if all(item == 0 for item in ratings):
    #     r = random.randint(0, len(probBoard)-1)
    #     drop(board, probBoard[r], side)
    #     return str(probBoard[r]), "You are Winning." if max(ratings) == -1 else "You are Losing." if max(ratings) == 1 else "Your Turn..."
    # else:


if __name__ == '__main__':
    # PvE(board0)
    minimax(board1, 8, 1)
    print(steps)
    print(str(time.time()-now)+"s")



