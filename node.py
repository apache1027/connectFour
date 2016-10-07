import copy

class Node(object):
    """Stores info for the search tree and the AI logic.
    
    Need a paragraph description here...

    Attributes:
        board (Board): The board for the current state
        depth (int): The depth of the tree counting down from root (leaf node == 0)
        turn (int): -1 for minimizing player and +1 for maximizing player
        player(char): Either 'R' or 'B' for current player
        move(int): Column to move into to get the current board state from parent
        value(int): Value assigned to the board by the evaluation function
        children[Node]: List of children of the node
    
    """
    def __init__(self, board, depth, turn, player, move, value):
        """The init function for each node.

        Need a paragraph description here...

        Args:
            board(Board): The board for the current state
            depth(int): The depth of the tree counting down from root (leaf node == 0)
            turn(int): -1 for minimizing player +1 for maximizing player
            player(char): Either 'R' or 'B' for the current player
            move(int): Column to move into to get the current board from parent
            value(int): The fitness of the board based on board evaluation

        """
        self.board = board
        self.depth = depth
        self.turn = turn
        self.player = player
        self.move = move
        self.value = value
        self.children = []

    def create_children(self):
        """Populates the children attribute for each possible board state.
        
        Needs a paragrph description here...
        
        """

        moves = self.board.possible_moves()
        for move in moves:
            temp_move = move
            temp_board = copy.deepcopy(self.board)
            temp_depth = self.depth-1
            temp_turn = self.turn * -1
            temp_board.update_board(self.player, move)
            if(self.player == 'B'):
                temp_player = 'R'
            else:
                temp_player = 'B'
            self.children.append(Node(temp_board, temp_depth, temp_turn, temp_player, temp_move, 0))
        if(self.turn == -1):
            self.children.sort(key = lambda x: x.value)
        else:
            self.children.sort(key = lambda x: x.value)

    def alphabeta(self, a, b, max_player):
        """Uses alpha beta pruning to find the best next move for max player.
        
        Need a paragraph description here...
        
        Args:
            a(int):
            b(int): 
            max_player(char):

        Return:
            value(int): The best choice value for the current player to choose
            
        """
        if (self.depth == 0):
            self.value = self.board.board_eval(self.player, self.turn)
            return self.value
        if(len(self.children) == 0):
            if(self.value != 512 * self.turn):
                self.create_children()
            else:
                return self.value
        if(self.player == max_player):
            v = -1000000
            for child in self.children:
                v = max(v, child.alphabeta(a, b, max_player))
                a = max(a,v)
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

    def test_print(self):
        print "++++++++++++++++++++++++++++++++++++++++\n"
        self.board.print_board()
        print "depth = %d; player = %s; turn = %d; value = %d; Move = %d\n"%(self.depth, self.player, self.turn, self.value, self.move)
        print "----------------------------------------\n"

