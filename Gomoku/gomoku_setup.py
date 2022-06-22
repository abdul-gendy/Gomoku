from .board_analysis import board_analyzer
from .game_visualization import gomoku_ascii_visualizer

class gomoku_setup:
    """
    This is a class that sets up the gomoku board game and tracks the 
    game events and players 

    Attributes:
        board_size (int): Size of board N, to create a N x N board
        connections_to_win (int): Number of vertical/horizontal/diagonal connections needed to win
        time_limit (int): Number of seconds given for a player to make a move
    """
    def __init__(self, board_size = 15, connections_to_win = 5, time_limit = 0):
        """
        The constructor for gomoku_setup class.
  
        Parameters:
            board_size (int): Size of board N, to create a N x N board
            connections_to_win (int): Number of vertical/horizontal/diagonal connections needed to win
            time_limit (int): Number of seconds given for a player to make a move
        """
        self.time_limit = time_limit
        self.board_size = board_size
        self.connections_to_win = connections_to_win
        self.num_of_plays = 0
        self.current_board = self.init_board()
        self.board_analyzer = board_analyzer(board_size, connections_to_win)
        self.visualizer = gomoku_ascii_visualizer(board_size)

    def init_board(self):
        """
        Sets up the gomoku board before the start of the game
  
        Returns:
            current_board (dict): 2D array containing the states of all positions on the board
        """
        current_board = []
        for i in range(self.board_size):
            #rows
            current_board.append([])                   
            for j in range(self.board_size):
                #columns
                current_board[i].append('.')
        return current_board

    def get_desired_play(self, player):
        """
        Asks selected player to input their desired move
  
        Parameters: 
            player (str): Current player
          
        Returns:
            desired_play: (row, col) tuple containing the desired coordinate on the board
        """
        while True:
            try:
                print("Player " + str(player) + " turn:")
                row = int(input("row: "))
                col = int(input("col: "))
                if self.board_analyzer.in_bounds(row, col):
                    if self.board_analyzer.check_position_available((row, col), self.current_board):
                        return (row,col)
                    else:
                        print("Position is busy, try different coordinates")
                else:        
                    print("Please try again and insert values between 0 and 14")
            except ValueError:
                print('invalid input: make sure you are inputting integers between 0 and 14')
        return []

    def make_play(self, desired_play, current_player):
        """
        Makes the desired move and updates the board
  
        Parameters: 
            desired_play: (row, col) tuple containing the desired coordinate on the board
            current_player (str): player who is currently making the move
        """
        row = desired_play[0]
        col = desired_play[1]
        self.current_board[row][col] = current_player

    def current_turn(self):
        """
        Returns the player whos turn it is to play
        """
        players = ['X', 'O']
        return players[self.num_of_plays % 2]

    def reset_game(self):
        """
        Resets the game and clears the board up for a new game
        """
        self.current_board = self.init_board()
        self.play_game()

    def play_game(self):
        """
        Entry point function for launching the game
        """
        self.visualizer.show_current_board(self.current_board)
        winner_found = False
        while winner_found == False:
            current_player = self.current_turn()
            desired_play = self.get_desired_play(current_player)
            self.make_play(desired_play, current_player)
            self.num_of_plays += 1
            self.visualizer.show_current_board(self.current_board)
            winner_found = self.board_analyzer.check_for_winner(desired_play, self.current_board)   
        print("Player " + current_player + " has won the game !!!\n\n")
        self.reset_game()
