class Board(object):
    """Holds the current game state in a board.

    The current game state is represented by a 2d array that is initialized
    full of '*'; representing a blank space. As the board is updated, the 
    char for the player who made the move is inserted into the column at the
    row that is determined by the cur_row list. 

    Attributes:
        board[[char]]: Holds the current state of the game with '*' for blanks.
        height(int): The set height of the board.
        width(int): The set width of the board.
        cur_row[int]: How many open spots left in each column.

    """
    def __init__(self):
        """Constructor for board.
        
        The board is initilized to be filled with '*' and the 
        cur_row is initilized to height - 1 for each column. 
        Pieces will be inserted in the correct row based on
        the cur_row value.
        
        """
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
        """Prints the current board state nice and pretty.
        
        
        """
        for row in self.board:
            print " ".join(row)
        for i in range(1, self.width + 1):
            print i,
        print '\n'

    #Takes the current player tile and searches the board for 4 in a row
    def victory_test(self, cur_name):
        """Checks if the current player won the game.
        
        
        """
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
        """Calculates a score based on board state.
        
        
        """
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
        """Uses list from board_eval() to assign score.
        
        
        """
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
        """Checks for a full board.
        
        
        """
        for x in self.cur_row:
            if(x > -1):
                return False
        self.print_board()
        print "It's a tie!"
        return True

    #update the board
    def update_board(self, val, move):
        """Updates the board with a move.
        
        
        """
        self.board[self.cur_row[move]][move] = val
        self.cur_row[move] = self.cur_row[move]-1

    #returns list of possible moves (standard game would be int 0-6)
    def possible_moves(self):
        """Calculates all possible moves.
        
        
        """
        temp = []
        counter = 0
        for x in self.cur_row:
            if (x > -1):
                temp.append(counter)
            counter += 1
        return temp

