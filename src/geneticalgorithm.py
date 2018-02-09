#calcFitness
#evalPopulation
#isTerminationConditionMet
#crossoverPopulation
#mutatePopulation


class GeneticAlgoritm:

    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
