class Board:
    def __init__(self):
        self.b = [['o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'],
                  ['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o']]

    def update_b(self, r, c):
        if self.b[r][c] == 'o':
            self.b[r][c] = 'x'

    def spot_avail(self, r):
        return sum(1 for cell in self.b[r] if cell == 'o')

    def row_empty(self, r):
        return all(cell == 'x' for cell in self.b[r])

    def draw(self):
        for i in range(len(self.b)):
            import math
            print(str(i) + ' '*(int(math.floor((i-2.5)**2)+4)), end='')
            for c in self.b[i]:
                print(c, end='   ')
            print()

    def g_o(self):
        for row in self.b:
            if 'o' in row:
                return False
        return True

    def __len__(self):
        return len(self.b)

    def dupe(self):
        new_board = Board()
        new_board.b = [row[:] for row in self.b]
        return new_board
