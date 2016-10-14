import copy
import time

class Node(object):
    """Stores info for the search tree and the AI logic.
    
    Each node contains attributes which allow for an alpha beta pruning algorithm to
    play a game of connect 4. The tree is constructed by the alphabeta function
    so as not to waste time buiding a massive tree.

    Attributes:
        board (Board): The board for the current state
        depth (int): The depth of the tree counting down from root (leaf node == 0)
        player(char): Either 'R' or 'B' for current player
        move(int): Column to move into to get the current board state from parent
        value(int): Value assigned to the board by the evaluation function
        max_player(char):
        min_player(char):
        children[Node]: List of children of the node
    
    """
    def __init__(self, board, depth, player, move, value, max_player, min_player):
        """The init function for each node.

        Args:
            board(Board): The board for the current state
            depth(int): The depth of the tree counting down from root (leaf node == 0)
            player(char): Either 'R' or 'B' for the current player
            move(int): Column to move into to get the current board from parent
            value(int): The fitness of the board based on board evaluation
            max_player(cahr): The char for the max player (never changes in the tree)
            min_player(char): The char for the min player (never changes in the tree)

        """
        self.board = board
        self.depth = depth
        self.player = player
        self.move = move
        self.value = value
        self.max_player = max_player
        self.min_player = min_player
        self.children = []

    def create_children(self):
        """Populates the children attribute for each possible board state.
        
        Variables named with temp_ wil be the args passed to the new node init function.
        A copy of the parent's board is used to seed the board for the next node.

        All nodes are assigned a value initially to allow for sorting.
        512 is the value for winning boards for the max player and
        -512 for the min player. If the node is not a winning board a value
        will be assigned based on the board_eval function in the board class.

        The player variable is the player who will make the choice at that node (
        max player for max nodes and min player for min nodes). The children list is then
        sorted by value to allow more aggressive pruning from the alphabeta algorithm.
        Min nodes are sorted lowest to highest and the max nodes are sorted 
        highest to lowest.
        
        """

        moves = self.board.possible_moves()
        for move in moves:
            temp_move = move
            temp_board = copy.deepcopy(self.board)
            temp_depth = self.depth-1
            temp_board.update_board(self.player, move)
            if(temp_board.victory_test(self.player)):
                if(self.player == self.max_player):
                    temp_value = 512
                else:
                    temp_value = -512
            else:
                temp_value = temp_board.board_eval(self.max_player, self.min_player)
            if(self.player == 'B'):
                temp_player = 'R'
            else:
                temp_player = 'B'
            self.children.append(Node(temp_board, temp_depth, temp_player, temp_move, temp_value, self.max_player, self.min_player))
        if(self.player == self.min_player):
            self.children.sort(key = lambda x: x.value)
        else:
            self.children.sort(key = lambda x: x.value, reverse = True)

    def alphabeta(self, a, b, max_player, time1, t_limit):
        """Uses alpha beta pruning to find the best next move for max player.
        
        Standard alphabeta algorithm. The function builds the tree by generating child nodes
        for nodes that are not in a winning condition and nodes that are not at the depth limit.
        1000000 and -1000000 are used as infinity and -infinity.
        
        Args:
            a(int): The current best choice for max from higher in the tree
            b(int): The current best choice for min from higher in the tree
            max_player(char): The char that represents the max player

        Return:
            value(int): The best choice value for the current player to choose
            
        """
        if((time.time() - time1) >= t_limit):
            return None
        if (self.depth == 0):
            return self.value
        if(len(self.children) == 0):
            if(self.value != 512 and self.value != -512):
                self.create_children()
            else:
                return self.value
        if(self.player == max_player):
            v = -1000000
            for child in self.children:
                v = max(v, child.alphabeta(a, b, max_player, time1, t_limit))
                a = max(a,v)
                if((time.time() - time1) >= t_limit):
                    return None
                if b <= a:
                    break
            self.value = v
            return v
        else:
            v = 1000000
            for child in self.children:
                v = min(v, child.alphabeta(a, b, max_player, time1, t_limit))
                b = min(b, v)
                if((time.time() - time1) >= t_limit):
                    return None
                if(b <= a):
                    break
            self.value = v
            return v

    def test_print(self):
        print "++++++++++++++++++++++++++++++++++++++++\n"
        self.board.print_board()
        print "depth = %d; player = %s; value = %d; Move = %d\n"%(self.depth, self.player, self.value, self.move)
        print "----------------------------------------\n"

    def test_print2(self):
        print "%d\t%s\t%d\t%d"%(self.depth, self.player, self.move, self.value)
