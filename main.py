import pygame
from Board import Board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (118, 150, 86)
BLUE = (238, 238, 210)

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

def load_images():
    pieces = ['bR', 'bH', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wH', 'wB', 'wQ', 'wK', 'wP']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))
    return images

IMAGES = load_images()

def draw_board(screen):
    colors = [BLUE, GREEN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board.grid[row][col]
            if piece:
                piece_name = piece.get_type()
                piece_color = piece.get_color()[0]  # 'w' or 'b'
                screen.blit(IMAGES[piece_color + piece_name[0]], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def highlight_moves(screen, possible_moves):
    """
    Highlight the possible moves on the board.

    :param screen: The pygame screen where the board is drawn.
    :param possible_moves: List of possible moves (row, col) tuples.
    """
    for move in possible_moves:
        row, col = move
        # Draw a semi-transparent blue rectangle on the possible move squares
        pygame.draw.rect(screen, (0, 255, 255, 128), pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

def main():
    chess_board = Board()  
    selected_piece = None
    possible_moves = []
    turn = 'white'  # Track the current player's turn
    game_over = False  # Track if the game is over

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over:  # Allow interaction only if the game is not over
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // SQUARE_SIZE
                    row = pos[1] // SQUARE_SIZE

                    if selected_piece:  # If a piece is already selected, handle movement
                        if (row, col) in possible_moves:
                            start_row, start_col = selected_piece_position
                            chess_board.move_piece(start_row, start_col, row, col)
                            
                            # Switch turn after a valid move
                            turn = 'black' if turn == 'white' else 'white'

                            # Reset selection
                            selected_piece = None
                            possible_moves = []

                            # Check for checkmate after the move
                            if chess_board.is_checkmate(turn):
                                game_over = True  # End the game if it's checkmate
                        else:
                            # Allow selecting a new piece only if it's the player's piece
                            new_piece = chess_board.grid[row][col]
                            if new_piece and new_piece.get_color() == turn:
                                selected_piece = new_piece
                                possible_moves = selected_piece.get_moves(chess_board.grid, row, col)
                                selected_piece_position = (row, col)
                    else:
                        # Select a piece if it's the player's turn
                        selected_piece = chess_board.grid[row][col]
                        if selected_piece and selected_piece.get_color() == turn:
                            possible_moves = selected_piece.get_moves(chess_board.grid, row, col)
                            selected_piece_position = (row, col)

        # Draw the board and pieces
        draw_board(screen)
        draw_pieces(screen, chess_board)

        # Highlight the possible moves if a piece is selected
        if possible_moves:
            highlight_moves(screen, possible_moves)

        # If the game is over, display a checkmate message
        if game_over:
            font = pygame.font.SysFont('Arial', 60)
            text = font.render(f'{turn.capitalize()} is in Checkmate!', True, (255, 0, 0))
            screen.blit(text, (WIDTH // 4, HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()




if __name__ == "__main__":
    main()
