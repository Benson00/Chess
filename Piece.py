from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self,color):
        self.color = color
    
    @abstractmethod
    def get_moves(self, r, c):
        pass