import math
from datetime import datetime

from src.config import mapconfig as md


class Journey(object):
    def __init__(self, **kwargs):
        self.start_time = kwargs.get("start_time", datetime.now())
        self.starting_point = kwargs.get("starting_point", '0,0')
        self.end_point = kwargs.get("end_point", '0,10')
        self.stops = kwargs.get("stops", ['a'])

    def _euclidean_distance(self, point1, point2):
        euclidean = math.sqrt(((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2))
        return euclidean

    def journey_distance(self):
        euclidean = self._euclidean_distance(self.starting_point, self.end_point)
        mpd = md.MapConfig()
        total_distance_km = euclidean * mpd.legend_distance
        return total_distance_km
