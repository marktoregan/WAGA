class ElectricVehicle(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get("ev_id", 0)
        self.range = kwargs.get("range", 80)
        self.max_speed = kwargs.get("max_speed", 80)
