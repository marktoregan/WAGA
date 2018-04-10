from src import journeymanager as jm, population as p, journey as jy, geneticalgorithm as gen, benchmark as bk
from datetime import datetime


if __name__ == '__main__':
    journey_manager = jm.JourneyManager()
    start_time = datetime.now()
    journey1 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey1)
    journey2 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey2)
    journey3 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey3)
    journey4 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey4)
    journey5 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey5)
    journey6 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey6)
    journey7 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey7)
    journey8 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey8)
    journey9 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey9)
    journey10 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey10)

    journey11 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey11)
    journey12 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey12)
    journey13 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey13)
    journey14 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey14)
    journey15 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey15)
    journey16 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey16)
    journey17 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey17)
    journey18 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey18)
    journey19 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey19)
    journey20 = jy.Journey(start_time=start_time)
    journey_manager.add_journey(journey20)

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
        #print(f'generation: {i}')
        pop = ga.evolvePopulation(pop)

    # Print final results
    print("Finished")
    print(f"Final distance {pop.get_fittest().get_fitness()} ")
    print(f"Solution: {pop.get_fittest().get_fitness()} journey {pop.get_fittest().journey_allocation}" )

    bench = bk.Benchmark(journey_manager=journey_manager.stops, stops=available_stops)

    print(f'Random: {bench.get_random_fitness()}')