from src import population as p, \
                geneticalgorithm as gen, \
                populatejourneymanager as pjm, \
                evchargepoints as evcps, \
                benchmark as bk
from src.calc import distance as dis

class RunGA(object):
    def __init__(self, **kwargs):
        jm = pjm.PopulateJourneyManager()
        self.num = kwargs.get("num_of_journeys")
        self.journey_manager = jm.get_journey_manager(self.num)
        self.available_stops = []
        self.preloaded = []
        self.population_size = kwargs.get("population_size")
        self.initialise = kwargs.get("initialise", True)
        self.generations = kwargs.get("generations", 10)

    def process(self, charge_types):

        self.available_stops, preloaded_point_details = evcps.EvChargePoints.get_ev_charge_point_by_ids(charge_types)
        #print(self.available_stops, preloaded_point_details)
        distances_loaded = self.method_name(preloaded_point_details)
        pre_loaded = {'evp_details':preloaded_point_details, 'distances':distances_loaded}

        ##print(f'Getting Initial Population.')
        #print(f'just before {len(self.journey_manager.stops)}')
        pop = p.Population(journey_manager=self.journey_manager,
                                    available_stops=self.available_stops,
                                    population_size=self.population_size,
                                    initialise=self.initialise,
                                    preloaded_stops=pre_loaded)
        #print(f'Getting Journey manager.')
        ga = gen.GeneticAlgorithm(self.journey_manager)
        #print(f'Starting evolve.')
        #print('any before here??')
        pop = ga.evolve_population(pop)
        generation_results = []

        current_res = 2
        for i in range(0, self.generations):
            pop = ga.evolve_population(pop)
            res = pop.get_fittest().get_fitness(pop.preloaded_stops)
            generation_results.append(res)
            print(f"gen {i} {generation_results[i]} ")
        #print(generation_results)
        #print(pop)
        #print(f'stops {len(pop.get_fittest().journey_allocation)}')
        #print(f'stops {pop.get_fittest().journey_allocation}')
        #print(f'fitness: {pop.get_fittest().get_fitness(pop.preloaded_stops)}')

        bench_charge_types = charge_types[:]
        ben = bk.Benchmark(journey_manager=self.journey_manager, charge_types=bench_charge_types)
        ben_result = ben.run(pre_loaded)
        fit = pop.get_fittest().get_fitness(pop.preloaded_stops)
        benres = ben_result
        return fit, benres

    def method_name(self, preloaded_point_details):
        journeys_pre = [[(j.starting_point[0], j.starting_point[1]), (j.end_point[0], j.end_point[1])] for j in
                        self.journey_manager.stops]
        stops_pre = [(v.location[0], v.location[1]) for k, v in preloaded_point_details.items()]
        pp = dis.Distance(stops=stops_pre, journeys=journeys_pre)
        journey_dict = pp.populate()
        return journey_dict

    def benchmark(self):
        print(self.journey_manager)