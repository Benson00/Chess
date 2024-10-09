import copy
import math
from Board import Board
from player import Player


   
'''

        Alpha-beta pruning pseudo-code

        FUNZIONE alfa_beta(nodo, profondità, α, β, chi_gioca)
02      SE profondità = 0 O nodo è terminale
03          RESTITUISCI valore euristico del nodo
04      SE chi_gioca = MAX
05          v := -∞
06          PER OGNI figlio del nodo
07              v := max(v, alfa_beta(figlio, profondità - 1, α, β, MIN))
08              α := max(α, v)
09              SE β ≤ α
10                  INTERROMPI IL CICLO (* taglio secondo β *)
11          RESTITUISCI v
12      ALTRIMENTI SE chi_gioca = MIN
13          v := +∞
14          PER OGNI figlio del nodo
15              v := min(v, alfa_beta(figlio, profondità - 1, α, β, MAX))
16              β := min(β, v)
17              SE β ≤ α
18                  INTERROMPI IL CICLO (* taglio secondo α *)
19          RESTITUISCI v


(* richiamo iniziale *)
alfa_beta(origine, profondità, -∞, +∞, MAX)

'''


class minimaxPlayer(Player):
    
    
    def __init__(self,color, depth = 3):
        """
        Initialize an AI Player.

        :param color: 'white' or 'black'
        :param depth: Depth of the Minimax search tree
        """
        super().__init__(color)
        self.depth = depth

    def get_move(self,board:Board):
        """
        Determine the best move using Minimax algorithm with alpha-beta pruning.

        :param board: Current state of the board
        :return: Tuple of start and end positions ((start_row, start_col), (end_row, end_col))
        """
        best_move = None
        # if agent's color is white play as Max, otherwhise as Min
        best_score = -math.inf if self.color == 'white' else math.inf   

        for row in range(8):
            for col in range(8):
                piece = board.grid[row][col]
                if piece and piece.color == self.color:
                    possible_moves = piece.get_moves(board.grid, row, col)
                
                temp_board = copy.deepcopy(board)




     