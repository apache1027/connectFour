class Board(object):
    def __init__(self):
        #self explanatory fields and intilize board
        self.board = []
        self.player = 'R'
        self.height = 6
        self.width = 7
        temp = 'a'
        while (temp != 'c' and temp != 'h'):
            temp = raw_input("Will the (c)omputer or the (h)uman go first?: ")
        if(temp == 'c'):
            self.computer = 'R'
        else:
            self.computer = 'B'
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
        self.depth = temp
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

    #makes the move for the player
    def move(self):
        self.print_board()
        #set string to proper name
        cur_player = self.player
        if self.player == 'R':
            cur_name = "Red"
        else:
            cur_name = "Black"
        print '\n',cur_name, "player, enter a number between 1 and" ,self.width, ":"
        user_move = raw_input()
        #loop until valid move
        while (not self.check_move(user_move)):
            user_move = raw_input("Invalid input, please try again: ")
        user_move = int(user_move)
        #update the board with the correct tile
        self.board[self.cur_row[user_move - 1]][user_move - 1] = cur_player
        self.cur_row[user_move - 1] = self.cur_row[user_move - 1] - 1
        #will be FALSE if there is a winner to break loop
        victory = self.victory_test(cur_name)
        #update turn
        if self.player == 'R':
            self.player = 'B'
        else:
            self.player = 'R'
        return victory

    #will make sure the user inputs a valid move
    def check_move(self, user_move):
        try:
            user_move = int(user_move)
        except ValueError:
            return False
        else:
            if(user_move < 1 or user_move > self.width):
                return False
            if(self.cur_row[user_move - 1] < 0):
                return False
        return True

    #Takes the current player tile and searches the board for 4 in a row
    def victory_test(self, cur_name):
        #WILL RETURN FALSE IF THERE IS A WINNER
        #check horizontal
        for x in range (self.height):
            for y in range (self.width - 3):
                if self.board[x][y] == self.player and self.board[x][y+1] == self.player and self.board[x][y+2] == self.player and self.board[x][y+3] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return False
        #check vertical
        for x in range (self.height - 3):
            for y in range (self.width):
                if self.board[x][y] == self.player and self.board[x + 1][y] == self.player and self.board[x + 2][y] == self.player and self.board[x + 3][y] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return False
        #check forward diagonal \
        for x in range (self.height - 3):
            for y in range (self.width - 3):
                if self.board[x][y] == self.player and self.board[x + 1][y + 1] == self.player and self.board[x + 2][y + 2] == self.player and self.board[x + 3][y + 3] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return False
        #check back diagonal /
        print '\n'
        for x in range (self.height - 3):
            for y in range (3, self.width):
                if self.board[x][y] == self.player and self.board[x + 1][y - 1] == self.player and self.board[x + 2][y - 2] == self.player and self.board[x + 3][y - 3] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return False
                
        return True


board = Board()
test = True
while(test):
    test = board.move()

