"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_Count = sum(row.count(X) for row in board)
    O_Count = sum(row.count(O) for row in board)
    
    if(X_Count > O_Count):
        return O
    else: 
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell != X and cell != O:
                moves.add((i,j))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    
    if action not in actions(board):
        raise Exception("Move not available")
    else:
        turn = player(board_copy)
        board_copy[action[0]][action[1]] = turn
    
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Checking horizontally
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

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif sum(row.count(EMPTY) for row in board) == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    best_move = None

    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move