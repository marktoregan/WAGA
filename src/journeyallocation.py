from src import journeystop as js, journeystops as jss, evchargepoint as evp
from datetime import datetime
import random
from collections import namedtuple


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

    def get_fitness(self, preloaded):
        arrival_time = datetime.now()
        journeys = list()
        for index, allocation in enumerate(self.journey_allocation):
            ev_point = preloaded['evp_details'].get(allocation) #evp.EvChargePoint(id=allocation)
            journey = self.journey_manager.get_journey(index)
            journey.stop = [allocation]
            stop = js.JourneyStop(ev_point_id=allocation,
                                        arrival_time=arrival_time,
                                        departure_time=0,
                                        wait_time=0,
                                        charge_time=ev_point.charge_time_required)
            journeys.append(stop)
        jstops = jss.JourneyStops()
        charge_time_total = jstops.total_time_of_stops(journeys)
        journey_time = 0

        for index, alloc in enumerate(self.journey_allocation):
            a_journey = self.journey_manager.get_journey(index)
            ev_point = preloaded['evp_details'].get(alloc)
            JourneyConfig = namedtuple("JourneyConfig", ["ev_stop", "point"])

            point_start = JourneyConfig(ev_stop=(ev_point.location[0],ev_point.location[1]),
                                        point=(a_journey.starting_point[0], a_journey.starting_point[1]))

            point_end = JourneyConfig(ev_stop=(ev_point.location[0], ev_point.location[1]),
                                       point=(a_journey.end_point[0], a_journey.end_point[1]))
            start_dis = preloaded['distances'][point_start]
            ed_dis = preloaded['distances'][point_end]
            tots = start_dis + ed_dis
            time = tots / 100
            time *= 60
            journey_time += time
        total_time = charge_time_total + journey_time

        return total_time

    def journey_allocation_size(self):
        return len(self.journey_allocation)