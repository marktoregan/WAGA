from datetime import datetime
import random

from src import journeystop as js, journeystops as jss

class JourneyAllocation(object):

    def __init__(self, **kwargs):
        self.journey_allocation = []
        self.journey_manager = kwargs.get("journey_manager")
        self.available_stops = kwargs.get("available_stops")
        for i in range(0, self.journey_manager.number_of_stops()):
            self.journey_allocation.append(None)

    def set_individual(self, stops):
        stop = random.choice(stops)
        return stop

    def save_allocation(self, index, stop):
        self.journey_allocation[index] = stop

    def generate_individual(self):
        for i in range(0, self.journey_manager.number_of_stops()):
            allocated_stop = self.set_individual(self.available_stops)
            self.save_allocation(i, allocated_stop)

    def get_fitness(self):
        charge_time = 25
        ctime = datetime.now()
        journeys = list()
        for alloc in self.journey_allocation:
            stop = js.JourneyStop(ev_point_id=alloc,
                                        arrival_time=ctime,
                                        departure_time=0,
                                        wait_time=0,
                                        charge_time=charge_time)
            journeys.append(stop)
        jstops = jss.JourneyStops()
        time_total = jstops.total_time_of_stops(journeys)
        print(f'score {time_total} for {self.journey_allocation}')
        return time_total