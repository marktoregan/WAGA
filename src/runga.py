from src import journey as jy
from src import journeymanager as jm
from src import population as pop
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

    available_stops = ['a','b','c','d','e']

    population = pop.Population(journey_manager=journey_manager, available_stops=available_stops, population_size=20, initialise=True)

    for p in population.journey_allocations:
        print(f'{p.journey_allocation}')

