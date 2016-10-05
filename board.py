        self.player = 'R'

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


board = Board()
test = True
while(test):
    test = board.move()

