from src import individual as ind
import random


class Population(object):

    def __init__(self, **kwargs):
        self.population_fitness = -2
        self.population_size = kwargs.get("population_size", 0)
        self.chromosome_length = kwargs.get("chromosome_length", 0)
        self.population = []
        if self.population_size > 0:
            self.population = [ind.Individual() for i in range(self.population_size)]
        if self.chromosome_length > 0:
            self.population = [ind.Individual(chromosome_length=self.chromosome_length)
                               for i in self.population]

   # def __iter__(self):
    #    return (x for x in self.population)

    def get_fittest(self, index):
        self.population = sorted(self.population)
        return self.population[index]


    def suffle(self):
        self.population = random.suffle(self.population)
