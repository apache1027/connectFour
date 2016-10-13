import time
from random import randint
from board import Board
from node import Node

def check_move(user_move):
    """Checks a move to make sure it's valid.
    
    Ensures that the move is an int and that it is valid with the
    current board. 
    
    Args:
        user_move(int): The column the player wants to move in.

    """
    try:
        user_move = int(user_move)
    except ValueError:
        return False
    else:
        if(user_move < 1 or user_move > board.width):
            return False
        if(board.cur_row[user_move - 1] < 0):
            return False
    return True

def human_turn(board, human, human_name):
    """Gets human turn from user.
    
    Prompts the human player to enter the desired column. This move is
    checked for validity and added to the board. 

    Args:
        board(Board): Current game board 
        human(char): The char representing the player
        human_name(string): "Black" or "Red"

    """
    board.print_board()
    #user_move = randint(1,7)
    user_move = raw_input("%s player, enter a number between 1 and %d: " %(human_name, board.width))
    while(not check_move(user_move)):
        user_move = raw_input("%s player, enter a number between 1 and %d: " %(human_name, board.width))
    user_move = int(user_move)
    board.update_board(human, user_move-1)



def computer_turn(board, comp, time):
    """Makes comuter move.
    
    Calculates the best move for the computer and updates the board. Also
    outputs the time the calculation takes to complete. Once the value
    is passed back from the AI function, the root node picks the move
    associated with the child that has that value.

    Args:
        board(Board): Current game board
        comp(char): the char representing the player
        depth(int): The depth that the search algorithm will run to
    
    """
    depth = 0
    move = -1
    board.print_board()
    time1 = time.time()
    if (comp == 'R'):
        oth = 'B'
    else:
        oth = 'R'
    while(True):
        depth += 1
        root = Node(board, depth, comp, 0, 0, comp, oth)
        val = root.alphabeta(-1000000, 1000000, comp, time1, time)
    time2 = time.time()
    print "Search took %0.3f s" %(time2 - time1)
    #printyy(root)
    for child in root.children:
        if(child.value == val):
            move = child.move
            break
    board.update_board(comp, move)
    move+=1
    print "Computer chose column %d" %move


def printyy(node):
    """Test print function"""
    node.test_print2()
    for child in node.children:
        printyy(child)



board = Board()
turn = 'R'
turn_name = "Red"
cont = True

#get user input for who goes first
#set human and computer to respective value
temp = 'a'
while (temp != 'c' and temp != 'h'):
    temp = raw_input("Will the (c)omputer or the (h)uman go first?: ")
if(temp == 'c'):
    computer = 'R'
    human = 'B'
else:
    computer = 'B'
    human = 'R'

#get user input for search depth
test = True
while(test):
    temp = raw_input("Enter the search depth: ")
    try:
        int(temp)
    except ValueError:
        test = True
    else:
        temp = int(temp)
        test = False
depth = temp


#loop until there is a winner
while (cont):
    if(turn == computer):
        computer_turn(board, turn, depth)
    else:
        #computer_turn(board, turn, depth)
        human_turn(board, turn, turn_name)
    if(board.victory_test(turn)):
        cont = False
        board.print_board()
        print turn_name, "player wins!"
    if(board.tie_test()):
        cont = False
    if(turn == 'B'):
        turn = 'R'
        turn_name = "Red"
    else:
        turn = 'B'
        turn_name = "Black"
