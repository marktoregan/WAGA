from src import population as p, \
                geneticalgorithm as gen, \
                populatejourneymanager as pjm


class RunGA(object):
    def __init__(self, **kwargs):
        jm = pjm.PopulateJourneyManager()
        self.journey_manager = jm.get_journey_manager(2)
        self.available_stops = kwargs.get("available_stops", [])
        self.population_size = kwargs.get("population_size", 20)
        self.initialise = kwargs.get("initialise", True)
        self.generations = kwargs.get("generations", 10)

    def process(self):

        print(f'Getting Initial Population.')

        #pre_loaded_stop_info =
        pop = p.Population(journey_manager=self.journey_manager,
                                    available_stops=self.available_stops,
                                    population_size=self.population_size,
                                    initialise=self.initialise)
        print(f'Getting Journey manager.')
        ga = gen.GeneticAlgorithm(self.journey_manager)
        print(f'Starting evolve.')
        print('any before here??')
        #load

        self.pre_load(self.available_stops)
        #endload
        pop = ga.evolve_population(pop)
        generation_results = [None] * self.generations

        for i in range(0, self.generations):
            print(f'gen {i}')
            pop = ga.evolve_population(pop)
            generation_results[i] = pop.get_fittest().get_fitness()

        print(generation_results)
        print(pop)
        print(f'stops {pop.get_fittest().journey_allocation}')
        #
        print(f'fitness: {pop.get_fittest().get_fitness()}')

    def pre_load(self, stops):
        for s in stops:
            print(f'{s}')
