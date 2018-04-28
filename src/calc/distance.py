import math
from src.config import mapconfig as md
from collections import namedtuple


class Distance(object):
        def __init__(self, stops, journeys):
            self.stops = stops
            self.journeys = journeys

        def _euclidean_distance(self, point1, point2):
            euclidean = math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))
            return euclidean

        def distance_between_points(self, p1, p2):
            mpd = md.MapConfig()
            dist = self._euclidean_distance(p1, p2)
            distance_in_km = dist * mpd.legend_distance
            return distance_in_km

        def populate(self):
            populated = self.create_dict()
            populated = self.insert_distance(populated)
            return populated

        def create_dict(self):
            JourneyConfig = namedtuple("JourneyConfig", ["ev_stop", "point"])
            journey_dict = {}
            for i, stop in enumerate(self.stops):
                for j, journey in enumerate(self.journeys):
                    tup = JourneyConfig(ev_stop=stop, point=journey[0])
                    tup1 = JourneyConfig(ev_stop=stop, point=journey[1])
                    if tup not in journey_dict.items():
                        journey_dict.update({tup: 0})
                    if tup1 not in journey_dict.items():
                        journey_dict.update({tup1: 0})
            return journey_dict

        def insert_distance(self, journey_dict):
            for k, v in journey_dict.items():
                calcs = self.distance_between_points(k.ev_stop, k.point)
                print(f"-----> {calcs} stop {k.ev_stop} point {k.point} " )
                journey_dict.update({k: calcs})
            return journey_dict