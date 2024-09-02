
from typing import override
import Piece


class King(Piece):
    
    def __init__(self, color):
        super().__init__(color)
    
    def get_moves(self, r, c):
        allowed_moves =[]
        
        if r-1 >= 0:
            if c-1 >= 0:
                allowed_moves.append((r-1,c-1))
            allowed_moves.append(r-1,c)
            if c+1 <= 7:
                allowed_moves.append((r-1,c+1))
        
        if r+1 <= 7:
            if c-1 >= 0:
                allowed_moves.append((r+1,c-1))
            allowed_moves.append(r+1,c)
            if c+1 <= 7:
                allowed_moves.append((r+1,c+1))

        if c-1 >= 0:
                allowed_moves.append((r,c-1))
        allowed_moves.append(r,c)
        if c+1 <= 7:
                allowed_moves.append((r,c+1))

        return allowed_moves



