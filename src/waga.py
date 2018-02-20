from src import geneticalgorithm as ga


class Waga:

    def __init__(self):
        pass

    def main(self):
        #Timetable  timetable = initializeTimetable();

        #GeneticAlgorithm ga = new  GeneticAlgorithm(100, 0.01, 0.9, 2, 5);

        #population = ga.initPopulation(timetable);

        #ga.evalPopulation(population, timetable);

        generation = 1

        while generation <= 10:

            print("gen {}".format(generation))
            generation += 1

                #while (ga.isTerminationConditionMet(generation, 1000) == false
        #    & & ga.isTerminationConditionMet(population) == false)
        #     {
        #
        #         System.out.println("G" + generation + " Best fitness: " + population.getFittest(0).getFitness());
        #
        #         // Apply crossover
        #         population = ga.crossoverPopulation(population);
        #
        #         // Apply mutation
        #         population = ga.mutatePopulation(population, timetable);
        #
        #         // Evaluate population
        #         ga.evalPopulation(population, timetable);
        #
        #         // Increment the current generation
        #         generation++;
        #     }
        #
        # timetable.createClasses(population.getFittest(0));
        # System.out.println();
        # System.out.println("Solution found in " + generation + " generations");
        # System.out.println("Final solution fitness: " + population.getFittest(0).getFitness());
        # System.out.println("Clashes: " + timetable.calcClashes());
        #
        # System.out.println();
        # Class  classes[] = timetable.getClasses();
        # int classIndex = 1;
        # for (Class bestClass: classes) {
        #     System.out.println("Class " + classIndex + ":");
        # System.out.println("Module: " + timetable.getModule(bestClass.getModuleId()).getModuleName());
        # System.out.println("Group: " + timetable.getGroup(bestClass.getGroupId()).getGroupId());
        # System.out.println("Room: " + timetable.getRoom(bestClass.getRoomId()).getRoomNumber());
        # System.out.println("Professor: " + timetable.getProfessor(bestClass.getProfessorId()).getProfessorName());
        # System.out.println("Time: " + timetable.getTimeslot(bestClass.getTimeslotId()).getTimeslot());
        # System.out.println("-----");
        # classIndex + +;
        # }
        # }


if __name__ == '__main__':
    waga = Waga()
    waga.main()
    #gal = ga.GeneticAlgoritm(100, 0.01, 0.95, 0)
    print('hello')