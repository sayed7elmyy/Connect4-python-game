import numpy as np
import pygame
import sys
import random
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0
WINDOW_LENGTH = 4

pygame.init()

THEMES = {
    "Classic": {"board_color": (0, 0, 255), "player_color": (255, 0, 0), "ai_color": (255, 255, 0), "winning_color": (0, 255, 0)},
    "Space": {"board_color": (30, 30, 30), "player_color": (135, 206, 235), "ai_color": (255, 215, 0), "winning_color": (0, 255, 0)},
    "Neon": {"board_color": (50, 205, 50), "player_color": (255, 105, 180), "ai_color": (0, 255, 255), "winning_color": (255, 255, 0)}
}

SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")

font = pygame.font.SysFont("monospace", 35)

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), int) #np is A function from the NumPy library used to create an array filled with zeros.

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Horizontal win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and all([board[r][c+i] == piece for i in range(4)]):
                return [(r, c+i) for i in range(4)]
    # Vertical win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and all([board[r+i][c] == piece for i in range(4)]):
                return [(r+i, c) for i in range(4)]
    # Positive diagonal win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and all([board[r+i][c+i] == piece for i in range(4)]):
                return [(r+i, c+i) for i in range(4)]
    # Negative diagonal win
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and all([board[r-i][c+i] == piece for i in range(4)]):
                return [(r-i, c+i) for i in range(4)]
    return None

# Draw the board
def draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR, winning_tiles=None):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BOARD_COLOR, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (255, 255, 255), (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, PLAYER_COLOR, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, AI_COLOR, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    if winning_tiles:
        for (r, c) in winning_tiles:
            pygame.draw.circle(screen, WINNING_COLOR, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    pygame.display.update()

def ai_move_easy(board):
    valid_columns = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    return random.choice(valid_columns)

def ai_move_medium(board):
    valid_columns = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    for col in valid_columns:
        row = get_next_open_row(board, col)
        board_copy = board.copy()
        drop_piece(board_copy, row, col, AI_PIECE)
        if winning_move(board_copy, AI_PIECE):
            return col
        if winning_move(board_copy, PLAYER_PIECE):
            return col
    return random.choice(valid_columns)

# Minimax algorithm with Alpha-Beta Pruning for Hard difficulty
def minimax(board, depth, maximizing_player, alpha, beta):
    valid_columns = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    is_terminal = winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(valid_columns) == 0

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -100000000000000)
            else:
                return (None, 0)
        else:
            return (None, 0)

    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_columns)
        for col in valid_columns:
            row = get_next_open_row(board, col)
            board_copy = board.copy()
            drop_piece(board_copy, row, col, AI_PIECE)
            new_score = minimax(board_copy, depth-1, False, alpha, beta)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_columns)
        for col in valid_columns:
            row = get_next_open_row(board, col)
            board_copy = board.copy()
            drop_piece(board_copy, row, col, PLAYER_PIECE)
            new_score = minimax(board_copy, depth-1, True, alpha, beta)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def ai_move_hard(board):
    column, minimax_score = minimax(board, 5, True, -math.inf, math.inf)
    return column

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def display_winner(winner):

    overlay = pygame.Surface((width, height))
    overlay.set_alpha(150)  # Transparency
    overlay.fill((0, 0, 0))  # Black overlay
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 75)
    small_font = pygame.font.Font(None, 50)

    if winner == "Draw":
        message = "It's a Draw!"
        color = (255, 255, 0)  # Yellow
    elif winner == "Player":
        message = "Player Wins!"
        color = (0, 255, 0)  # Green
    else:  # "AI"
        message = "AI Wins!"
        color = (255, 0, 0)  # Red

    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text_surface, text_rect)

    restart_message = "Click to Restart"
    restart_text = small_font.render(restart_message, True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(restart_text, restart_rect)

    pygame.display.update()

    return restart_rect

def display_theme_selection():
    themes = list(THEMES.keys())
    buttons = {}
    button_width = width // 3
    button_height = 50
    for i, theme in enumerate(themes):
        x = (width - button_width) // 2
        y = 100 + (button_height + 10) * i
        button_rect = pygame.draw.rect(screen, (0, 255, 0), (x, y, button_width, button_height), border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), (x, y, button_width, button_height), 5)
        text = font.render(theme, True, (0, 0, 0))
        text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2))
        screen.blit(text, text_rect)
        buttons[theme] = button_rect
    pygame.display.update()
    return buttons

def display_difficulty_selection():
    difficulties = ['Easy', 'Medium', 'Hard']
    buttons = {}
    button_width = width // 3
    button_height = 50
    for i, diff in enumerate(difficulties):
        x = (width - button_width) // 2
        y = 100 + (button_height + 10) * i
        button_rect = pygame.draw.rect(screen, (0, 255, 0), (x, y, button_width, button_height), border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), (x, y, button_width, button_height), 5)
        text = font.render(diff, True, (0, 0, 0))
        text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2))
        screen.blit(text, text_rect)
        buttons[diff] = button_rect
    pygame.display.update()
    return buttons

def main():
    while True:
        buttons = display_theme_selection()
        theme_selected = False
        selected_theme = None
        while not theme_selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for theme, button_rect in buttons.items():
                        if button_rect.collidepoint(event.pos):
                            selected_theme = theme
                            theme_selected = True
                            break

        current_theme = THEMES[selected_theme]
        PLAYER_COLOR = current_theme["player_color"]
        AI_COLOR = current_theme["ai_color"]
        WINNING_COLOR = current_theme["winning_color"]
        BOARD_COLOR = current_theme["board_color"]

        buttons = display_difficulty_selection()
        difficulty_selected = False
        difficulty = None
        while not difficulty_selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons['Easy'].collidepoint(event.pos):
                        difficulty = 'Easy'
                        difficulty_selected = True
                    elif buttons['Medium'].collidepoint(event.pos):
                        difficulty = 'Medium'
                        difficulty_selected = True
                    elif buttons['Hard'].collidepoint(event.pos):
                        difficulty = 'Hard'
                        difficulty_selected = True

        if difficulty == 'Easy':
            ai_move_function = ai_move_easy
        elif difficulty == 'Medium':
            ai_move_function = ai_move_medium
        else:
            ai_move_function = ai_move_hard

        board = create_board()
        game_over = False
        player_turn = True
        draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR)

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if player_turn:
                        pygame.draw.circle(screen, PLAYER_COLOR, (posx, int(SQUARESIZE / 2)), RADIUS)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_turn:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARESIZE))

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, PLAYER_PIECE)

                            if winning_move(board, PLAYER_PIECE):
                                winning_tiles = winning_move(board, PLAYER_PIECE)
                                draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR, winning_tiles)
                                display_winner("Player")
                                game_over = True
                                break

                            # Check for draw after player move
                            if all(not is_valid_location(board, col) for col in range(COLUMN_COUNT)):
                                draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR)
                                display_winner("Draw")
                                game_over = True
                                break

                            player_turn = False

            if not player_turn and not game_over:
                col = ai_move_function(board)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    winning_tiles = winning_move(board, AI_PIECE)
                    draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR, winning_tiles)
                    display_winner("AI")
                    game_over = True
                    break

                if all(not is_valid_location(board, col) for col in range(COLUMN_COUNT)):
                    draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR)
                    display_winner("Draw")
                    game_over = True
                    break

                player_turn = True

            draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, BOARD_COLOR)

        restart_button = display_winner("Player" if game_over and winning_move(board, PLAYER_PIECE) else "AI" if game_over and winning_move(board, AI_PIECE) else "Draw")
        restart_selected = False
        while not restart_selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        main()

if __name__ == "__main__":
    main()