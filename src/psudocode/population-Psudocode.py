from src import journeyallocation as ja
import random


CLASS Population(object):
ENDCLASS


    FUNCTION __init__(self, **kwargs):
         journey_allocations <- []
         population_size <- kwargs.get("population_size", 0)
         available_stops <- kwargs.get("available_stops", [])
         journey_manager <- kwargs.get("journey_manager", [])
    ENDFUNCTION


        for i in range(0,  population_size):
             journey_allocations.append(None)
        ENDFOR

         initialise <- kwargs.get("initialise", False)
        IF  initialise:
            for i in range(0,  population_size):
                new_journey_all <- ja.JourneyAllocation(journey_manager= journey_manager,
                                                       available_stops= available_stops)
                new_journey_all.generate_individual()
                 save_journey_allocation(i, new_journey_all)
        ENDIF
            ENDFOR

    FUNCTION size_of_population(self):
        RETURN len( journey_allocations)
    ENDFUNCTION


    FUNCTION save_journey_allocation(self, index, journey):
         journey_allocations[index] <- journey
    ENDFUNCTION


    FUNCTION get_journey_allocation(self, index):
        RETURN  journey_allocations[index]
    ENDFUNCTION


    FUNCTION get_fittest(self):
        fittest <-  journey_allocations[0]
        for i in range(0,  population_size):
            journ <-  get_journey_allocation(i)
            IF fittest.get_fitness() >= journ.get_fitness():
                fittest <-  get_journey_allocation(i)
            ENDIF
        ENDFOR
        RETURN fittes
