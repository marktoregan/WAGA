import random
from src import population as p, journeyallocation as ja


CLASS GeneticAlgorithm:
      
    FUNCTION __init__(self, journey_manager):
         journey_manager <- journey_manager
         mutation_rate <- 0.015
         tournament_size <- 5
         elitism <- True
    ENDFUNCTION

ENDCLASS


    FUNCTION evolve_population(self, pop):
        newPopulation <- p.Population(journey_manager= journey_manager, population_size=pop.size_of_population(), initialise=False)
        elitismOffset <- 0
        IF  elitism:
            newPopulation.save_journey_allocation(0, pop.get_fittest())
            elitismOffset <- 1
        ENDIF
        for i in range(elitismOffset, newPopulation.size_of_population()):
            parent1 <-  tournamentSelection(pop)
            parent2 <-  tournamentSelection(pop)
            child <-  crossover(parent1, parent2)
            newPopulation.save_journey_allocation(i, child)
        ENDFOR
        for i in range(elitismOffset, newPopulation.size_of_population()):
             mutate(newPopulation.get_journey_allocation(i))
    ENDFUNCTION

        ENDFOR

        RETURN newPopulation

    FUNCTION crossover(self, parent1, parent2):
        child <- ja.JourneyAllocation(journey_manager= journey_manager)
        startPos <- int(random.random() * parent1.journey_allocation_size())
        endPos <- int(random.random() * parent1.journey_allocation_size())
    ENDFUNCTION


        for i in range(0, child.journey_allocation_size()):
            IF startPos < endPos AND i > startPos AND i < endPos:
                child.set_allocation(i, parent1.get_allocation(i))
            ELSEIF startPos > endPos:
                IF not (i < startPos AND i > endPos):
                    child.set_allocation(i, parent1.get_allocation(i))
            ENDIF
                ENDIF
        ENDFOR

        for i in range(0, parent2.journey_allocation_size()):
            for ii in range(0, child.journey_allocation_size()):
                IF child.get_allocation(ii) = None:
                    child.set_allocation(ii, parent2.get_allocation(i))
                    break
                ENDIF
        ENDFOR
            ENDFOR
        RETURN child

    FUNCTION mutate(self, journey_allocation):
        for allocationPos1 in range(0, journey_allocation.journey_allocation_size()):
            IF random.random() <  mutation_rate:
                allocationPos2 <- int(journey_allocation.journey_allocation_size() * random.random())
            ENDIF
    ENDFUNCTION

        ENDFOR

                allocation1 <- journey_allocation.get_allocation(allocationPos1)
                allocation2 <- journey_allocation.get_allocation(allocationPos2)

                journey_allocation.set_allocation(allocationPos2, allocation1)
                journey_allocation.set_allocation(allocationPos1, allocation2)

    FUNCTION tournamentSelection(self, pop):
        tournament <- p.Population(journey_manager= journey_manager,
                                  population_size= tournament_size,
                                  initialise=False)
        for i in range(0,  tournament_size):
            randomId <- int(random.random() * pop.size_of_population())
            tournament.save_journey_allocation(i, pop.get_journey_allocation(randomId))
        ENDFOR
        fittest <- tournament.get_fittest()
        RETURN fittest
    ENDFUNCTION



