from src import individual as ind
import random


class Population(object):

    def __init__(self, **kwargs):
        self.journeys = []
        self.population_size = kwargs.get("population_size", 0)
        for i in range(0, self.population_size):
            self.journeys.append(None)

        self.initialise = kwargs.get("initialise", 0)
        if self.initialise:
            for i in range(0, self.population_size):
                new_journey = Tour(tourmanager)
                newTour.generateIndividual()
                self.save_journey(i, new_journey)

    def save_journey(self, index, journey):
        self.journeys[index] = journey

        #self.population = []
        #if self.population_size > 0:
        #    self.population = [ind.Individual() for i in range(self.population_size)]
        #if self.chromosome_length > 0:
        #    self.population = [ind.Individual(chromosome_length=self.chromosome_length)
         #                      for i in self.population]






    def get_fittest(self, index):
        pass

    def suffle(self):
        pass
