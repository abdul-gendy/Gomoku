
class board_analyzer:
    """
    This is a class that analyzes the gomoku board to check for
    invalid plays, or to check for a winner or any other tasks
    that require analyzing the board

    Attributes:
        board_size (int): Size of board N, to create a N x N board
        connections_to_win (int): Number of vertical/horizontal/diagonal connections needed to win
    """
    def __init__(self, board_size, connections_to_win):
        """
        The constructor for board_analyzer class.

        Parameters:
            board_size (int): Size of board N, to create a NxN board
            connections_to_win (int): Number of vertical/horizontal/diagonal connections needed to win
        """
        self.board_size = board_size
        self.connections_to_win = connections_to_win
        
    def in_bounds(self, row, col):
        """
        Check if a given (row,col) coordinate is within bounds on the board
  
        Parameters: 
            row (int): row coordinate on the board
            col (int): col coordinate on the board
          
        Returns:
            (bool): whether or not the coordinate is within bounds
        """
        if ((0 <= row < self.board_size) and (0 <= col < self.board_size)):
            return True
        else:
            return False

    def check_position_available(self, desired_play, current_board):
        """
        given a position [x,y] of the board, returns if its occupied or not
  
        Parameters: 
            desired_play: (row, col) tuple containing the desired coordinate on the board
            current_board: 2D array containing current status of all positions on the board
          
        Returns:
            (bool): whether or not the coordinate is already occupied
        """
        row = desired_play[0]
        col = desired_play[1]
        position_value = current_board[row][col]
        if position_value != ".":
            return False
        else:
            return True

    def check_for_winner(self, latest_play, current_board):
        """
        Checks the board to search for a winner after the latest play
  
        Parameters: 
            latest_play: (row, col) tuple containing the coordinate of the latest play
            current_board: 2D array containing current status of all positions on the board
        
        Returns:
            (bool): whether or not a winner has been found
        """
        latest_row = latest_play[0]
        latest_col = latest_play[1]
        last_letter = current_board[latest_row][latest_col]

        # [r, c] direction, matching letter count, locked bool
        directions = [[(-1, 0), 0, True], 
                      [(1, 0), 0, True], 
                      [(0, -1), 0, True],
                      [(0, 1), 0, True],
                      [(-1, -1), 0, True],
                      [(1, 1), 0, True],
                      [(-1, 1), 0, True],
                      [(1, -1), 0, True]]
        
        # Search outwards looking for matching pieces
        for i in range(self.connections_to_win):
            for d in directions:
                r = latest_row + (d[0][0] * (i+1))
                c = latest_col + (d[0][1] * (i+1))

                if d[2] and self.in_bounds(r, c) and current_board[r][c] == last_letter:
                    d[1] += 1
                else:
                    # Stop searching in this direction
                    d[2] = False

        # Check possible direction pairs for '5 pieces in a row'
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= (self.connections_to_win - 1)):
                return True
        # Did not find any winners
        return False
