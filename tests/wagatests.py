# File: gentests.py
# Author: Mark O'Regan <mark.t.oregan@mycit.ie>

import unittest

from src import waga as xxx


class WagaTests(unittest.TestCase):
    gene_set = ['a', 'b', 'c', 'd', 'e']

    def test_10_journeys_5_points(self):
        x = xxx.Waga()

        optimal_fitness, best = x.solve(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e', 'a'])
        self.assertTrue(optimal_fitness == best.Fitness)


if __name__ == '__main__':
    unittest.main()

