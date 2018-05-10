from tinydb import TinyDB, Query, where
from src.config import mapconfig as mc
"""
Charge point class
"""


class EvChargePoint(object):
    dbconn = mc.MapConfig.db_location()

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", 0)
        self.charge_type = kwargs.get("charge_type", 0)
        self.location = kwargs.get("location", [0, 0])
        self.charge_time_required = kwargs.get("charge_time_required", 25)
        self.longitude = kwargs.get("longitude")
        self.latitude = kwargs.get("latitude")
        self.name = kwargs.get("name")

    def get_ev_charge_point(self, id):
        db = TinyDB(EvChargePoint.dbconn)
        charge_point = Query()
        results = db.search(charge_point.evp == id)
        evp = EvChargePoint(id=results[0]["evp"],
                            charge_type=results[0]["charge_type"],
                            location=results[0]["location"],
                            charge_time_required=results[0]["charge_time_required"],
                            longitude = results[0]["longitude"],
                            latitude = results[0]["latitude"],
                            name = results[0]["name"])
        return evp


    def all_ev_charge_points(self):
        db = TinyDB(EvChargePoint.dbconn)
        charge_point = Query()
        results = db.all()
        charge_points = []
        for r in results:
            charge_points.append(r["location"])
        return charge_points

    def load_all_evps(self):
        #db = TinyDB('../src/db/db.json')
        db = TinyDB(EvChargePoint.dbconn)
        charge_point = Query()
        results = db.all()
        all_charge_points = []
        for r in results:
            result_evp = EvChargePoint(id=r["evp"],
                                       charge_type=r["charge_type"],
                                       location=r["location"],
                                       charge_time_required=r["charge_time_required"],
                                       longitude=r["longitude"],
                                       latitude=r["latitude"],
                                       name=r["name"])
            all_charge_points.append(result_evp)
        return all_charge_points

    def get_ev_charge_point_by_type(self, type):
        db = TinyDB(EvChargePoint.dbconn)
        evps = []
        preloaded = {}
        for t in type:
            results = db.search(where('charge_type') == t)
            for r in results:
                evp = EvChargePoint(id=r["evp"],
                                    charge_type=r["charge_type"],
                                    location=r["location"],
                                    charge_time_required=r["charge_time_required"])
                evps.append(evp)
                preloaded[r["evp"]] = evp
        return evps, preloaded

    def get_ev_charge_point_by_location(self, locations):
        db = TinyDB(EvChargePoint.dbconn)
        evps = []
        preloaded = {}
        for l in locations:
            results = db.search(where('location') == l)
            for r in results:
                evp = EvChargePoint(id=r["evp"],
                                    charge_type=r["charge_type"],
                                    location=r["location"],
                                    charge_time_required=r["charge_time_required"])
                evps.append(evp)
                preloaded[r["evp"]] = evp
        return evps, preloaded

    def get_ev_charge_point_by_ids(self, ids):
        evps = []
        preloaded = {}
        for id in ids:
            evp = self.get_ev_charge_point(id)
            evps.append(evp)
            preloaded[evp.id] = evp
        return evps, preloaded

