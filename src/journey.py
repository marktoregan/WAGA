import math
from datetime import datetime
from src import ev_charge_point as ecp
from src.config import mapconfig as md
from src import electricvehicle as ev


class Journey(object):
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: start_time, starting_point, end_point, stops, ev_id
        """
        self.start_time = kwargs.get("start_time", datetime.now())
        self.starting_point = kwargs.get("starting_point", [0, 0])
        self.end_point = kwargs.get("end_point", [0, 10])
        self.stops = kwargs.get("stops", ['a'])
        self.ev_id = kwargs.get("ev_id", 0)
        self.current_location = kwargs.get("current_point", [0, 5])
        self.stops = dict(kwargs.get({"stops", [{"ev_point_id": 1, "arrival_time": 0, "departure_time": 0,
                                                 "wait_time": 0}]}))

    def _euclidean_distance(self, point1, point2):
        """
        :param point1:
        :param point2:
        :return:
        """
        euclidean = math.sqrt(((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2))
        return euclidean

    def journey_distance(self):
        """
        :return:
        """
        euclidean = self._euclidean_distance(self.starting_point, self.end_point)
        mpd = md.MapConfig()
        total_distance_km = euclidean * mpd.legend_distance
        return total_distance_km

    def distance_in_minutes(self, ev, distance):
        """
        :param ev instance, distance:
        :return: time = distance / speed
        """
        #distance = self.journey_distance()
        time = distance / ev.max_speed
        time = time * 60
        return time

    def distance_from_charge_point_in_mins(self):
        ev_cp = ecp.EvChargePoint(id=1, location=[0, 5], occupied=False [0, 0], time_occupied=False,
                                              charge_time_required=25,
                                              charge_type='xyz')
        evcar = ev.ElectricVehicle(ev_id=0, range=80, max_speed=120)
        distance = self._euclidean_distance(self.current_location, ev_cp.location)
        time_from_cp = self.distance_in_minutes(evcar)
        return time_from_cp