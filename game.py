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

class Game():
    pass


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
