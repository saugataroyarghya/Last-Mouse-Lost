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
    def num_row(self):
        temp_l = []
        for i in range(len(self.b)):
            s = 0
            for c in range(len(self.b[i])-1, -1, -1):
                if self.b[i][c] == 'o':
                    s += 1
                else:
                    break
                temp_l.append(s)
        return temp_l
    
    def diff(self, r1, r2):
        r10 = 0
        r20 = 0
        for i in range(0, len(self.b[r1])):
            if self.b[r1][i] == 'o':
                r10 += 1
            if self.b[r2][i] == 'o':
                r20 += 1
        if r10 > r20:
            return (r1, r10 - r20)
        else:
            return (r2, r20 - r10)

    def dupe(self):
        new_board = Board()
        new_board.b = [row[:] for row in self.b]
        return new_board
