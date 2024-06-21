import pygame
import tkinter as tk
from tkinter import simpledialog


class HumanPlayer:
    def __init__(self, board, screen, font, screen_width, screen_height, game):
        self.board = board
        self.screen = screen
        self.font = font
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game = game  # Reference to the game instance to store max_select

    def move(self):
        pos = self.get_click_position()
        if pos is None:
            return None

        r, c = pos
        if self.board.b[r][c] == 'o':
            max_select = self.get_max_select()
            self.game.max_select = max_select  # Store the max_select in the game instance
            move = []
            for col in range(c, min(c + max_select, len(self.board.b[r]))):
                if self.board.b[r][col] == 'o':
                    move.append((r, col))
                else:
                    break
            return move
        return None

    def get_click_position(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, row in enumerate(self.board.b):
                    row_y = 100 + i * 70
                    row_x_start = self.screen_width // 2 - len(row) * 35
                    for j, cell in enumerate(row):
                        cell_x = row_x_start + j * 70
                        if (cell_x - 30 <= x <= cell_x + 30) and (row_y - 30 <= y <= row_y + 30):
                            return (i, j)
        return None

    def get_max_select(self):
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        max_select = simpledialog.askinteger("Amount", "Enter the number of circles to select:")

        root.destroy()  # Close the root window
        return max_select if max_select is not None else 1
import pygame
import random

class SmartPlayer:
    def __init__(self, board, depth, screen_width, screen_height, game):
        self.board = board
        self.depth = depth
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game = game  # Reference to the game instance to get max_select

    def move(self):
        max_select = self.game.max_select if self.game.max_select is not None else 1  # Use max_select from game
        move = self.minimax(self.board, self.depth, True, float('-inf'), float('inf'), max_select)
        return move[1]

    def minimax(self, board, depth, maximizing, alpha, beta, max_select):
        if depth == 0 or board.g_o():
            return self.evaluate(board), []

        if maximizing:
            max_eval = float('-inf')
            best_move = []
            for r in range(len(board.b)):
                for c in range(len(board.b[r])):
                    if board.b[r][c] == 'o':
                        new_board = board.dupe()
                        move = []
                        for col in range(c, min(c + max_select, len(new_board.b[r]))):
                            if new_board.b[r][col] == 'o':
                                move.append((r, col))
                            else:
                                break
                        for pos in move:
                            new_board.update_b(pos[0], pos[1])
                        eval = self.minimax(new_board, depth - 1, False, alpha, beta, max_select)[0]
                        if eval > max_eval:
                            max_eval = eval
                            best_move = move
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = []
            for r in range(len(board.b)):
                for c in range(len(board.b[r])):
                    if board.b[r][c] == 'o':
                        new_board = board.dupe()
                        move = []
                        for col in range(c, min(c + max_select, len(new_board.b[r]))):
                            if new_board.b[r][col] == 'o':
                                move.append((r, col))
                            else:
                                break
                        for pos in move:
                            new_board.update_b(pos[0], pos[1])
                        eval = self.minimax(new_board, depth - 1, True, alpha, beta, max_select)[0]
                        if eval < min_eval:
                            min_eval = eval
                            best_move = move
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval, best_move

    def evaluate(self, board):
        # Simple evaluation function
        score = 0
        for row in board.b:
            score += row.count('o')
        return -score    