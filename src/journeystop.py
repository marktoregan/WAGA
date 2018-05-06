import datetime
from datetime import datetime


class JourneyStop:
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs:
        """
        self.ev_point_id = kwargs.get("ev_point_id")
        self.arrival_time = kwargs.get("arrival_time", datetime.now())
        self.departure_time = kwargs.get("departure_time")
        self.wait_time = kwargs.get("wait_time")
        self.charge_time = kwargs.get("charge_time", 25)
        self.location_in_journey_manager = kwargs.get("location_in_journey_manager")




