from src import evchargepoint as evp


class EvChargePoints:

    default_charge_types = {'Type-2 AC Socket 3.7kW': 480,
                   'Type-2 AC Socket 7kW': 270,
                   'Type-2 AC Socket 22kW': 90,
                   'CHAdeMO DC 22kW': 60,
                   'Fast AC Type-2 43kW': 45,
                   'CHAdeMO DC 45kW': 45,
                   'Fast AC Type-2 44kW': 40,
                   'CHAdeMO DC 44kW': 30,
                   'Fast AC Type-2 50kW': 30,
                   'Combo DC 44kW': 30,
                   'Combo DC 45kW': 30,
                   'Combo DC 50kW': 25,
                   'CHAdeMO DC 50kW': 25}

    def __init__(self):
        pass

    def all_evps(self):
        cpoints = evp.EvChargePoint()
        all_stops = cpoints.load_all_evps()
        stop_ids = [stop.id for stop in all_stops]
        return stop_ids

    @staticmethod
    def charge_time(charge_type):
        time = EvChargePoints.default_charge_types[charge_type]
        return time

    @staticmethod
    def get_by_type(type):
        cpoints = evp.EvChargePoint()
        all_stops, preloaded = cpoints.get_ev_charge_point_by_type(type)
        stop_ids = [stop.id for stop in all_stops]
        return stop_ids, preloaded

    @staticmethod
    def get_ev_charge_point_by_ids(ids):
        cpoints = evp.EvChargePoint()
        all_stops, preloaded = cpoints.get_ev_charge_point_by_ids(ids)
        stop_ids = [stop.id for stop in all_stops]
        return stop_ids, preloaded

    def get_stop_ids(self, journey_manager, speeds):
        ctypes = self.load_speeds(speeds)
        city_names = self.load_names(journey_manager)
        cpoints = evp.EvChargePoint()
        evps, preloaded = cpoints.all_evps_for_destinations(city_names,ctypes)
        return evps, preloaded

    def load_speeds(self, speeds):
        ctypes = []
        if speeds == ['slow']:
            ctypes = [k for k,v  in EvChargePoints.default_charge_types.items() if v > 45]
        if speeds ==['fast']:
            ctypes = [k for k, v in EvChargePoints.default_charge_types.items() if v <= 45]
        if len(speeds) == 2:
            ctypes = [k for k, v in EvChargePoints.default_charge_types.items()]
        return ctypes

    def load_names(self, journey_manager):
        to_cities = set()
        for journey in journey_manager.stops:
            to_cities.add(journey.to_city)
            #print(journey.to_city)
        return to_cities

    @staticmethod
    def prints():
        evp1 = EvChargePoints()
        print(evp1.all_evps())

        print(EvChargePoints.default_charge_types)

        print(EvChargePoints.charge_time("Fast AC Type-2 43kW"))

        print(len(EvChargePoints.get_by_type("Type-2 AC Socket 3.7kW"))) #75
        print(len(EvChargePoints.get_by_type("Type-2 AC Socket 7kW"))) #31
        print(len(EvChargePoints.get_by_type("Type-2 AC Socket 22kW"))) # 465
        print(len(EvChargePoints.get_by_type("CHAdeMO DC 22kW"))) #1
        print(len(EvChargePoints.get_by_type("Fast AC Type-2 43kW"))) #111
        print(len(EvChargePoints.get_by_type("CHAdeMO DC 45kW"))) #33
        print(len(EvChargePoints.get_by_type("Fast AC Type-2 44kW"))) #4
        print(len(EvChargePoints.get_by_type("CHAdeMO DC 44kW"))) #25
        print(len(EvChargePoints.get_by_type("Fast AC Type-2 50kW"))) #2
        print(len(EvChargePoints.get_by_type("Combo DC 44kW"))) #12
        print(len(EvChargePoints.get_by_type("Combo DC 45kW"))) #66
        print(len(EvChargePoints.get_by_type("Combo DC 50kW"))) # 12
        print(len(EvChargePoints.get_by_type("CHAdeMO DC 50kW"))) #35

    #athlone 90
    #mntfzsgzue33-382

    #athlone 45
    #mntfzsgzue33-615


