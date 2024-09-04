class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Pawn(Piece):
    def get_type(self):
        return "Pawn"

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
