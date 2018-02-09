import datetime
import random
from itertools import chain
from src import calculatetotalminutes as ctm
from src import genetic
from src import fitness as fit


class Waga:
    #def __init__(self):

    def get_fitness(self, genes):
        calc = ctm.CalculateTotalMinutes(genes)
        total_time = calc.total_wait_time(25)
        return fit.Fitness(total_time)

    def mutate(self, genes, fnGetFitness):
        print('entering mutate')
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

    def crossover(self, parentGenes, donorGenes, fnGetFitness):
        print('entering crossover')
        pairs = {Pair(donorGenes[0], donorGenes[-1]): 0}

        for i in range(len(donorGenes) - 1):
            pairs[Pair(donorGenes[i], donorGenes[i + 1])] = 0

        tempGenes = parentGenes[:]
        if Pair(parentGenes[0], parentGenes[-1]) in pairs:
            # find a discontinuity
            found = False
            for i in range(len(parentGenes) - 1):
                if Pair(parentGenes[i], parentGenes[i + 1]) in pairs:
                    continue
                tempGenes = parentGenes[i + 1:] + parentGenes[:i + 1]
                found = True
                break
            if not found:
                return None

        runs = [[tempGenes[0]]]
        for i in range(len(tempGenes) - 1):
            if Pair(tempGenes[i], tempGenes[i + 1]) in pairs:
                runs[-1].append(tempGenes[i + 1])
                continue
            runs.append([tempGenes[i + 1]])

        initialFitness = fnGetFitness(parentGenes)
        count = random.randint(2, 20)
        runIndexes = range(len(runs))
        while count > 0:
            count -= 1
            for i in runIndexes:
                if len(runs[i]) == 1:
                    continue
                if random.randint(0, len(runs)) == 0:
                    runs[i] = [n for n in reversed(runs[i])]
            #print('runIndexes {}'.format(runIndexes))
            indexA, indexB = random.sample(runIndexes, 2)
            runs[indexA], runs[indexB] = runs[indexB], runs[indexA]
            childGenes = list(chain.from_iterable(runs))
            if fnGetFitness(childGenes) > initialFitness:
                return childGenes
        return childGenes

    def solve(self, ev_locations, optimal_sequence,size):

        def _create():
            stops = [random.choice(ev_locations) for x in range(size)]
            return stops

        def _display(candidate):
            self.display(candidate, start_time)

        def _get_fitness(genes):
            return self.get_fitness(genes)

        def _mutate(genes):
            self.mutate(genes, _get_fitness)

        def _crossover(parent, donor):
            return self.crossover(parent, donor, _get_fitness)
            #self.mutate(genes, _get_fitness)

        start_time = datetime.datetime.now()
        optimal_fitness = _get_fitness(optimal_sequence)
        best = genetic.get_best(_get_fitness, None, optimal_fitness, None,
                                _display, _mutate, _create, maxAge=500, poolSize=25, crossover=_crossover)
        return optimal_fitness, best

class Pair:
    def __init__(self, node, adjacent):
        if node < adjacent:
            node, adjacent = adjacent, node
        self.Node = node
        self.Adjacent = adjacent

    def __eq__(self, other):
        return self.Node == other.Node and self.Adjacent == other.Adjacent

    def __hash__(self):
        return hash(self.Node) * 397 ^ hash(self.Adjacent)