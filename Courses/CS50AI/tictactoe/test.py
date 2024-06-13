import math
import copy

X = 'X'
O = 'O'
EMPTY = None

#Get the initial state of the game
def initial_state():
    return [[EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#Determine the turn of the player
def player(board):
    X_Count = sum(row.count(X) for row in board)
    O_Count = sum(row.count(O) for row in board)

    if X_Count > O_Count:
        return O
    else:
        return X

#Look for all possible actions in the game
def actions(board):

    moves = set()
    for i, row in enumerate(board):
        for j,cell in enumerate(row):
            if cell != X and cell != O:
                moves.add((i,j))
    return moves

#Get the result after making an action to the state
def result(board, action):

    if action not in actions(board):
        raise Exception("Invalid Moves")

    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

#Check whether terminal stage is gained or not
def terminal(board):
    if winner(board):
        return True
    elif sum(row.count(EMPTY) for row in board) == 0:
        return True
    else:
        return False
    
#Check whether we have a winner in the game or not
def winner(board):
    for row in board:
        if all(cell == row[0] and cell is not None for cell in row):
            return row[0]
    
    #Checking vertically
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] is not None for row in range(3)):
            return board[0][col]
    

    #Checking diagonally
    if all(board[i][i] == board[0][0] and board[0][0] is not None for i in range(3)):
        return board[0][0]
    
    if all(board[i][2-i] == board[0][2] and board[0][2] is not None for i in range(3)):
        return board[0][2]

    return None 

#Return the utility of the function so as to implement the minimax algorithm
def utility(board):
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


#Implement the mininmax algorithm to get the best move for computer player

def max_value(state):
    v = -math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    v = math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v


#Main minimax logic here
def minimax(board):
    
    if terminal(board):
        return None
    
    current_player = player(board)
    best_move = None

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            val = min_value(result(board, action))
            if val > v:
                v = val
                best_move = action                
    else:
        v = math.inf
        for action in actions(board):
            val = max_value(result(board, action))
            if val < v:
                v = val
                best_move = action                
    
    return best_move