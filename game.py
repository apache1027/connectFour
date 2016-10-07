import time
from node import Node
from random import randint
import copy
"""
class Node(object):
    def __init__(self, depth, player, board, turn, move, is_root):
        self.depth = depth
        self.player = player
        self.board = board
        self.turn = turn
        self.is_root = is_root
        self.move = move
        if(self.board.victory_test(self.player)):
            self.value = turn * 512 
        else:
            self.value = board.board_eval(self.player, self.turn)
        self.children = []

    def create_children(self):
        if self.depth > 0:
            moves = self.board.possible_moves()
            for move in moves:
                temp_move = move
                temp_board = copy.deepcopy(self.board)
                temp_depth = self.depth-1
                if(not self.is_root):
                    temp_turn = self.turn * -1
                    if (self.player == 'R'):
                        temp_player = 'B'
                    else:
                        temp_player = 'R'
                else:
                    temp_turn = self.turn
                    temp_player = self.player
                temp_board.update_board(temp_player, move)
                self.children.append(Node(temp_depth, temp_player, temp_board, temp_turn, temp_move, False))

            #sort children for min and max nodes to speed up alpha beta
            if(self.turn == -1):
                self.children.sort(key = lambda x: x.value)
            else:
                self.children.sort(key = lambda x: x.value, reverse=True)


    def test_print(self):
        print "++++++++++++++++++++++++++++++++++++++++\n"
        self.board.print_board()
        print "depth = %d; player = %s; turn = %d; value = %d; Move = %d\n"%(self.depth, self.player, self.turn, self.value, self.move)
        print "----------------------------------------\n"

    def alphabeta(self, a, b, max_player):
        if (self.depth == 0):
            return self.value
        if(len(self.children) == 0):
            if(self.value != 512 * self.turn):
                self.create_children()
            else:
                return self.value
        if (self.player == max_player):
            v = -1000000
            for child in self.children:
                v = max(v, child.alphabeta(a, b, max_player))
                a = max(a, v)
                if b <= a:
                    break
            self.value = v
            return v
        else:
            v = 1000000
            for child in self.children:
                v = min(v, child.alphabeta(a, b, max_player))
                b = min(b, v)
                if(b <= a):
                    break
            self.value = v
            return v
"""
class Board(object):
    def __init__(self):
        #self explanatory fields and intilize board
        self.board = []
        self.height = 6
        self.width = 7
        self.cur_row = []
        for row in range(self.height):
            self.board.append([])
            for column in range(self.width):
                self.board[row].append('*')
        for x in range(self.width):
            self.cur_row.append(self.height - 1)

    #prints board nice and pretty
    def print_board(self):
        for row in self.board:
            print " ".join(row)
        for i in range(1, self.width + 1):
            print i,
        print '\n'

    #Takes the current player tile and searches the board for 4 in a row
    def victory_test(self, cur_name):
        #check horizontal
        for x in range (self.height):
            for y in range (self.width - 3):
                if self.board[x][y] == cur_name and self.board[x][y+1] == cur_name and self.board[x][y+2] == cur_name and self.board[x][y+3] == cur_name:
                    return True
        #check vertical
        for x in range (self.height - 3):
            for y in range (self.width):
                if self.board[x][y] == cur_name and self.board[x + 1][y] == cur_name and self.board[x + 2][y] == cur_name and self.board[x + 3][y] == cur_name:
                    return True 
        #check forward diagonal \
        for x in range (self.height - 3):
            for y in range (self.width - 3):
                if self.board[x][y] == cur_name and self.board[x + 1][y + 1] == cur_name and self.board[x + 2][y + 2] == cur_name and self.board[x + 3][y + 3] == cur_name:
                    return True
        #check back diagonal /
        for x in range (self.height - 3):
            for y in range (3, self.width):
                if self.board[x][y] == cur_name and self.board[x + 1][y - 1] == cur_name and self.board[x + 2][y - 2] == cur_name and self.board[x + 3][y - 3] == cur_name:
                    return True
        return False



    def board_eval(self, maxp, minp):
        score = 0
        #check horizontal
        for x in range (self.height):
            for y in range (self.width - 3):
                temp = []
                temp.append(self.board[x][y])
                temp.append(self.board[x][y+1])
                temp.append(self.board[x][y+2])
                temp.append(self.board[x][y+3])
                score += self.eval_helper(temp, maxp, minp)               
        #check vertical
        for x in range (self.height - 3):
            for y in range (self.width):
 		temp = []
                temp.append(self.board[x][y])
                temp.append(self.board[x+1][y])
                temp.append(self.board[x+2][y])
                temp.append(self.board[x+3][y])
		score += self.eval_helper(temp, maxp, minp)
                
        #check forward diagonal \
        for x in range (self.height - 3):
            for y in range (self.width - 3):
 		temp = []
                temp.append(self.board[x][y])
                temp.append(self.board[x+1][y+1])
                temp.append(self.board[x+2][y+1])
                temp.append(self.board[x+3][y+1])
		score += self.eval_helper(temp, maxp, minp)
                
        #check back diagonal /
        for x in range (self.height - 3):
            for y in range (3, self.width):
 		temp = []
                temp.append(self.board[x][y])
                temp.append(self.board[x+1][y-1])
                temp.append(self.board[x+2][y-2])
                temp.append(self.board[x+3][y-3])
		score += self.eval_helper(temp, maxp, minp)
        return score
                
    def eval_helper(self, data, maxp, minp):
	min_count = 0
	max_count = 0
        if(len(data) == 0):
            return 0
        for x in data:
            if(x == maxp):
                max_count += 1
            elif(x != '*'):
                min_count += 1
        if(max_count == 0):
            if(min_count == 3):
                return -50 
            elif(min_count == 2):
                return -10 
            elif(min_count == 1):
                return -1  
            else:
                return 0
        elif(min_count == 0):
            if(max_count == 3):
                return 50
            if(max_count == 2):
                return 10
            if (max_count == 1):
                return 1
        return 0

    #return true if board is full
    def tie_test(self):
        for x in self.cur_row:
            if(x > -1):
                return False
        self.print_board()
        print "It's a tie!"
        return True

    #update the board
    def update_board(self, val, move):
        self.board[self.cur_row[move]][move] = val
        self.cur_row[move] = self.cur_row[move]-1

    #returns list of possible moves (standard game would be int 0-6)
    def possible_moves(self):
        temp = []
        counter = 0
        for x in self.cur_row:
            if (x > -1):
                temp.append(counter)
            counter += 1
        return temp

#will make sure the user inputs a valid move
def check_move(user_move):
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

#human turn
def human_turn(board, human, human_name):
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
#human turn
def computer_turn(board, human, human_name, depth):
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

