import unittest
from src import journey as jny
from src import electricvehicle as ev
from src import ev_charge_point as ecp
from datetime import datetime, timedelta


class JourneyTest(unittest.TestCase):
    def setUp(self):
        self.current_time = datetime.now()
        self.journey1 = jny.Journey(start_time=self.current_time, starting_point=[0, 0], end_point=[0, 10],
                                    current_point=[5, 0], stops={"stops": {"ev_point_id": 1,
                                                                           "arrival_time": self.current_time,
                                                                           "departure_time": 0, "wait_time": 0}})
        self.ev_car = ev.ElectricVehicle(ev_id=0, range=80, max_speed=120)
        self.ev_cp = ecp.EvChargePoint(id=1, location=[9, 0], occupied=False, time_occupied=False,
                                       charge_time_required=20, charge_type='xyz')

    def test_distance(self):
        distance = self.journey1.journey_distance()
        self.assertEquals(200, distance)

    def test_distance_in_minutes(self):
        time = self.journey1.distance_in_minutes(self.ev_car)
        self.assertEquals(100, time)

