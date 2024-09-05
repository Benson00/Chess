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
    current_turn = "white"  # Inizializza il turno del bianco

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQUARE_SIZE
                row = pos[1] // SQUARE_SIZE

                if selected_piece:  # Se un pezzo è già selezionato, il clic è per il movimento
                    if (row, col) in possible_moves:
                        start_row, start_col = selected_piece_position
                        chess_board.move_piece(start_row, start_col, row, col)
                        selected_piece = None
                        possible_moves = []

                        # Cambia il turno dopo un movimento valido
                        current_turn = "black" if current_turn == "white" else "white"
                    else:
                        new_piece = chess_board.grid[row][col]
                        if new_piece and new_piece.get_color() == selected_piece.get_color():
                            selected_piece = new_piece
                            possible_moves = selected_piece.get_moves(chess_board.grid, row, col)
                            selected_piece_position = (row, col)
                else:
                    # Seleziona un pezzo
                    selected_piece = chess_board.grid[row][col]
                    if selected_piece:
                        # Controlla se il pezzo selezionato appartiene al turno corrente
                        if selected_piece.get_color() == current_turn:
                            possible_moves = selected_piece.get_moves(chess_board.grid, row, col)
                            selected_piece_position = (row, col)
                        else:
                            # Il pezzo non appartiene al turno corrente, non selezionarlo
                            selected_piece = None

        # Disegna la scacchiera e i pezzi
        draw_board(screen)
        draw_pieces(screen, chess_board)

        # Evidenzia le mosse possibili se un pezzo è selezionato
        if possible_moves:
            highlight_moves(screen, possible_moves)

        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
