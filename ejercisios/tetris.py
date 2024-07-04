import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definición de constantes
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
FONT_SIZE = 30
FPS = 60  # Aumentamos los FPS para tener más precisión en el tiempo de caída

# Tiempo en milisegundos para la caída de las piezas
PIECE_DROP_TIME = 500  # Puedes ajustar este valor para aumentar o disminuir el tiempo de caída

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Lista de colores
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, WHITE]

# Creación de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

# Define la forma de cada pieza de Tetris
shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3],
     [3, 3]],

    [[0, 4, 0],
     [4, 4, 4]],

    [[5, 0, 0],
     [5, 5, 5]],

    [[0, 0, 6],
     [6, 6, 6]],

    [[7, 7, 0],
     [0, 7, 7]]
]

# Clase para representar una pieza de Tetris
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0

    def draw(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] != 0:
                    pygame.draw.rect(screen, self.color, (self.x + j * BLOCK_SIZE, self.y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, BLACK, (self.x + j * BLOCK_SIZE, self.y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

    def move_down(self):
        self.y += BLOCK_SIZE

    def move_left(self):
        self.x -= BLOCK_SIZE

    def move_right(self):
        self.x += BLOCK_SIZE

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# Función para dibujar el tablero
def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                pygame.draw.rect(screen, colors[board[i][j] - 1], (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

# Función para comprobar si la pieza puede moverse a la posición deseada
def can_move(piece, board, dx, dy):
    for i in range(len(piece.shape)):
        for j in range(len(piece.shape[i])):
            if piece.shape[i][j] != 0:
                x = piece.x // BLOCK_SIZE + j + dx
                y = piece.y // BLOCK_SIZE + i + dy
                if x < 0 or x >= len(board[0]) or y >= len(board) or (y >= 0 and board[y][x] != 0):
                    return False
    return True

# Función para eliminar filas completas
def remove_complete_rows(board):
    rows_to_remove = []
    for i in range(len(board)):
        if 0 not in board[i]:
            rows_to_remove.append(i)
    for row in rows_to_remove:
        del board[row]
        board.insert(0, [0 for _ in range(len(board[0]))])

# Función principal del juego
def main():
    board = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    current_piece = Piece(3 * BLOCK_SIZE, 0, random.choice(shapes))

    last_move_down_time = pygame.time.get_ticks()
    
    game_over = False
    while not game_over:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and can_move(current_piece, board, -1, 0):
                    current_piece.move_left()
                elif event.key == pygame.K_RIGHT and can_move(current_piece, board, 1, 0):
                    current_piece.move_right()
                elif event.key == pygame.K_DOWN and can_move(current_piece, board, 0, 1):
                    current_piece.move_down()
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not can_move(current_piece, board, 0, 0):
                        current_piece.rotate()
                        current_piece.rotate()
                        current_piece.rotate()

        if current_time - last_move_down_time >= PIECE_DROP_TIME:
            if can_move(current_piece, board, 0, 1):
                current_piece.move_down()
            else:
                for i in range(len(current_piece.shape)):
                    for j in range(len(current_piece.shape[i])):
                        if current_piece.shape[i][j] != 0:
                            x = current_piece.x // BLOCK_SIZE + j
                            y = current_piece.y // BLOCK_SIZE + i
                            if y >= 0:
                                board[y][x] = colors.index(current_piece.color) + 1
                remove_complete_rows(board)
                current_piece = Piece(3 * BLOCK_SIZE, 0, random.choice(shapes))
                if not can_move(current_piece, board, 0, 0):
                    game_over = True
            last_move_down_time = current_time

        screen.fill(BLACK)
        draw_board(board)
        current_piece.draw()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
