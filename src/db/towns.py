import random
from src.calc import normalize as nl
from collections import namedtuple

class Towns(object):

    start_towns = {'dublin': nl.Normalize(latitude=53.350140, longitude=-6.266155)}
    end_towns = {'cork': nl.Normalize(latitude=51.903614, longitude=-8.468399),
                  'limerick': nl.Normalize(latitude=52.668018, longitude=-8.630498),
                  'galway': nl.Normalize(latitude=53.270962, longitude=-9.062691),
                  'waterford': nl.Normalize(latitude=52.2500, longitude=-7.5000),
                  'wexford': nl.Normalize(latitude=52.336918, longitude=-6.463338)}

    @staticmethod
    def get_start_town():
        City = namedtuple('City', 'name location')
        t = random.choice(['dublin'])
        cord = Towns.start_towns[t]
        return City(name=t, location=cord)

    @staticmethod
    def get_end_town():
        City = namedtuple('City', 'name location')
        ed_t = random.choice(['limerick', 'galway', 'waterford', 'wexford', 'wexford'])
        cord = Towns.end_towns[ed_t]
        return City(name=ed_t, location=cord)

class Town(object):
    def __init__(self,**kwargs):
        self.name = kwargs.get("name")
        self.longitude = kwargs.get("longitude")
        self.latitude = kwargs.get("latitude")

if __name__ == "__main__":

    for t in range(0,20):
        t1 = Towns.get_start_town()
        t2 = Towns.get_end_town()
        print(t1.name, t2.name)