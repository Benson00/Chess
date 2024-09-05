from Piece import King, Queen, Bishop, Horse, Rook, Pawn 


class Board:
    
    def __init__(self):
        """
        Initializes the chessboard.

        This constructor method sets up the chessboard by creating an 8x8 grid and populating it with `None` to represent
        empty squares. After initializing the grid, it calls the `setup_board` method to arrange the chess pieces in their 
        starting positions.

        :grid: An 8x8 list of lists representing the chessboard. Each element can be a `ChessPiece` object or `None`.
        :vartype grid: list[list[ChessPiece | None]]

        Upon instantiation, `board.grid` will contain a fully initialized chessboard with all pieces in their correct starting positions.

        :note: The `setup_board` method is automatically called during initialization to set up the pieces on the board.
        """
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()
        

    def setup_board(self):
        """
        Configures the chessboard with the initial piece setup.

        This method initializes the board to the standard chess starting position, with all pieces arranged 
        in their correct initial locations. It places black pieces on the first two rows and white pieces on the last two rows.

        :return: None
        :rtype: None

        :raises: No exceptions are raised by this method.
        
        note: This method assumes that `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, and `King` classes have been defined.

        """
        for i in range(8):
            self.grid[1][i] = Pawn("black")
            self.grid[6][i] = Pawn("white")
        
        # Torri
        self.grid[0][0] = Rook("black")
        self.grid[0][7] = Rook("black")
        self.grid[7][0] = Rook("white")
        self.grid[7][7] = Rook("white")
        
        # Cavalli
        self.grid[0][1] = Horse("black")
        self.grid[0][6] = Horse("black")
        self.grid[7][1] = Horse("white")
        self.grid[7][6] = Horse("white")
        
        # Alfieri
        self.grid[0][2] = Bishop("black")
        self.grid[0][5] = Bishop("black")
        self.grid[7][2] = Bishop("white")
        self.grid[7][5] = Bishop("white")
        
        # Regine
        self.grid[0][3] = Queen("black")
        self.grid[7][3] = Queen("white")
        
        # Re
        self.grid[0][4] = King("black")
        self.grid[7][4] = King("white")
        self.__print_board()


    def __print_board(self):
            """
            Prints the chessboard with the pieces in their current positions.

            This method iterates over the grid and prints a simple textual representation of the board.

            Use this method for debugging.

            Private method.
            """
            piece_symbols = {
                'Pawn': 'P', 'Rook': 'R', 'Horse': 'H', 'Bishop': 'B', 'Queen': 'Q', 'King': 'K'
            }
            
            for row in self.grid:
                print(" | ".join([piece_symbols.get(type(piece).__name__, '.') if piece else '.' for piece in row]))
                print("-" * 33)

    def get_piece_moves(self, row, col):
        """
        Retrieve possible moves for the piece at the given position.

        :param row: The row of the piece.
        :param col: The column of the piece.
        :return: A list of possible moves for the piece.
        """
        piece = self.grid[row][col]
        if piece:
            return piece.get_moves(self.grid, row, col)  # Calls the get_moves of the specific piece, like Pawn
        return []



chess_board = Board()
print(chess_board.get_piece_moves(1,1))