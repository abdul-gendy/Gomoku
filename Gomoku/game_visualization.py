
class gomoku_ascii_visualizer:
    """
    This is a class that shows the state and progression of the gomoku game
    through ASCII graphics.

    Attributes:
        board_size (int): Size of board N, to create a N x N board
    """
    def __init__(self, board_size):
        """
        The constructor for gomoku_ascii_visualizer class.
        
        Parameters:
            board_size (int): Size of board N, to create a N x N board
        """
        self.board_size = board_size
        
    def print_header(self):
        """
        prints the header of the gomoku board which outlines
        the column numbers and game details
        """
        print(" === === === === === Gomoku 1vs1  === === === === === === ===\n")
        header = "  "
        for j in range(self.board_size):
            header += " " + str(j).zfill(2)
        header += "     X = Player1 , O = Player2"
        print(header)
    
    def print_footer(self):
        """
        prints the footer of the gomoku board which outlines
        the column numbers
        """
        footer = "  "
        for j in range(self.board_size):
            footer += " " + str(j).zfill(2)
        print(footer)

    def print_body(self, current_board):
        """
        print the body of the gomoku board which are all the 
        coordinates on the board and the pieces occupying them
        
        Parameters:
            current_board (dict): 2D array containing the states of all positions on the board
        """
        for i in range(0, self.board_size):
            row = current_board[i]
            row_string = str(i).zfill(2) + " "
            for column_value in row:
                row_string += str(column_value) + "  "
            row_string += str(i).zfill(2)
            print(row_string)

    def show_current_board(self, current_board):
        """
        Entry point function for displaying a gomoku board in ascii characters
        
        Parameters:
            current_board (dict): 2D array containing the states of all positions on the board
        """
        self.print_header()
        self.print_body(current_board)
        self.print_footer()





