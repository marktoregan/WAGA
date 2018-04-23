from src import population as p, \
                geneticalgorithm as gen, \
                populatejourneymanager as pjm


CLASS RunGA(object):
    FUNCTION __init__(self, **kwargs):
        jm <- pjm.PopulateJourneyManager()
         journey_manager <- jm.get_journey_manager(2)
         available_stops <- kwargs.get("available_stops", [])
         population_size <- kwargs.get("population_size", 20)
         initialise <- kwargs.get("initialise", True)
         generations <- kwargs.get("generations", 10)
    ENDFUNCTION

ENDCLASS


    FUNCTION process(self):
        pop <- p.Population(journey_manager= journey_manager,
                                    available_stops= available_stops,
                                    population_size= population_size,
                                    initialise= initialise)
        ga <- gen.GeneticAlgorithm( journey_manager)
        pop <- ga.evolve_population(pop)
        generation_results <- [None] *  generations
        for i in range(0,  generations):
            pop <- ga.evolve_population(pop)
            generation_results[i] <- pop.get_fittest().get_fitness()
        ENDFOR
        RETURN generation_results, pop
