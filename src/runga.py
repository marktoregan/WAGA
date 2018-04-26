from src import population as p, \
                geneticalgorithm as gen, \
                populatejourneymanager as pjm, \
                evchargepoints as evcps
from src.calc import distance as dis
from collections import namedtuple


class RunGA(object):
    def __init__(self, **kwargs):
        jm = pjm.PopulateJourneyManager()
        self.journey_manager = jm.get_journey_manager(2)
        self.available_stops = []
        self.preloaded = []
        self.population_size = kwargs.get("population_size", 200)
        self.initialise = kwargs.get("initialise", True)
        self.generations = kwargs.get("generations", 10)

    def process(self):

        self.available_stops, preloaded = evcps.EvChargePoints.get_by_type(["Fast AC Type-2 44kW"])

        print(f'Getting Initial Population.')

        ##Start pre load surgey
        journeys_pre = [[(j.starting_point[0], j.starting_point[1]), (j.end_point[0], j.end_point[1])] for j in
                        self.journey_manager.stops]

        stops_pre = [(v.location[0], v.location[1]) for k, v in preloaded.items()]


        #stops = [(9, 9), (8, 8), (7, 6)]
        #journeys = [[(0, 0), (1, 1)], [(2, 3), (3, 3)]]

        pp = dis.Distance(stops=stops_pre, journeys=journeys_pre)
        journey_dict = pp.populate()
        print(journey_dict)

        JourneyConfig = namedtuple("JourneyConfig", ["ev_stop", "point"])
        lookup_tup = JourneyConfig(ev_stop=(25.59, 25.9), point=(36.17, 27.27))
        lookup_tup1 = JourneyConfig(ev_stop=(25.59, 25.9), point=(49.21, 85.39))
        print(lookup_tup)
        print(journey_dict)
        #print(f' {journey_dict[lookup_tup]} + {journey_dict[lookup_tup1]} = {journey_dict[lookup_tup] + journey_dict[lookup_tup1]}')
        ##End pre load surgey


        #pre_loaded_stop_info =
        pop = p.Population(journey_manager=self.journey_manager,
                                    available_stops=self.available_stops,
                                    population_size=self.population_size,
                                    initialise=self.initialise,
                                    preloaded_stops=preloaded)
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

    def pre_load(self, stops):
        for s in stops:
            print(f'{s}')
