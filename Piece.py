class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def get_moves(self, board, row, col):
        return []

class Pawn(Piece):
    def get_type(self):
        return "Pawn"
    
    def get_moves(self, board, row, col):

        """
        Calculate all possible moves for the pawn based on the rules of chess.

        :param board: The chessboard (8x8) with the pieces.
        :param row: The current row of the pawn.
        :param col: The current column of the pawn.
        :return: List of tuples (row, column) representing the possible moves.
        """

        moves = []
        direction = -1 if self.color == "white" else 1  # direction of movement (up white, down black)

        # 1. Standard movement
        if 0 <= row + direction < 8 and board[row + direction][col] is None:    # in board and empty
            moves.append((row + direction, col))
            
            # 2. Two squares movement
            if (self.color == "white" and row == 6) or (self.color == "black" and row == 1):
                if board[row + direction * 2][col] is None:                     # in board and empty
                    moves.append((row + direction * 2, col))

        # 3. Capture 
        for d_col in [-1, 1]:
            new_col = col + d_col
            new_row = row + direction
            if 0 <= new_col < 8 and 0 <= new_row < 8:       # in board
                target_piece = board[new_row][new_col]
                if target_piece is not None and target_piece.get_color() != self.color:     # there is an opponent piece
                    moves.append((new_row, new_col))

        return moves

class Rook(Piece):
    def get_type(self):
        return "Rook"

class Horse(Piece):
    def get_type(self):
        return "Horse"

class Bishop(Piece):
    def get_type(self):
        return "Bishop"

class Queen(Piece):
    def get_type(self):
        return "Queen"

class King(Piece):
    def get_type(self):
        return "King"


class Empty(Piece):
    def get_type(self):
        return "Empty"