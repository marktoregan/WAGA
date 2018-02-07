import unittest

from src import calculatetotalminutes as ctm


class CalculateTotalMinutesTests(unittest.TestCase):

    def test_x2_each_point(self):
        est_ev_points = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]
        calc = ctm.CalculateTotalMinutes(est_ev_points)
        result = calc.total_wait_time(25)
        self.assertEquals(375.0, result)

    def test_same_for_all_points(self):
        est_ev_points = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
        calc = ctm.CalculateTotalMinutes(est_ev_points)
        result = calc.total_wait_time(25)
        self.assertEquals(1375.0, result)
