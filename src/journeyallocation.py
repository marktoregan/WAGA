from datetime import datetime
import random
from src import journeystop as js, journeystops as jss, ev_charge_point as evp
import tinydb

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

    def get_allocation(self, allocation_pos):
        return self.journey_allocation[allocation_pos]

    def set_allocation(self, allocation_pos, allocation):
        self.journey_allocation[allocation_pos] = allocation
        #self.fitness = 0.0
        #self.distance = 0

    def save_allocation(self, index, stop):
        self.journey_allocation[index] = stop

    def generate_individual(self):
        for i in range(0, self.journey_manager.number_of_stops()):
            allocated_stop = self.set_individual(self.available_stops)
            self.save_allocation(i, allocated_stop)

    def get_journey(self, index):
        journey = self.journey_manager[index]
        return journey

    def get_fitness(self):
        charge_time = 25
        arrival_time = datetime.now()
        journeys = list()
        for index, alloc in enumerate(self.journey_allocation):
            evp1 = evp.EvChargePoint(id=alloc)
            jour = self.journey_manager.get_journey(index)

            jour.stop = [alloc]
            stop = js.JourneyStop(ev_point_id=alloc,
                                        arrival_time=arrival_time,
                                        departure_time=0,
                                        wait_time=0,
                                        charge_time=evp1.charge_time_required)
            journeys.append(stop)
        jstops = jss.JourneyStops()
        time_total = jstops.total_time_of_stops(journeys)
        tot = 0
        #print(f'{len(self.journey_allocation)}')
        for index, alloc in enumerate(self.journey_allocation):
            jour1 = self.journey_manager.get_journey(index)
            tot += jour1.distance()
        time_total +=tot
        #print(f'{time_total}')
        return time_total

    def journey_allocation_size(self):
        return len(self.journey_allocation)