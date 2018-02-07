# File: gentests.py
# Author: Mark O'Regan <mark.t.oregan@mycit.ie>


import datetime
import unittest
import random
import genetic
import calculatetotalminutes as ctm
import fitness as fit


def get_fitness(genes):
    calc = ctm.CalculateTotalMinutes(genes)
    total_time = calc.total_wait_time(25)
    return fit.Fitness(total_time)


def mutate(genes, fnGetFitness):
    count = random.randint(2, len(genes))
    initial_fitness = fnGetFitness(genes)
    while count > 0:
        count -= 1
        indexA, indexB = random.sample(range(len(genes)), 2)
        genes[indexA], genes[indexB] = genes[indexB], genes[indexA]
        fitness = fnGetFitness(genes)
        if fitness > initial_fitness:
            return


def display(candidate, start_time):
    timeDiff = datetime.datetime.now() - start_time
    print("{}\t{}\t{}\t{}".format(
        ' '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        candidate.Strategy.name,
        timeDiff))


class WagaTests(unittest.TestCase):
    gene_set = ['a', 'b', 'c', 'd', 'e']

    def test_10_journeys_5_points(self):
        self.solve(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e', 'a'])

    def solve(self, ev_locations, optimal_sequence):

        def _create():
            stops = [random.choice(ev_locations) for x in range(6)]
            return stops

        def _display(candidate):
            display(candidate, start_time)

        def _get_fitness(genes):
            return get_fitness(genes)

        def fn_mutate(genes):
            mutate(genes, _get_fitness)

        start_time = datetime.datetime.now()
        optimal_fitness = _get_fitness(optimal_sequence)
        best = genetic.get_best(_get_fitness, None, optimal_fitness, None,
                                _display, fn_mutate, _create, maxAge=500, poolSize=25)

        self.assertTrue(optimal_fitness == best.Fitness)


if __name__ == '__main__':
    unittest.main()

