import math
from datetime import datetime, timedelta
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
        self.ev_id = kwargs.get("ev_id", 0)
        self.current_location = kwargs.get("current_point", [0, 5])
        self.stops = dict(kwargs.get("stops", {"stops": {"ev_point_id": 1,
                                                         "arrival_time": datetime.now(),
                                                         "departure_time": 0, "wait_time": 0}}))

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

    def distance_in_minutes(self, ev1):
        """
        :param ev1:
        :return: time = distance / speed
        """
        distance = self.journey_distance()
        time = distance / ev1.max_speed
        time *= 60
        return time

    def journey_distance_2(self, evp):
        """
        :return:
        """
        euclidean = self._euclidean_distance(self.current_location, evp.location)
        mpd = md.MapConfig()
        total_distance_km = euclidean * mpd.legend_distance
        return total_distance_km

    def distance_in_minutes_2(self, ev1, evp):
        """
        :param ev1:
        :param evp:
        :return: time = distance / speed
        """
        total_distance_km = self.journey_distance_2(evp)
        time = total_distance_km / ev1.max_speed
        time *= 60
        return time

    def set_arrival_time(self, ev1, evp):
        time_from_cp = self.distance_in_minutes_2(ev1, evp)
        ct = self.stops["stops"]["arrival_time"]
        now_plus_10 = ct + timedelta(minutes=time_from_cp)
        self.stops["stops"]["arrival_time"] = now_plus_10

    def get_arrival_time(self):
        return self.stops["stops"]["arrival_time"]

    def set_departure_time(self, evp):
        self.stops["stops"]["departure_time"] += evp.charge_time_required

    def get_departure_time(self):
        return self.stops["stops"]["departure_time"]


