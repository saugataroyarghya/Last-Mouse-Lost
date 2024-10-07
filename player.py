from random import randint as rand
import random 
import board as Board 
import collections as col


class Player:
	def __init__(self, board):
		self.board = board

	def move(self):
		raise NotImplementedError


class RandomPlayer(Player):
	def move(self):
		r = rand(0, 5)
		while self.board.row_empty(r):
			r = rand(0, 5)
		return (r, rand(1, self.board.spot_avail(r)) + 1)

	def __str__(self):
		return 'Random Player'


class HumanPlayer(Player):
	def move(self):
		try:
			pr = int(input('Row: '))
			pa = int(input('Amount: '))
		except ValueError:
			pr = -1
			pa = -1
		while pr > 5 or self.board.row_empty(pr) or pa <= 0 or pr < 0:
			print('Invalid move')
			try:
				pr = int(input('Row: '))
				pa = int(input('Amount: '))
			except ValueError:
				pr = -1
				pa = -1
		return (pr, pa)

	def __str__(self):
		return 'Human Player'


class SmartPlayer(Player):
	def __init__(self, board, pn):
		Player.__init__(self, board)
		self.pn = pn

	def _rmove(self):
		r = rand(0, 5)
		while self.board.row_empty(r):
			r = rand(0, 5)
		return (r, rand(1, self.board.spot_avail(r)))

	def move(self):
		cur_b = col.Counter(self.board.num_row())
		if cur_b in [{0: 2, 1: 4}, {0: 2, 1: 3, 2: 1}, {0: 2, 1: 3, 3: 1}, {0: 2, 1: 3, 4: 1}, {0: 2, 1: 3, 5: 1}, {0: 2, 1: 3, 6: 1}, {1: 6}, {1: 5, 2: 1}, {1: 5, 3: 1}, {1: 5, 4: 1}, {1: 5, 5: 1}, {1: 5, 6: 1}, {0: 4, 1: 2}, {0: 4, 1: 1, 2: 1}, {0: 4, 1: 1, 3: 1}, {0: 4, 1: 1, 4: 1}, {0: 4, 1: 1, 5: 1}, {0: 4, 1: 1, 6: 1}]:
			m = 0
			r = 0
			for i in range(len(self.board)):
				if self.board.spot_avail(i) > m:
					m = self.board.spot_avail(i)
					r = i
			return (r, m)
		elif cur_b in [{0: 1, 1: 4, 2: 1}, {0: 1, 1: 4, 3: 1}, {0: 1, 1: 4, 4: 1}, {0: 1, 1: 4, 5: 1}, {0: 1, 1: 4, 6: 1}, {0: 3, 1: 2, 2: 1}, {0: 3, 1: 2, 3: 1}, {0: 3, 1: 2, 4: 1}, {0: 3, 1: 2, 5: 1}, {0: 3, 1: 2, 6: 1}, {0: 5, 2: 1}, {0: 5, 3: 1}, {0: 5, 4: 1}, {0: 5, 5: 1}, {0: 5, 6: 1}]:
			m = 0
			r = 0
			for i in range(len(self.board)):
				if self.board.spot_avail(i) > m:
					m = self.board.spot_avail(i)
					r = i
			return (r, m - 1)
		else:
			if self.board.b[0] != self.board.b[5]:
				return self.board.diff(0, 5)
			if self.board.b[1] != self.board.b[4]:
				return self.board.diff(1, 4)
			if self.board.b[2] != self.board.b[3]:
				return self.board.diff(2, 3)
			else:
				return self._rmove()

	def __str__(self):
		return 'Smart Player'
	

class FuzzyPlayer(Player):
    pass

class GeneticAlgorithmPlayer(Player):
    def __init__(self, board, population_size=20, generations=100):
        super().__init__(board)
        self.population_size = population_size
        self.generations = generations
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = [self.random_move(self.board) for _ in range(5)]  
            population.append(individual)
        return population

    def random_move(self, board):
        """Generates a random valid move for the given board state."""
        valid_moves = self.generate_possible_moves(board)
        if valid_moves:
            return random.choice(valid_moves)
        else:
            return (0, 1)  

    def generate_possible_moves(self, board):
        """Generate all possible valid moves for the current board state."""
        possible_moves = []
        for r in range(len(board.b)):
            if not board.row_empty(r):
                for a in range(1, board.spot_avail(r) + 1):
                    possible_moves.append((r, a))
        return possible_moves

    def evolve_population(self):
        """Evolves the population over a set number of generations."""
        for generation in range(self.generations):
            
            population_fitness = [(self.evaluate_individual(individual), individual) for individual in self.population]
            population_fitness.sort(reverse=True, key=lambda x: x[0])
            self.population = [individual for _, individual in population_fitness[:self.population_size // 2]]

          
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(self.population, 2)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])

            self.population = new_population

    def crossover(self, parent1, parent2):
        """Performs crossover between two parents to produce two children."""
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, individual):
        """Randomly mutates an individual's move with a small probability."""
        mutation_rate = 0.1
        if random.random() < mutation_rate:
            index = random.randint(0, len(individual) - 1)
            individual[index] = self.random_move(self.board)
        return individual

    def evaluate_individual(self, individual):
        """Evaluates the fitness of an individual based on their moves for the game."""
       
        simulated_board = self.copy_board(self.board)
        score = 0

        for move in individual:
            r, a = move
            if 0 <= r < len(simulated_board.b) and 1 <= a <= simulated_board.spot_avail(r):
                simulated_board.update_b(r, a)
                if simulated_board.g_o():
                    score -= 100  
                    break
                else: 
                    score -= len(self.generate_possible_moves(simulated_board))
            else:
                score -= 100

       
        if not simulated_board.g_o():
            score += 50 if len(self.generate_possible_moves(simulated_board)) == 1 else 0

        return score

    def copy_board(self, board):
        """Creates a deep copy of the board to simulate game states."""
        return board.dupe()
    
    def move(self):
        """Choose the best move from the evolved population."""
        self.evolve_population()
        best_individual = max(self.population, key=lambda ind: self.evaluate_individual(ind))
        return best_individual[0]

    def __str__(self):
        return 'Genetic Algorithm Player'
 
       
class AStarPlayer(Player):
      pass
class MinMaxPlayer(Player):
      pass

