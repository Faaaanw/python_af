import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
GRID_SIZE = 3
GRID_SPACING = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize game variables
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
player_X_turn = True
winner = None

# Fonts
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.rect(screen, LINE_COLOR, (0, row * GRID_SPACING - LINE_WIDTH // 2, WIDTH, LINE_WIDTH))
        pygame.draw.rect(screen, LINE_COLOR, (row * GRID_SPACING - LINE_WIDTH // 2, 0, LINE_WIDTH, HEIGHT))

# Function to draw X and O on the grid
def draw_symbols():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            symbol = grid[row][col]
            if symbol == 'X':
                draw_x(row, col)
            elif symbol == 'O':
                draw_o(row, col)

# Function to draw an X
def draw_x(row, col):
    x_center = col * GRID_SPACING + GRID_SPACING // 2
    y_center = row * GRID_SPACING + GRID_SPACING // 2
    half_size = GRID_SPACING // 2 - 10
    pygame.draw.line(screen, X_COLOR, (x_center - half_size, y_center - half_size), (x_center + half_size, y_center + half_size), 10)
    pygame.draw.line(screen, X_COLOR, (x_center - half_size, y_center + half_size), (x_center + half_size, y_center - half_size), 10)

# Function to draw an O
def draw_o(row, col):
    x_center = col * GRID_SPACING + GRID_SPACING // 2
    y_center = row * GRID_SPACING + GRID_SPACING // 2
    radius = GRID_SPACING // 2 - 10
    pygame.draw.circle(screen, O_COLOR, (x_center, y_center), radius, 10)

# Function to check for a win
def check_win(symbol):
    # Check rows, columns, and diagonals
    for i in range(GRID_SIZE):
        if all(grid[i][j] == symbol for j in range(GRID_SIZE)) or all(grid[j][i] == symbol for j in range(GRID_SIZE)):
            return True
    if all(grid[i][i] == symbol for i in range(GRID_SIZE)) or all(grid[i][GRID_SIZE - 1 - i] == symbol for i in range(GRID_SIZE)):
        return True
    return False

# Function to check for a draw
def check_draw():
    return all(all(cell != '' for cell in row) for row in grid)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if winner is None:
            if event.type == pygame.MOUSEBUTTONDOWN and not check_draw():
                row = event.pos[1] // GRID_SPACING
                col = event.pos[0] // GRID_SPACING
                if grid[row][col] == '':
                    if player_X_turn:
                        grid[row][col] = 'X'
                    else:
                        grid[row][col] = 'O'
                    player_X_turn = not player_X_turn
            winner = 'X' if check_win('X') else ('O' if check_win('O') else None)

    screen.fill(WHITE)
    draw_grid()
    draw_symbols()

    if winner:
        winner_text = font.render(f"Player {winner} wins!", True, LINE_COLOR)
        screen.blit(winner_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    elif check_draw():
        draw_text = font.render("It's a draw!", True, LINE_COLOR)
        screen.blit(draw_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))

    pygame.display.flip()
