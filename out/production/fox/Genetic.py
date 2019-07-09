import random
class DNA:
    xBound = 100
    yBound = 100
    size = 100
    @staticmethod
    def generate():
        return random.uniform(0, DNA.xBound), random.uniform(0, DNA.yBound)

    def __init__(self):
        self.locations = []
        self.colors = []
        fitness = 0
        for i in range(DNA.size):
            self.locations.append(DNA.generate())
            self.colors.append((random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)))

    def calc_fitness(self, target):


    def crossover(self, target):
        child = DNA()
        for i in range(DNA.size):
            if random.randint(0, 1):
                child.locations.append(self.locations[i])
                child.colors.append(self.colors[i])
            else:
                child.locations.append(self.locations[i])
                child.colors.append(self.colors[i])

    def mutate(self, mutation_rate):
        for i in range(DNA.size):
            if random.random() < mutation_rate:
                self.locations[i] = DNA.generate()
                self.colors[i] = random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)

class Population:
    def __init__(self, target, mutation_rate, num):
        self.target = target
        self.mutation_rate = mutation_rate
        self.population = []
        self.mates = {}
        self.generation = 0
        self.finished = False
        self.size = 100
        for i in range(num):
            self.population.append(DNA())
        self.calc_fitness()

    def calc_fitness(self):
        for i in self.population:
            i.calc_fitness()

    def selection(self):
        self.mates = sorted(self.population, key=lambda dna: dna.fitness)[-5:]

    def reproduce(self):
        probability = [0.35, 0.275, 0.2, 0.125, 0.05]
        for i in range(self.size):
            out = random.choice(self.mates, 2, replace=False, p=probability)
            mother = out[0]
            father = out[1]
            child = mother.crossover(father)
            child.mutate(self.mutation_rate)
            self.population.append(child)
        self.generation += 1

    def most_fit(self):
        return min(self.population, key=lambda dna: dna.fitness)