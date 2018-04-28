from src import population as p, \
                geneticalgorithm as gen, \
                populatejourneymanager as pjm, \
                evchargepoints as evcps
from src.calc import distance as dis
from collections import namedtuple


class RunGA(object):
    def __init__(self, **kwargs):
        jm = pjm.PopulateJourneyManager()
        self.journey_manager = jm.get_journey_manager(10)
        self.available_stops = []
        self.preloaded = []
        self.population_size = kwargs.get("population_size", 200)
        self.initialise = kwargs.get("initialise", True)
        self.generations = kwargs.get("generations", 10)

    def process(self):
        self.available_stops, preloaded_point_details = evcps.EvChargePoints.get_by_type(['Fast AC Type-2 44kW',
                                                                                          'Fast AC Type-2 50kW'
                                                                                            'CHAdeMO DC 44kW',
                                                                                            'Fast AC Type-2 43kW',
                                                                                            'Fast AC Type-2 44kW',
                                                                                            'Fast AC Type-2 50kW',
                                                                                            'CHAdeMO DC 45kW',
                                                                                            'CHAdeMO DC 50kW',
                                                                                            'CHAdeMO DC 22kW',
                                                                                            'Combo DC 44kW',
                                                                                            'Combo DC 45kW',
                                                                                            'Combo DC 50kW'])
        print(self.available_stops)
        print(f'Getting Initial Population.')

        ##strt
        distances_loaded = self.method_name(preloaded_point_details)
        print(distances_loaded)
        pre_loaded = {'evp_details':preloaded_point_details, 'distances':distances_loaded}

        pop = p.Population(journey_manager=self.journey_manager,
                                    available_stops=self.available_stops,
                                    population_size=self.population_size,
                                    initialise=self.initialise,
                                    preloaded_stops=pre_loaded)
        print(f'Getting Journey manager.')
        ga = gen.GeneticAlgorithm(self.journey_manager)
        print(f'Starting evolve.')
        print('any before here??')
        #load

        #self.pre_load(self.available_stops)
        #endload
        pop = ga.evolve_population(pop)
        generation_results = [None] * self.generations

        for i in range(0, self.generations):
            print(f'gen {i}')
            pop = ga.evolve_population(pop)
            generation_results[i] = pop.get_fittest().get_fitness(pop.preloaded_stops)

        print(generation_results)
        print(pop)
        print(f'stops {pop.get_fittest().journey_allocation}')
        #
        print(f'fitness: {pop.get_fittest().get_fitness(pop.preloaded_stops)}')


    def method_name(self, preloaded_point_details):
        journeys_pre = [[(j.starting_point[0], j.starting_point[1]), (j.end_point[0], j.end_point[1])] for j in
                        self.journey_manager.stops]
        stops_pre = [(v.location[0], v.location[1]) for k, v in preloaded_point_details.items()]
        pp = dis.Distance(stops=stops_pre, journeys=journeys_pre)
        journey_dict = pp.populate()

        return journey_dict

    def benchmark(self):
        print(self.journey_manager)