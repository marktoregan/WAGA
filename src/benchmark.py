from src import populatejourneymanager as pjm, evchargepoint as evp, journeystop as js, journeystops as jss
from src.calc import distance as dis
from datetime import datetime
from scipy.spatial import distance
from collections import namedtuple
import random


class Benchmark(object):

    def __init__(self, **kwargs):
        #jm = pjm.PopulateJourneyManager()
        self.journey_manager = kwargs.get("journey_manager",0)
        self.charge_type = kwargs.get("charge_types")
        self.journey_allocation = []


    def midpoint(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        point = ((x1 + x2) / 2, (y1 + y2) / 2)
        return point

    def midpoints(self):
        cpoints = evp.EvChargePoint()
        all_points, all = cpoints.get_ev_charge_point_by_ids(self.charge_type)
        evps_locations = list(map(lambda x: (x.location), all_points))
        mid_points = []
        for j in self.journey_manager.stops:
            mid = (self.midpoint(j.starting_point, j.end_point))
            p = self.closest_node(mid, evps_locations)
            mid_points.append(p)
        return mid_points

    def closest_node(self, node, nodes):
        closest_index = distance.cdist([node], nodes).argmin()
        return nodes[closest_index]

    #build allocation list is broken, just pass in the existing one!!
    #In fact this is not broken,  they are two diffenet lists!! Just get rid of the pre-loaded one below,
    # load youself from db
    def build_allocation_list(self, midpoints):
        cpoints = evp.EvChargePoint()
        all_points, all = cpoints.get_ev_charge_point_by_ids(self.charge_type)
        ## cpoints.get_ev_charge_point_by_location(midpoints)
        for mid in midpoints:
            filter_points = list(filter(lambda x: x.location == mid, all_points))
            alloc = random.choice(filter_points)
            self.journey_allocation.append(alloc.id)

    def get_fitness(self):
        arrival_time = datetime.now()
        journeys = list()
        for index, allocation in enumerate(self.journey_allocation):
            ev_point = evp.EvChargePoint(id=allocation)
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
            ev = evp.EvChargePoint()
            ev_point = ev_point.get_ev_charge_point(alloc)
            #JourneyConfig = namedtuple("JourneyConfig", ["ev_stop", "point"])
            disobj = dis.Distance([],1)
            start_dis = disobj.distance_between_points(a_journey.starting_point, ev_point.location)
            ed_dis = disobj.distance_between_points(ev_point.location,a_journey.end_point)

            tots = start_dis + ed_dis
            time = tots / 100
            time *= 60
            journey_time += time
        total_time = charge_time_total + journey_time
        return total_time

    def run(self, preloaded):
        midpoints = self.midpoints()
        self.build_allocation_list(midpoints)
        #print(self.journey_allocation)
        totals = self.get_fitness()
        return totals






