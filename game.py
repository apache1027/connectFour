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

    #Takes the current player tile and searches the board for 4 in a row
    def victory_test(self, cur_name):
        #check horizontal
        for x in range (self.height):
            for y in range (self.width - 3):
                if self.board[x][y] == self.player and self.board[x][y+1] == self.player and self.board[x][y+2] == self.player and self.board[x][y+3] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return True
        #check vertical
        for x in range (self.height - 3):
            for y in range (self.width):
                if self.board[x][y] == self.player and self.board[x + 1][y] == self.player and self.board[x + 2][y] == self.player and self.board[x + 3][y] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return True
        #check forward diagonal \
        for x in range (self.height - 3):
            for y in range (self.width - 3):
                if self.board[x][y] == self.player and self.board[x + 1][y + 1] == self.player and self.board[x + 2][y + 2] == self.player and self.board[x + 3][y + 3] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return True
        #check back diagonal /
        print '\n'
        for x in range (self.height - 3):
            for y in range (3, self.width):
                if self.board[x][y] == self.player and self.board[x + 1][y - 1] == self.player and self.board[x + 2][y - 2] == self.player and self.board[x + 3][y - 3] == self.player:
                    self.print_board()
                    print '\n' ,cur_name, "player wins!"
                    return True
                
        return False

board = Board()
board.print_board()
