# human_player.py
import pygame
from player import Player

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)
        self.selected_piece = None
        self.possible_moves = []
        self.move_made = False
        self.move = None

    def handle_event(self, event, board):
        """
        Handle Pygame events to select and move pieces.

        :param event: Pygame event
        :param board: Current state of the board
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // SQUARE_SIZE
            row = pos[1] // SQUARE_SIZE

            if self.selected_piece:
                if (row, col) in self.possible_moves:
                    start_pos = self.selected_piece_position
                    end_pos = (row, col)
                    self.move = (start_pos, end_pos)
                    self.move_made = True
                else:
                    new_piece = board.grid[row][col]
                    if new_piece and new_piece.get_color() == self.color:
                        self.selected_piece = new_piece
                        self.possible_moves = self.selected_piece.get_moves(board.grid, row, col)
                        self.selected_piece_position = (row, col)
                    else:
                        self.selected_piece = None
                        self.possible_moves = []
            else:
                piece = board.grid[row][col]
                if piece and piece.get_color() == self.color:
                    self.selected_piece = piece
                    self.possible_moves = piece.get_moves(board.grid, row, col)
                    self.selected_piece_position = (row, col)
