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

        :note: This method assumes that `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, and `King` classes have been defined,
            and that these classes accept a color argument ('black' or 'white').

        """
        pass



