import math
import random
from datetime import datetime, timedelta
from src.config import mapconfig as md
from src import journeystop as js, ev_charge_point as evp


class Journey(object):
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: start_time, starting_point, end_point, stops
        """
        self.start_time = kwargs.get("start_time", datetime.now())
        self.starting_point = kwargs.get("starting_point", [0, 0])
        self.end_point = kwargs.get("end_point", [0, 10])
        self.current_location = kwargs.get("current_point", [0, 5])
        self.total_journey_time = kwargs.get("total_journey_time", 0)
        self.stop = kwargs.get("stop", [0, 0])

    def _euclidean_distance(self, point1, point2):
        """
        :param point1:
        :param point2:
        :return:
        """
        euclidean = math.sqrt(((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2))
        return euclidean

    def distance_in_minutes(self, ev1):
        """
        :param ev1:
        :return: time = distance / speed
        """
        distance = self.distance()
        time = distance / ev1.max_speed
        time *= 60
        return time

    def distance(self):
        """
        :return:
        """
        ev_stop = evp.EvChargePoint()
        ev_stop1 = ev_stop.get_ev_charge_point('a')
        print(f"{ev_stop.location}")
        print(ev_stop1)

        start_to_evp = self._euclidean_distance(self.starting_point, ev_stop.location)
        mpd = md.MapConfig()
        total_distance_km = start_to_evp * mpd.legend_distance
        return total_distance_km

    def set_journey_stop(self, stops):
        s = random.choice(stops)
        a_stop = js.JourneyStop(s)
        self.stop.append(a_stop)
