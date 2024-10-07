import pygame
from Board import Board
from human_player import HumanPlayer

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (118, 150, 86)
BLUE = (238, 238, 210)

# Screen settings
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

def load_images():
    pieces = ['bR', 'bH', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wH', 'wB', 'wQ', 'wK', 'wP']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(
            pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))
    return images

IMAGES = load_images()

def draw_board(screen):
    colors = [BLUE, GREEN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(
                col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board.grid[row][col]
            if piece:
                piece_name = piece.get_type()
                piece_color = piece.get_color()[0]  # 'w' or 'b'
                screen.blit(IMAGES[piece_color + piece_name[0]], pygame.Rect(
                    col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def highlight_moves(screen, possible_moves):
    """
    Highlight the possible moves on the board.

    :param screen: The pygame screen where the board is drawn.
    :param possible_moves: List of possible moves (row, col) tuples.
    """
    for move in possible_moves:
        row, col = move
        # Draw a semi-transparent blue rectangle on the possible move squares
        s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        s.fill((0, 255, 255, 100))  # RGBA
        screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def main():
    chess_board = Board()
    # Initialize players
    white_player = HumanPlayer('white')
    black_player = HumanPlayer('black')
    players = {'white': white_player, 'black': black_player}

    turn = 'white'  # Track the current player's turn
    game_over = False  # Track if the game is over

    running = True
    while running:
        current_player = players[turn]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over:
                current_player.handle_event(event, chess_board)

                if current_player.move_made:
                    (start_row, start_col), (end_row, end_col) = current_player.move
                    
                    # Validate if the move is possible
                    possible_moves = current_player.selected_piece.get_moves(chess_board.grid, start_row, start_col)
                    
                    if (end_row, end_col) in possible_moves:
                        # Move the piece only if it's a valid move
                        chess_board.move_piece(start_row, start_col, end_row, end_col)

                        # Switch turn after a valid move
                        turn = 'black' if turn == 'white' else 'white'

                        # Reset player move
                        current_player.move_made = False
                        current_player.move = None

                        # Reset possible moves to avoid highlights after move
                        current_player.possible_moves = []  # Reset highlight moves

                        # Check for checkmate after the move
                        if chess_board.is_checkmate(turn):
                            game_over = True
                    else:
                        # If the move is not valid, reset move
                        current_player.move_made = False
                        current_player.move = None

        # Draw the board and pieces
        draw_board(screen)
        draw_pieces(screen, chess_board)

        # Highlight the possible moves if a piece is selected
        if current_player.selected_piece and current_player.possible_moves:
            highlight_moves(screen, current_player.possible_moves)

        # If the game is over, display a checkmate message
        if game_over:
            font = pygame.font.SysFont('Arial', 60)
            text = font.render(f'{turn.capitalize()} is in Checkmate!', True, (255, 0, 0))
            screen.blit(text, (WIDTH // 4, HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
