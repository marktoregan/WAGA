from tinydb import TinyDB, Query
"""
Charge point class
"""


class EvChargePoint(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", 0)
        self.charge_type = 0    #kwargs.get("charge_type", 0)
        self.location = [0, 0]   #kwargs.get("location", [0, 0])
        self.charge_time_required = 0 #kwargs.get("charge_time_required", 25)

    def get_ev_charge_point(self, id):
        db = TinyDB('../src/db/db.json')
        charge_point = Query()
        results = db.search(charge_point.evp == id)
        evp = EvChargePoint(id=results[0]["evp"],
                            charge_type=results[0]["charge_type"],
                            location=results[0]["location"],
                            charge_time_required=results[0]["charge_time_required"])
        return evp


    def all_ev_charge_points(self):
        db = TinyDB('../src/db/db.json')
        charge_point = Query()
        results = db.all()
        charge_points = []
        for r in results:
            charge_points.append(r["location"])
        return charge_points

        #evp = EvChargePoint(id=results[0]["evp"],
          #                  charge_type=results[0]["charge_type"],
          #                  location=results[0]["location"],
           #                 charge_time_required=results[0]["charge_time_required"])
        #return evp