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
        self.longitude = kwargs.get("longitude")
        self.latitude = kwargs.get("latitude")
        self.name = kwargs.get("name")

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

    def load_all_evps(self):
        db = TinyDB('../src/db/db.json')
        charge_point = Query()
        results = db.all()
        all_charge_points = []
        for r in results:
            result_evp = EvChargePoint(id=r["evp"], charge_type=r["charge_type"],
                                    location=r["location"],
                                    charge_time_required=r["charge_time_required"],
                                    longitude=r["longitude"],
                                    latitude=r["latitude"],
                                    name=r["name"])
            all_charge_points.append(result_evp)
        return all_charge_points





 #        "evp": "mnwmuug4bf46-1",
 #       "charge_type": "Type-2 AC Socket 3.7kW",
 #       "location": [0.0004851078424378046, -6.64769659607716e-05],
 #       "charge_time_required": 480,
 #       "longitude": 54.001958,
 #       "latitude": -7.400182,
 #       "name": "Radisson Blu Hotel, Farnham Estate, Cavan-Longford Road (R198), Cavan Town, County Cavan"
 #