from src import individual as ind
import random


class Population:

    def __init__(self, population_size, chromosomeLength=0):
        self.population_fitness = -1;
        self.population = ind.Individual(population_size)

        if not chromosomeLength == 0:
            pops = list
            for individualCount in range(0,population_size):
                ind1 = ind.Individual(chromosome_length=chromosomeLength)
                self.population[individualCount] = ind1

    #    public Individual getFittest(int offset) {
    #       Arrays.sort(this.population, new Comparator<Individual>() {                  
    #
    #       @Override                  
    #       public int compare(Individual o1, Individual o2) {  
    #           if (o1.getFitness() > o2.getFitness()) {                              
    #               return -1;                        
    #           }
    #           else if (o1.getFitness() < o2.getFitness()) { 
    #               return 1;
    #           }
    #           return 0;
    #       }
    #       });
    #       return this.population[offset];
    #   }

    def suffle(self):
        self.population = random.suffle(self.population)
