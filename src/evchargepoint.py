from tinydb import TinyDB, Query, where
from src.config import mapconfig as mc
"""
Charge point class
"""


class EvChargePoint(object):
    dbconn = mc.MapConfig.db_location()
    stations = {"cork": ["Topaz Service Station, M8 @Junction 3 (R433), Ballacolla, County Laois",
                         "Texaco Service Station, Main Street, Urlingford, County Kilkenny",
                         "Topaz Service Station, M8 Junction 8 (R692), Wallers Lot, Cashel, County Tipperary",
                         "Texaco Woodview Service Station, Mitchelstown Road, Cahir, County Tipperary",
                         "Supervalu, Courthouse Road, Fermoy, County Cork",
                         "Deasy's Topaz Service Station, Commons Road, Cork City, County Cork",
                         "Topaz Frankfield Service Station, Frankfield Road, Douglas, County Cork",
                         "Midway Complex, M7 Junction 17 (N77/R423), Portlaoise, County Laois",
                         "Esso/Centra, Rochestown Road, Rochestown, Cork City, County Cork",
                         "Temperance Street, Abbeyleix, County Laois",
                         "Irish Rail, Butler Avenue, Thurles, County Tipperary",
                         "Gordon Place Car Park, Wolfe Tone Street, Clonmel, County Tipperary",
                         "Off Abbeyleix Road, Portlaoise, County Laois",
                         "Irish Rail, Kildare Train Station, Station Road, Kildare Town, County Kildare"],
                "galway": ["Applegreen Enfield Services, M4 (Westbound, 2km after Jnct 9), County Kildare",
                           "Topaz Service Station, M6 Junction 5 (R389/N52), Tullamore Road, Kilbeggan, County Westmeath",
                           "Topaz Service Station, Castlemaine Street (Dublin Road), Athlone, County Westmeath",
                           "Topaz Service Station (Dolan's), Athlone Road (R446), Ballinasloe, County Galway",
                           "Glynn's Centra/Topaz Service Station, Carnmore Cross (@Galway Airport Entrance on R339 off N18), Oranmore, County Galway",
                           "Topaz Service Station, Castlemaine Street (Dublin Road), Athlone, County Westmeath",
                           "Irish Rail Train Station Car Park, Off Main Street, Enfield, County Meath",
                           "O'Connell Square, Edenderry, County Offaly",
                           "The Square, Kilbeggan, County Westmeath",
                           "Irish Rail Clara Train Station, Railway View, Clara, County Offaly",
                           "Main Street, Moate, County Westmeath",
                           "Topaz Service Station, Castlemaine Street (Dublin Road), Athlone, County Westmeath",
                           "Saint Michael's Square, Ballinasloe, County Galway"],
                "waterford": ["Tesco, Monread Road, Naas, County Kildare",
                              "Four Lakes Retail Park, Dublin Road, Carlow Town, County Carlow",
                              "Barlo Nissan, Dublin Road, Kilkenny City, County Kilkenny",
                              "EMO Service Station, M9 Junction 10 (R699), Main Street, Knocktopher, County Kilkenny",
                              "Top/Londis Service Station, Holy Cross/Butlerstown (R680 - Old Cork Road), Waterford City, County Waterford",
                              "The Square Shopping Centre, Belgard Road, Tallaght, Dublin 24, County Dublin",
                              "Citywest Shopping Centre Car Park, Citywest Drive, Saggart, County Dublin",
                              "Main Street, Rathcoole, Dublin 24, County Dublin",
                              "Irish Rail, Sallins and Naas Train Station (South Car Park), The Waterways, Off R407, Sallins, County Kildare",
                              "Fairgreen Street, Naas, County Kildare",
                              "Hedermans Car Park, Friary Road, Naas, County Kildare",
                              "Hanover Bus Car Park, Barrack Street, Carlow Town, County Carlow",
                              "The Parade, Bagenalstown, County Carlow",
                              "The Quay, Thomastown, County Kilkenny",
                              "Irish Rail Plunkett Station, Dock Road, Abbeylands, County Waterford",
                              "Ballybricken Green, Ballbricken, Waterford City, County Waterford"],
                "wexford": [
                    "Stillorgan Luas Park & Ride, Blackthorn Drive, Stillorgan Office Park, Sandyford, Dublin 18, County Dublin",
                    "Tesco, Vevay Road, Bray, County Wicklow",
                    "Applegreen Services (Northbound), M11 Junction 14 (R772), Cullenmore, County Wicklow",
                    "Tesco, Glebe Road, Wicklow Town, County Wicklow",
                    "Maxol Service Station, Arklow Road, Gorey, County Wexford",
                    "Topaz Service Station, Rosslare Road, Drinagh, County Wexford",
                    "Applegreen Services (Northbound), M11 Junction 14 (R772), Cullenmore, County Wicklow",
                    "Shankhill Dart Station, Shanganagh Wood, Dun Laoghaire, Dublin 18, County Dublin",
                    "GAA Car Park, Main Street, Ashford, County Wicklow",
                    "Riverwalk, Via Upper Main Street, Arklow, County Wicklow",
                    "Laffins Lane Car Park, Via Lower Main Street or Castle Park, Arklow, County Wicklow",
                    "Irish Rail, Mary Street, Arklow, County Wicklow",
                    "Irish Rail, Railway Road, Gorey, County Wexford",
                    "Civic Centre Car Park, The Avenue, Gorey, County Wexford",
                    "Public Car Park, Island Road, Enniscorthy, County Wexford",
                    "Public  Car Park, Duffry Gate, Enniscorthy, County Wexford",
                    "Garda Station Car Park, Off Lymington Road, Enniscorthy, County Wexford",
                    "High Street, Wexford Town, County Wexford"],
                "limerick": ["Main Street, Rathcoole, Dublin 24, County Dublin",
                             "Citywest Shopping Centre Car Park, Citywest Drive, Saggart, County Dublin",
                             "Fairgreen Street, Naas, County Kildare",
                             "Hedermans Car Park, Friary Road, Naas, County Kildare",
                             "Irish Rail, Newbridge Train Station, Station Road, Newbridge, County Kildare",
                             "Irish Rail, Kildare Train Station, Station Road, Kildare Town, County Kildare",
                             "Mayfield Services, M7 Junction 14 (R445), Monasterevin, County Kildare",
                             "Irish Rail Station Cark Park, Canal Harbour, Monasterevin, County Kildare",
                             "Off Abbeyleix Road, Portlaoise, County Laois",
                             "Irish Rail, Train Station Car Park, Station Road, Portlaoise, County Laois",
                             "Supervalu Car Park, Off Green Street, Roscrea, County Tipperary",
                             "Topaz Service Station, Barack Obama Plaza, R445 / M7 Junction 23, Moneygall, County Tipperary",
                             "Esso Daybreak Service Station, Limerick Road, Nenagh, County Tipperary",
                             "Pery Square, Limerick City, County Limerick",
                             "Tesco, Monread Road, Naas, County Kildare",
                             "Mayfield Services, M7 Junction 14 (R445), Monasterevin, County Kildare",
                             "Midway Complex, M7 Junction 17 (N77/R423), Portlaoise, County Laois",
                             "Topaz Service Station, M8 @Junction 3 (R433), Ballacolla, County Laois",
                             "Topaz Carrig Service Station, Carrig Road, Roscrea, County Tipperary",
                             "Abbey Court Hotel, Dublin Road, Nenagh, County Tipperary"]}

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

    def all_evps_for_destinations(self, city_names, ctypes):
        names_s = set()
        for city in city_names:
            evp_names = EvChargePoint.stations[city]
            for name in evp_names:
                names_s.add(name)
        evps, preloaded = self.get_ev_charge_point_by_name(names_s,ctypes)
        return evps, preloaded

    def get_ev_charge_point_by_name(self, all_names, charge_types):
        db = TinyDB(EvChargePoint.dbconn)
        evps = []
        preloaded = {}
        for n in all_names:
            results = db.search(where('name') == n)
            for r in results:
                ctype = r["charge_type"]
                if ctype in charge_types:
                    evp = EvChargePoint(id=r["evp"],
                                               charge_type=r["charge_type"],
                                               location=r["location"],
                                               charge_time_required=r["charge_time_required"],
                                               longitude=r["longitude"],
                                               latitude=r["latitude"],
                                               name=r["name"])
                    evps.append(evp)
                    preloaded[r["evp"]] = evp
        return evps, preloaded