import datetime
import random
import genetic
import calculatetotalminutes as ctm
import fitness as fit


class Waga:
    #def __init__(self):

    def get_fitness(self, genes):
        calc = ctm.CalculateTotalMinutes(genes)
        total_time = calc.total_wait_time(25)
        return fit.Fitness(total_time)

    def mutate(self, genes, fnGetFitness):
        count = random.randint(2, len(genes))
        initial_fitness = fnGetFitness(genes)
        while count > 0:
            count -= 1
            indexA, indexB = random.sample(range(len(genes)), 2)
            genes[indexA], genes[indexB] = genes[indexB], genes[indexA]
            fitness = fnGetFitness(genes)
            if fitness > initial_fitness:
                return

    def display(self, candidate, start_time):
        timeDiff = datetime.datetime.now() - start_time
        print("{}\t{}\t{}\t{}".format(
            ' '.join(map(str, candidate.Genes)),
            candidate.Fitness,
            candidate.Strategy.name,
            timeDiff))

    def solve(self, ev_locations, optimal_sequence):

        def _create():
            stops = [random.choice(ev_locations) for x in range(6)]
            return stops

        def _display(candidate):
            self.display(candidate, start_time)

        def _get_fitness(genes):
            return self.get_fitness(genes)

        def _mutate(genes):
            self.mutate(genes, _get_fitness)

        start_time = datetime.datetime.now()
        optimal_fitness = _get_fitness(optimal_sequence)
        best = genetic.get_best(_get_fitness, None, optimal_fitness, None,
                                    _display, _mutate, _create, maxAge=500, poolSize=25)
        return optimal_fitness, best
