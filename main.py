import pygame
from Board import Board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (118, 150, 86)
BLUE = (238, 238, 210)

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Inizializzazione di pygame
pygame.init()

# Creazione della finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")


def load_images():
    pieces = ['bR', 'bH', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wH', 'wB', 'wQ', 'wK', 'wP']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))
    return images

IMAGES = load_images()

# Disegno della scacchiera
def draw_board(screen):
    colors = [BLUE, GREEN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Disegno dei pezzi sulla scacchiera
def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board.grid[row][col]
            if piece:
                piece_name = piece.get_type()
                piece_color = piece.get_color()[0]  # 'w' or 'b'
                screen.blit(IMAGES[piece_color + piece_name[0]], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Loop principale del gioco
def main():
    chess_board = Board()  # Inizializzazione della scacchiera
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(screen)
        draw_pieces(screen, chess_board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
