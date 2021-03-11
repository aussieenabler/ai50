"""
Tic Tac Toe Player
""" 

import math
import copy
from random import choice

X = "X"
O = "O"
EMPTY = None

move = ()

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    player_x = 0
    player_o = 0

    # If first move player X's turn
    if board == initial_state():
        return X

    # If not first move, if player X has more moves than playr O. Player O's turn
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    player_x += 1
                elif board[i][j] == O:
                    player_o += 1
        
        if player_x > player_o:
            return O

        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action = set()

    # If cell == EMPTY record in action and return as set.
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Save copy of current board state
    board_copy = copy.deepcopy(board)

    # Ensure action is valid
    if board_copy[action[0]][action[1]] != EMPTY:
        print(f"result {action}")
        raise NameError('Invalid action')
    
    # Update board with token
    else:
        board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    token = X

    if player(board) == X:
        token = O

    # Horizontal loop check
    for i in range(3):
        x = 0
        for j in range(3):
            if board[i][j] == token:
                x += 1
            if x == 3:
                return token

    # Vertican loop check
    for i in range(3):
        x = 0
        for j in range(3):
            if board[j][i] == token:
                x += 1
            if x == 3:
                return token
    
    # Diagonal loop check
  
    i = 0
    for j in range(3):
        x = 0
        if board[i][j] == token:
            x += 1
            i += 1
        if x == 3:
            return token
    
    i = 2
    x = 0
    for y in range(3):
        if board[i][y] == token:
            x += 1
            i -= 1
        if x == 3:
            return token

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # If no winner and any cell contains EMPTY, game is not over
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False

    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global move

    inf = float('inf')
    neg_inf = float('-inf')
    
    if board == initial_state():
        first_move = [(0, 0), (0, 2), (2, 0), (2, 2)]
        return random.choice(first_move)

    if player(board) == X:
        for action in actions(board):
            v = min_value(result(board, action))

            if v > neg_inf:
                neg_inf = v
                move = action

        return move
    else:
        for action in actions(board):
            v = max_value(result(board, action))

            if v < inf:
                inf = v
                move = action
        return move

def min_value(board):

    if terminal(board):
        return utility(board)

    v = float('inf')
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v

def max_value(board):

    if terminal(board):
        return utility(board)

    v = float('-inf')

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v
