from src import individual as ind
from src import journeyallocation as ja
import random


class Population(object):

    def __init__(self, **kwargs):
        self.journey_allocations = []
        self.population_size = kwargs.get("population_size", 0)
        self.available_stops = kwargs.get("available_stops", [])
        self.journey_manager = kwargs.get("journey_manager", [])
        for i in range(0, self.population_size):
            self.journey_allocations.append(None)

        self.initialise = kwargs.get("initialise", False)

        if self.initialise:
            for i in range(0, self.population_size):
                new_journey_all = ja.JourneyAllocation(journey_manager=self.journey_manager, available_stops=self.available_stops)
                new_journey_all.generate_individual()
                self.save_journey(i, new_journey_all)

    def save_journey(self, index, journey):
        self.journey_allocations[index] = journey

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
