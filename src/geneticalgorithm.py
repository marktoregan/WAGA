import random
from src import population as p, journeyallocation as ja


class GeneticAlgorithm:
      
    def __init__(self, journey_manager):
        self.journey_manager = journey_manager
        self.mutation_rate = 0.015
        self.tournament_size = 5
        self.elitism = True

    def evolve_population(self, pop):
        #print('evolve')
        newPopulation = p.Population(journey_manager=self.journey_manager, population_size=pop.size_of_population(),
                                     initialise=False,
                                     preloaded_stops=pop.preloaded_stops)
        elitismOffset = 0
        if self.elitism:
            newPopulation.save_journey_allocation(0, pop.get_fittest())
            elitismOffset = 1
        for i in range(elitismOffset, newPopulation.size_of_population()):
            parent1 = self.tournamentSelection(pop)
            parent2 = self.tournamentSelection(pop)
            child = self.crossover(parent1, parent2)
            newPopulation.save_journey_allocation(i, child)
        for i in range(elitismOffset, newPopulation.size_of_population()):
            self.mutate(newPopulation.get_journey_allocation(i))
        return newPopulation

    def crossover(self, parent1, parent2):
        #print(f'crossover')
        child = ja.JourneyAllocation(journey_manager=self.journey_manager)
        startPos = int(random.random() * parent1.journey_allocation_size())
        endPos = int(random.random() * parent1.journey_allocation_size())

        for i in range(0, child.journey_allocation_size()):
            if startPos < endPos and i > startPos and i < endPos:
                child.set_allocation(i, parent1.get_allocation(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.set_allocation(i, parent1.get_allocation(i))

        for i in range(0, parent2.journey_allocation_size()):
            for ii in range(0, child.journey_allocation_size()):
                if child.get_allocation(ii) == None:
                    child.set_allocation(ii, parent2.get_allocation(i))
                    break
        return child

    def mutate(self, journey_allocation):
        for allocationPos1 in range(0, journey_allocation.journey_allocation_size()):
            if random.random() < self.mutation_rate:
                #print('does mutate')
                allocationPos2 = int(journey_allocation.journey_allocation_size() * random.random())

                allocation1 = journey_allocation.get_allocation(allocationPos1)
                allocation2 = journey_allocation.get_allocation(allocationPos2)

                journey_allocation.set_allocation(allocationPos2, allocation1)
                journey_allocation.set_allocation(allocationPos1, allocation2)

    def tournamentSelection(self, pop):
        #print('t')
        tournament = p.Population(journey_manager=self.journey_manager,
                                  population_size=self.tournament_size,
                                  initialise=False,
                                  preloaded_stops=pop.preloaded_stops)
        for i in range(0, self.tournament_size):
            randomId = int(random.random() * pop.size_of_population())
            tournament.save_journey_allocation(i, pop.get_journey_allocation(randomId))
        fittest = tournament.get_fittest()
        return fittest


