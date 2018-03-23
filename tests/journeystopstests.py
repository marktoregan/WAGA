import unittest

from datetime import datetime
from src import journeystop as js
from src import journeystops as jss


class JourneyStopsTests(unittest.TestCase):

    def setUp(self):
        self.charge_time = 25
        self.current_time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
        self.current_time2 = datetime(year=2018, month=2, day=27, hour=13, minute=10)
        self.current_time3 = datetime(year=2018, month=2, day=27, hour=13, minute=15)
        self.current_time4 = datetime(year=2018, month=2, day=27, hour=14, minute=16)
        self.current_time5 = datetime(year=2018, month=2, day=27, hour=14, minute=22)

        self.stop1 = js.JourneyStop(ev_point_id=1, arrival_time=self.current_time4, departure_time=0, wait_time=0, charge_time=self.charge_time)
        self.stop2 = js.JourneyStop(ev_point_id=2, arrival_time=self.current_time1, departure_time=0, wait_time=0, charge_time=self.charge_time)
        self.stop3 = js.JourneyStop(ev_point_id=1, arrival_time=self.current_time3, departure_time=0, wait_time=0, charge_time=self.charge_time)
        self.stop4 = js.JourneyStop(ev_point_id=2, arrival_time=self.current_time2, departure_time=0, wait_time=0, charge_time=self.charge_time)
        self.stop5 = js.JourneyStop(ev_point_id=1, arrival_time=self.current_time5, departure_time=0, wait_time=0, charge_time=self.charge_time)

        self.journeys = list()
        self.journeys.append(self.stop1)
        self.journeys.append(self.stop2)
        self.journeys.append(self.stop3)
        self.journeys.append(self.stop4)
        self.journeys.append(self.stop5)
        self.jstops = jss.JourneyStops()

    def test_total_time(self):
        t = self.jstops.total_time_of_stops(self.journeys)
        self.assertEquals(159, t)
        #print(f'lkkll')

