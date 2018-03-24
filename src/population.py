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

    def get_journey(self, index):
        return self.journey_allocations[index]

    def get_fittest(self):
        fittest = self.journey_allocations[0]
        for i in range(0, self.population_size):
            if fittest.get_fitness() >= self.get_journey(i).get_fitness():
                fittest = self.get_journey(i)
        return fittest
