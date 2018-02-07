# File: genetic.py
#
# Author: Mark O'Regan <mark.t.oregan@mycit.ie>

import random
import statistics
import sys
import time
from bisect import bisect_left
from enum import Enum
from math import exp


def _generate_parent(length, gene_set, get_fitness):
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness, Strategies.Create)


def _mutate(parent, gene_set, get_fitness):
    child_genes = parent.Genes[:]
    index = random.randrange(0, len(parent.Genes))
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = alternate if new_gene == child_genes[index] else new_gene
    fitness = get_fitness(child_genes)
    return Chromosome(child_genes, fitness, Strategies.Mutate)


def _mutate_custom(parent, custom_mutate, get_fitness):
    child_genes = parent.Genes[:]
    custom_mutate(child_genes)
    fitness = get_fitness(child_genes)
    return Chromosome(child_genes, fitness, Strategies.Mutate)


def _crossover(parent_genes, index, parents, get_fitness, crossover, mutate,
               generate_parent):
    donor_index = random.randrange(0, len(parents))
    if donor_index == index:
        donor_index = (donor_index + 1) % len(parents)
    childGenes = crossover(parent_genes, parents[donor_index].Genes)
    if childGenes is None:
        # parent and donor are indistinguishable
        parents[donor_index] = generate_parent()
        return mutate(parents[index])
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness, Strategies.Crossover)


def get_best(get_fitness, target_length, optimal_fitness, gene_set, display,
             custom_mutate=None, custom_create=None, maxAge=None,
             poolSize=1, crossover=None):
    if custom_mutate is None:
        def fnMutate(parent):
            return _mutate(parent, gene_set, get_fitness)
    else:
        def fnMutate(parent):
            return _mutate_custom(parent, custom_mutate, get_fitness)

    if custom_create is None:
        def fnGenerateParent():
            return _generate_parent(target_length, gene_set, get_fitness)
    else:
        def fnGenerateParent():
            genes = custom_create()
            return Chromosome(genes, get_fitness(genes), Strategies.Create)

    strategy_lookup = {
        Strategies.Create: lambda p, i, o: fnGenerateParent(),
        Strategies.Mutate: lambda p, i, o: fnMutate(p),
        Strategies.Crossover: lambda p, i, o:
        _crossover(p.Genes, i, o, get_fitness, crossover, fnMutate,
                   fnGenerateParent)
    }

    used_strategies = [strategy_lookup[Strategies.Mutate]]
    if crossover is not None:
        used_strategies.append(strategy_lookup[Strategies.Crossover])

        def fnNewChild(parent, index, parents):
            return random.choice(used_strategies)(parent, index, parents)
    else:
        def fnNewChild(parent, index, parents):
            return fnMutate(parent)

    for improvement in _get_improvement(fnNewChild, fnGenerateParent,
                                        maxAge, poolSize):
        display(improvement)
        f = strategy_lookup[improvement.Strategy]
        used_strategies.append(f)
        if not optimal_fitness > improvement.Fitness:
            return improvement


def _get_improvement(new_child, generate_parent, max_age, pool_size):
    best_parent = generate_parent()
    yield best_parent
    parents = [best_parent]
    historical_fitnesses = [best_parent.Fitness]
    for _ in range(pool_size - 1):
        parent = generate_parent()
        if parent.Fitness > best_parent.Fitness:
            yield parent
            best_parent = parent
            historical_fitnesses.append(parent.Fitness)
        parents.append(parent)
    last_parent_index = pool_size - 1
    pindex = 1
    while True:
        pindex = pindex - 1 if pindex > 0 else last_parent_index
        parent = parents[pindex]
        child = new_child(parent, pindex, parents)
        if parent.Fitness > child.Fitness:
            if max_age is None:
                continue
            parent.Age += 1
            if max_age > parent.Age:
                continue
            index = bisect_left(historical_fitnesses, child.Fitness, 0,
                                len(historical_fitnesses))
            difference = len(historical_fitnesses) - index
            proportion_similar = difference / len(historical_fitnesses)
            if random.random() < exp(-proportion_similar):
                parents[pindex] = child
                continue
            parents[pindex] = best_parent
            parent.Age = 0
            continue
        if not child.Fitness > parent.Fitness:
            # same fitness
            child.Age = parent.Age + 1
            parents[pindex] = child
            continue
        parents[pindex] = child
        parent.Age = 0
        if child.Fitness > best_parent.Fitness:
            yield child
            best_parent = child
            historical_fitnesses.append(child.Fitness)


class Chromosome:
    def __init__(self, genes, fitness, strategy):
        self.Genes = genes
        self.Fitness = fitness
        self.Strategy = strategy
        self.Age = 0


class Strategies(Enum):
    Create = 0,
    Mutate = 1,
    Crossover = 2


class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(
                    1 + i, mean,
                    statistics.stdev(timings, mean) if i > 1 else 0))
