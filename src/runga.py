from src import journeymanager as jm, population as p, journey as jy, geneticalgorithm as gen
from datetime import datetime


if __name__ == '__main__':
    journey_manager = jm.JourneyManager()
    start_time = datetime.now()

    time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
    #time2 = datetime(year=2018, month=2, day=27, hour=13, minute=30)
    #time3 = datetime(year=2018, month=2, day=27, hour=14, minute=00)
    #time4 = datetime(year=2018, month=2, day=27, hour=14, minute=30)
    time5 = datetime(year=2018, month=2, day=27, hour=15, minute=00)

    journey1 = jy.Journey(start_time=time1)
    journey_manager.add_journey(journey1)
    journey2 = jy.Journey(start_time=time1)
    journey_manager.add_journey(journey2)
    journey3 = jy.Journey(start_time=time1)
    journey_manager.add_journey(journey3)
    journey4 = jy.Journey(start_time=time1)
    journey_manager.add_journey(journey4)
    journey5 = jy.Journey(start_time=time1)
    journey_manager.add_journey(journey5)

    journey6 = jy.Journey(start_time=time5)
    journey_manager.add_journey(journey6)
    journey7 = jy.Journey(start_time=time5)
    journey_manager.add_journey(journey7)
    journey8 = jy.Journey(start_time=time5)
    journey_manager.add_journey(journey8)
    journey9 = jy.Journey(start_time=time5)
    journey_manager.add_journey(journey9)
    journey10 = jy.Journey(start_time=time5)
    journey_manager.add_journey(journey10)

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

    # Print final results
    print("Finished")
    print(f"Final distance {pop.get_fittest().get_fitness()} ")
    print(f"Solution: {pop.get_fittest().get_fitness()} journey {pop.get_fittest().journey_allocation}" )
