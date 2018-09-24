from src import geneticalgorithm as ga


class Waga:

    def __init__(self):
        pass

    def main(self):
        #Timetable  timetable = initializeTimetable();

        #journey_table = initialize_journey_table

        #GeneticAlgorithm ga = new  GeneticAlgorithm(100, 0.01, 0.9, 2, 5);

        #population = ga.initPopulation(timetable);

        #ga.evalPopulation(population, timetable);

        generation = 0

        while generation <= 10:
            generation += 1
            print("G {} + Best fitness: + population.getFittest(0).getFitness()".format(generation))
        #
        #Apply crossover
        #         population = ga.crossoverPopulation(population);
        #
        #Apply mutation
        #         population = ga.mutatePopulation(population, timetable);
        #
        #Evaluate population
        #         ga.evalPopulation(population, timetable);
        #
        #Increment the current generation
        #         generation++;
        #     }
        #
        # print results


if __name__ == '__main__':
    waga = Waga()
    waga.main()
    #gal = ga.GeneticAlgoritm(100, 0.01, 0.95, 0)
    print('hello')