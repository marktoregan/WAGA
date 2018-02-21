import math
from datetime import datetime

from src.config import mapconfig as md


class Journey(object):
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: start_time, starting_point, end_point, stops, ev_id
        """
        self.start_time = kwargs.get("start_time", datetime.now())
        self.starting_point = kwargs.get("starting_point", '0,0')
        self.end_point = kwargs.get("end_point", '0,10')
        self.stops = kwargs.get("stops", ['a'])
        self.ev_id = kwargs.get("ev_id", 0)

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

    def journey_time_minutes(self, ev):
        """
        :param electric vehicle instance:
        :return: time = distance / speed
        """
        distance = self.journey_distance()
        time = distance / ev.max_speed
        time = time * 60
        return time
