"""
Charge point class
"""


class EvChargePoint(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", 0)
        self.charge_type = kwargs.get("id", 0)
        self.location = kwargs.get("location", [0, 0])
        self.occupied = kwargs.get("occupied", [0, 0])
        self.time_occupied = kwargs.get("time_occupied")
        self.charge_time_required = kwargs.get("time_occupied", 25)
