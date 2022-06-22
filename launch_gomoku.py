import argparse
from Gomoku import gomoku_setup

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Arguments needed to run a 2 player gomoku game')
    parser.add_argument('-b', '--board_size', required=True, type=int, 
                        help='The nxn board size needed')
    parser.add_argument('-c', '--connections_to_win', required=True, type=int,
                         help='number of vertical/horizontal/diagonal connections needed to win')
    parser.add_argument('-t', '--time_limit', required=True, type=int,
                         help='time limit in seconds for a player to make a play')
    args = parser.parse_args()

    board_size = int(args.board_size)    
    connections_to_win = int(args.connections_to_win)
    time_limit = int(args.time_limit)
    game = gomoku_setup(board_size, connections_to_win, time_limit)  
    game.play_game()