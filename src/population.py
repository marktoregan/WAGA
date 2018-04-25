from src import journeyallocation as ja
import random


class Population(object):

    def __init__(self, **kwargs):
        self.journey_allocations = []
        self.population_size = kwargs.get("population_size", 0)
        self.available_stops = kwargs.get("available_stops", [])
        self.journey_manager = kwargs.get("journey_manager", [])
        self.preloaded_stops = kwargs.get("preloaded_stops")

        for i in range(0, self.population_size):
            self.journey_allocations.append(None)

        self.initialise = kwargs.get("initialise", False)
        if self.initialise:
            for i in range(0, self.population_size):
                new_journey_all = ja.JourneyAllocation(journey_manager=self.journey_manager,
                                                       available_stops=self.available_stops)
                new_journey_all.generate_individual()
                self.save_journey_allocation(i, new_journey_all)

    def size_of_population(self):
        return len(self.journey_allocations)

    def save_journey_allocation(self, index, journey):
        self.journey_allocations[index] = journey

    def get_journey_allocation(self, index):
        return self.journey_allocations[index]

    def get_fittest(self):
        #print('i start here')
        fittest = self.journey_allocations[0]
        for i in range(0, self.population_size):
            journ = self.get_journey_allocation(i)
            if fittest.get_fitness(self.preloaded_stops) >= journ.get_fitness(self.preloaded_stops):
                fittest = self.get_journey_allocation(i)
        return fittest