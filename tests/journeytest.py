import unittest
from src import journey as jny


class JourneyTest(unittest.TestCase):

    def test_distance(self):
        journey = jny.Journey(starting_point=[0, 0], end_point=[17, 0])
        distance = journey.journey_distance()
        self.assertEquals(340, distance)
