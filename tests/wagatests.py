# File: gentests.py
# Author: Mark O'Regan <mark.t.oregan@mycit.ie>

import unittest

from src import waga as ga


class WagaTests(unittest.TestCase):
    gene_set = ['a', 'b', 'c', 'd', 'e']

    def test_10_journeys_5_points(self):
        x = ga.Waga()

        optimal_fitness, best = x.solve(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c','d','e'], 10)
        self.assertTrue(not optimal_fitness > best.Fitness)


if __name__ == '__main__':
    unittest.main()

