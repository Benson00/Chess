# player.py
class Player:
    def __init__(self, color):
        """
        Initialize a Player.

        :param color: 'white' or 'black'
        """
        self.color = color

    def get_move(self, board):
        """
        Abstract method to get a move from the player.

        :param board: Current state of the board
        :return: Tuple of start and end positions ((start_row, start_col), (end_row, end_col))
        """
        raise NotImplementedError("This method should be overridden by subclasses")
