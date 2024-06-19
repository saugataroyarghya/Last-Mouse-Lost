import pygame
import sys
from board import Board
from player import HumanPlayer, SmartPlayer, FuzzyPlayer

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Last Mouse Lost")
font = pygame.font.SysFont(None, 55)


class Game:
    def __init__(self, num_h, num_s, opponent_type, screen, font):
        self.board = Board()
        self.players = []
        self.max_select = None  # Variable to store the number of circles selected by the human player

        for _ in range(num_h):
            self.players.append(HumanPlayer(self.board, screen, font, screen_width, screen_height, self))

        if opponent_type == 'SmartPlayer':
            for _ in range(num_s):
                self.players.append(SmartPlayer(self.board, 3, screen_width, screen_height, self))
        elif opponent_type == 'FuzzyPlayer':
            for _ in range(num_s):
                self.players.append(FuzzyPlayer(self.board, 3, screen_width, screen_height, self))

        self.current_player_index = 0

    def draw_board(self):
        screen.fill((255, 255, 255))
        for i, row in enumerate(self.board.b):
            y = 100 + i * 70
            x_start = screen_width // 2 - len(row) * 35
            for j, cell in enumerate(row):
                x = x_start + j * 70
                color = (0, 0, 0) if cell == 'x' else (0, 0, 255)
                pygame.draw.circle(screen, color, (x, y), 30)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run_game(self):
        while not self.board.g_o():
            self.handle_events()
            self.draw_board()
            player = self.players[self.current_player_index]
            move = player.move()
            if move is None:
                continue

            for pos in move:
                self.board.update_b(pos[0], pos[1])
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            pygame.time.wait(1000)

        print(f"Player {self.current_player_index} lost!")
        pygame.quit()
        sys.exit()

def display_menu():
    screen.fill((255, 255, 255))
    text1 = font.render('Choose Opponent:', True, (0, 0, 0))
    text2 = font.render('1. Smart Player', True, (0, 0, 255))
    text3 = font.render('2. Fuzzy Player', True, (0, 0, 255))

    text1_rect = text1.get_rect(center=(screen_width // 2, screen_height // 3))
    text2_rect = text2.get_rect(center=(screen_width // 2, screen_height // 2))
    text3_rect = text3.get_rect(center=(screen_width // 2, screen_height // 2 + 60))

    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if text2_rect.collidepoint(mouse_pos):
                    return 'SmartPlayer'
                elif text3_rect.collidepoint(mouse_pos):
                    return 'FuzzyPlayer'

if __name__ == '__main__':
    opponent_type = display_menu()
    game = Game(1, 1, opponent_type, screen, font)
    game.run_game()
