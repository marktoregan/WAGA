import math
import random
from datetime import datetime, timedelta
from src.config import mapconfig as md
from src import journeystop as js, evchargepoint as evp


CLASS Journey(object):
    FUNCTION __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: start_time, starting_point, end_point, stops
        """
         start_time <- kwargs.get("start_time", datetime.now())
         starting_point <- kwargs.get("starting_point")
         end_point <- kwargs.get("end_point")
         current_location <- kwargs.get("current_point")
         total_journey_time <- kwargs.get("total_journey_time", 0)
         stop <- kwargs.get("stop")
    ENDFUNCTION

ENDCLASS


    FUNCTION _euclidean_distance(self, point1, point2):
        """
        :param point1:
        :param point2:
        :return:
        """
        euclidean <- math.sqrt(((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2))
        RETURN euclidean
    ENDFUNCTION


    FUNCTION distance_in_minutes(self, speed_limit):
        """
        :param ev1:
        :return: time <- distance / speed
        """
        distance_km <-  distance()
        time <- distance_km / speed_limit
        time *= 60
        RETURN time
    ENDFUNCTION


    FUNCTION distance(self):
        """
        :return:
        """
        ev_stop <- evp.EvChargePoint()
        ev_stop <- ev_stop.get_ev_charge_point( stop[0])
        distance_to_evp_km <-  _distance_in_km( starting_point, ev_stop.location)
        distance_from_evp_km <-  _distance_in_km(ev_stop.location,  end_point)
        total_distance_km <- distance_to_evp_km + distance_from_evp_km
        RETURN total_distance_km
    ENDFUNCTION


    FUNCTION _distance_in_km(self, p1, p2):
        mpd <- md.MapConfig()
        dist <-  _euclidean_distance(p1,p2)
        distance_in_km <- dist * mpd.legend_distance
        RETURN distance_in_km
    ENDFUNCTION


    FUNCTION set_journey_stop(self, stops):
        s <- random.choice(stops)
        a_stop <- js.JourneyStop(s)
         stop.append(a_stop)
