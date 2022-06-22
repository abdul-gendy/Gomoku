# Gomoku
Implementation of a two-player Freestyle Gomoku using only the Python standard library.

### Setup
Only python version 3.8 is required to run this game.

### Usage
##### Running Gomoku
```
python launch_gomoku.py -b BOARD_SIZE -c CONNECTIONS_TO_WIN -t TIME_TO_MAKE_MOVE
```    
Arguments needed:
  - BOARD_SIZE (int): Size of board N, to create a N x N board
  - CONNECTIONS_TO_WIN (int): Number of vertical/horizontal/diagonal connections needed to win
  - TIME_TO_MAKE_MOVE (int): Number of seconds given for a player to make a move

##### Sample Output
```
python launch_gomoku.py -b 15 -c 5 -t 30
```
<p align="center">
  <img src="images\Capture1.PNG" alt="alt text" width="610" height="600">
</p>

<p align="center">
  <img src="images\Capture.PNG" alt="alt text" width="610" height="350">
</p>

