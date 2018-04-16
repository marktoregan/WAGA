from src import journeymanager as jm, \
                population as p, \
                journey as jy, \
                geneticalgorithm as gen, \
                populatejourneymanager as pjm


class RunGA(object):
    def __init__(self, **kwargs):
        jm = pjm.PopulateJourneyManager()
        self.journey_manager = jm.get_journey_manager(20)
        self.available_stops = kwargs.get("available_stops", [])
        self.population_size = kwargs.get("population_size", 20)
        self.initialise = kwargs.get("initialise", True)
        self.generations = kwargs.get("generations", 10)

    def process(self):
        pop = p.Population(journey_manager=self.journey_manager,
                                    available_stops=self.available_stops,
                                    population_size=self.population_size,
                                    initialise=self.initialise)

        fittest_allocation = pop.get_fittest()
        print(f'Initial fittest {fittest_allocation}')

        ga = gen.GeneticAlgorithm(self.journey_manager)
        pop = ga.evolve_population(pop)
        for i in range(0, self.generations):
            pop = ga.evolve_population(pop)
            print(f'Generation: {i} fittest: {pop.get_fittest().get_fitness()}')

        print("Finished")
        print(f"Final distance {pop.get_fittest().get_fitness()} ")
        print(f"Solution: {pop.get_fittest().get_fitness()} journey {pop.get_fittest().journey_allocation}" )
