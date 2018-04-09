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

    journey1 = jy.Journey(start_time=time1, starting_point=[0, 0],end_point=[0, 10], stop=["a"] )
    journey_manager.add_journey(journey1)

    journey2 = jy.Journey(start_time=time1, starting_point=[0, 1],end_point=[0, 9], stop=["a"])
    journey_manager.add_journey(journey2)

    journey3 = jy.Journey(start_time=time1, starting_point=[0, 2],end_point=[0, 8], stop=["a"])
    journey_manager.add_journey(journey3)

    journey4 = jy.Journey(start_time=time1, starting_point=[0, 3],end_point=[0, 7], stop=["a"])
    journey_manager.add_journey(journey4)

    journey5 = jy.Journey(start_time=time1, starting_point=[0, 4],end_point=[0, 6], stop=["a"])
    journey_manager.add_journey(journey5)

    journey6 = jy.Journey(start_time=time5, starting_point=[0, 1],end_point=[0, 5], stop=["a"])
    journey_manager.add_journey(journey6)

    journey7 = jy.Journey(start_time=time5, starting_point=[0, 2],end_point=[0, 10], stop=["a"])
    journey_manager.add_journey(journey7)

    journey8 = jy.Journey(start_time=time5, starting_point=[0, 3],end_point=[0, 9], stop=["a"])
    journey_manager.add_journey(journey8)

    journey9 = jy.Journey(start_time=time5, starting_point=[0, 4],end_point=[0, 8], stop=["a"])
    journey_manager.add_journey(journey9)

    journey10 = jy.Journey(start_time=time5, starting_point=[0, 5],end_point=[0, 7], stop=["a"])
    journey_manager.add_journey(journey10)

    available_stops = ['a', 'b', 'c', 'd', 'e']

    print(journey1.total_journey_time)


    # pop = p.Population(journey_manager=journey_manager,
    #                             available_stops=available_stops,
    #                             population_size=20,
    #                             initialise=True)
    #
    # print(f'get fittest')
    # fittest_allocation = pop.get_fittest()
    # print(f'have fittest')
    #
    # ga = gen.GeneticAlgorithm(journey_manager)
    # pop = ga.evolve_population(pop)
    # for i in range(0, 100):
    #     print(f'gen {i}')
    #     pop = ga.evolve_population(pop)
    #
    #
    # print("Finished")
    # print(f"Final distance {pop.get_fittest().get_fitness()} ")
    # print(f"Solution: {pop.get_fittest().get_fitness()} journey {pop.get_fittest().journey_allocation}" )
