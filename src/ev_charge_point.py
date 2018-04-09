from tinydb import TinyDB, Query
"""
Charge point class
"""


class EvChargePoint(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", 0)
        self.charge_type = kwargs.get("charge_type", 0)
        self.location = kwargs.get("location", [0, 0])
        self.charge_time_required = kwargs.get("charge_time_required", 25)
        #self.occupied = kwargs.get("occupied", False)
        #self.time_occupied = kwargs.get("time_occupied")

    def get_ev_charge_point(self, id):
        db = TinyDB('../src/db/db.json')
        charge_point = Query()
        results = db.search(charge_point.evp == id)

        evp = EvChargePoint(id=results[0]["evp"],
                            charge_type=results[0]["charge_type"],
                            location=results[0]["location"],
                            charge_time_required=results[0]["charge_time_required"])
        return evp