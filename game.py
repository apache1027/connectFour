import time
from board import Board
from node import Node

def check_move(user_move):
    """Checks a move to make sure it's valid.
    
    
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
    
    
    """
    board.print_board()
    user_move = raw_input("%s player, enter a number between 1 and %d: " %(human_name, board.width))
    while(not check_move(user_move)):
        user_move = raw_input("%s player, enter a number between 1 and %d: " %(human_name, board.width))
    user_move = int(user_move)
    #user_move = randint(1,7)
    board.update_board(human, user_move-1)
def printyy(node):
    node.test_print2()
    for child in node.children:
        printyy(child)


def computer_turn(board, human, human_name, depth):
    """Makes comuter move.
    
    
    """
    board.print_board()
    time1 = time.time()
    if (human == 'R'):
        oth = 'B'
    else:
        oth = 'R'
    root = Node(board, depth, human, 0, 0, human, oth)
    move = -1
    val = root.alphabeta(-1000000, 1000000, human)
    time4 = time.time()
    print "Search took %0.3f s" %(time4 - time1)
    #printyy(root)
    for child in root.children:
        if(child.value == val):
            move = child.move
            break
    #if(move == -1 or val == 0):
        #while(not check_move(move)):
            #move = randint(0,6)
    board.update_board(human, move)
    move+=1
    print "Computer chose column %d" %move

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
        computer_turn(board, turn, turn_name, depth)
    else:
        computer_turn(board, turn, turn_name, depth)
        #human_turn(board, turn, turn_name)
    if(board.victory_test(turn)):
        cont = False
        board.print_board()
        print turn_name, "player wins!"
    if(turn == 'B'):
        turn = 'R'
        turn_name = "Red"
    else:
        turn = 'B'
        turn_name = "Black"
