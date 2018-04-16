from src import population as p, geneticalgorithm as gen, benchmark as bk, populatejourneymanager as pjm



if __name__ == '__main__':

    jm = pjm.PopulateJourneyManager()
    journey_manager = jm.get_journey_manager(20)
    available_stops = ['a', 'b', 'c', 'd', 'e']

    pop = p.Population(journey_manager=journey_manager,
                                available_stops=available_stops,
                                population_size=20,
                                initialise=True)

    print(f'fittest')
    fittest_allocation = pop.get_fittest()
    print(f"Initial fitness: {fittest_allocation.get_fitness()} stops {fittest_allocation.journey_allocation}")

    ga = gen.GeneticAlgorithm(journey_manager)
    pop = ga.evolvePopulation(pop)
    for i in range(0, 100):
        pop = ga.evolvePopulation(pop)
        print(f'generation: {i} and best score: {pop.get_fittest().get_fitness()}')

    # Print final results
    print("Finished")
    print(f"Final distance {pop.get_fittest().get_fitness()} ")
    print(f"Solution: {pop.get_fittest().get_fitness()} and the EVP allocated {pop.get_fittest().journey_allocation}")
    allocations = pop.get_fittest().journey_allocation
    my_dict = {i:allocations.count(i) for i in allocations}
    print(f'count {my_dict}')
    bench = bk.Benchmark(journey_manager=journey_manager.stops, stops=available_stops)

    print(f'Random soultion: {bench.get_random_fitness()} and {bench.random_allocation}')
    ran_allocations = bench.random_allocation
    my_dict_random = {i: ran_allocations.count(i) for i in ran_allocations}
    print(f'count {my_dict_random}')