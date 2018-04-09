# File: gentests.py
# Author: Mark O'Regan <mark.t.oregan@mycit.ie>

import unittest

from src import waga as ga

"""
The Watts Available Test class 
"""
class WagaTests(unittest.TestCase):
    gene_set = ['a', 'b', 'c', 'd', 'e']

    def test_10_journeys_5_points(self):
        pass