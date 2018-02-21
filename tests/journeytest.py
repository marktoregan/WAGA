import unittest
from src import journey as jny
from src import electricvehicle as ev


class JourneyTest(unittest.TestCase):

    def test_distance(self):
        journey = jny.Journey(starting_point=[0, 0], end_point=[17, 0])
        distance = journey.journey_distance()
        self.assertEquals(340, distance)

    def test_(self):
        journey = jny.Journey(starting_point=[0, 0], end_point=[17, 0])
        evcar = ev.ElectricVehicle(ev_id=0, range=85, max_speed=120)
        time = journey.distance_in_minutes(evcar)
        self.assertEquals(170, time)
