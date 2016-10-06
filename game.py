class Node(object):
    def __init__(self):
        
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
    def victory_test(self, cur_name, cur_title):
        #check horizontal
        for x in range (self.height):
            for y in range (self.width - 3):
                if self.board[x][y] == cur_name and self.board[x][y+1] == cur_name and self.board[x][y+2] == cur_name and self.board[x][y+3] == cur_name:
                    self.print_board()
                    print cur_title, "player wins!"
                    return True
        #check vertical
        for x in range (self.height - 3):
            for y in range (self.width):
                if self.board[x][y] == cur_name and self.board[x + 1][y] == cur_name and self.board[x + 2][y] == cur_name and self.board[x + 3][y] == cur_name:
                    self.print_board()
                    print cur_title, "player wins!"
                    return True
        #check forward diagonal \
        for x in range (self.height - 3):
            for y in range (self.width - 3):
                if self.board[x][y] == cur_name and self.board[x + 1][y + 1] == cur_name and self.board[x + 2][y + 2] == cur_name and self.board[x + 3][y + 3] == cur_name:
                    self.print_board()
                    print cur_title, "player wins!"
                    return True
        #check back diagonal /
        for x in range (self.height - 3):
            for y in range (3, self.width):
                if self.board[x][y] == cur_name and self.board[x + 1][y - 1] == cur_name and self.board[x + 2][y - 2] == cur_name and self.board[x + 3][y - 3] == cur_name:
                    self.print_board()
                    print cur_title, "player wins!"
                    return True
        return False

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
    board.update_board(human, user_move-1)


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
        human_turn(board, turn, turn_name)
    else:
        human_turn(board, turn, turn_name)
    if(board.victory_test(turn, turn_name)):
        cont = False
    if(turn == 'B'):
        turn = 'R'
        turn_name = "Red"
    else:
        turn = 'B'
        turn_name = "Black"

