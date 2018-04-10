import random
from datetime import datetime
from src import journeystop as js, journeystops as jss


class Benchmark(object):

    def __init__(self, **kwargs):
        self.random_allocation = []
        self.journey_manager = kwargs.get("journey_manager")
        self.stops_available = kwargs.get("stops")
        for journey in self.journey_manager:
            self.random_allocation.append(random.choice(self.stops_available))

    def get_random_fitness(self):
        charge_time = 25
        ctime = datetime.now()
        journeys = list()
        for alloc in self.random_allocation:
            stop = js.JourneyStop(ev_point_id=alloc,
                                        arrival_time=ctime,
                                        departure_time=0,
                                        wait_time=0,
                                        charge_time=charge_time)
            journeys.append(stop)
        jstops = jss.JourneyStops()
        time_total = jstops.total_time_of_stops(journeys)
        return time_total

