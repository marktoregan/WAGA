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
        distances_loaded = self.method_name(preloaded_point_details)
        pre_loaded = {'evp_details':preloaded_point_details, 'distances':distances_loaded}

        pop = p.Population(journey_manager=self.journey_manager,
                                    available_stops=self.available_stops,
                                    population_size=self.population_size,
                                    initialise=self.initialise,
                                    preloaded_stops=pre_loaded)
        ga = gen.GeneticAlgorithm(self.journey_manager)
        pop = ga.evolve_population(pop)
        generation_results = []

        current = None
        prev = None
        converge_count = 0
        convered_at = 0

        for i in range(0, self.generations):
            if current == prev:
                converge_count += 1
            else:
                converge_count = 1
            if converge_count == 20:
                convered_at = i
                break

            pop = ga.evolve_population(pop)
            res = pop.get_fittest().get_fitness(pop.preloaded_stops)
            generation_results.append(res)
            current = res
            prev = generation_results[i - 1]
            #print(f"gen {i} {generation_results[i]} ")

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