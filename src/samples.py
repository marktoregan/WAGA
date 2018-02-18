import random
from src import individual as ind
from src import population as pop
import itertools


i = ind.Individual(chromosome=[9, 0])

print("{}".format(i.chromosome))

l = list(range(10))
print(l)

l = [None] * 10
print(l)



sc = pop.Population(population_size = 2, chromosome_length=9)

print("{}".format(sc.population))
aa = [i for i in sc.population]
for a in aa:
    print("aa  {}".format(a.fitness))

def compare(a, b):
    if a < b:
        return -4
    if a > b:
        return 0



myList = [1, 2, 3, 4, 5, 3, 4, 6, 8, -2]
for a, b in itertools.combinations(myList, 2):
    r = compare(a, b)
    print(r)

results = [x for x in itertools.combinations(myList, 2)]

print("res {}".format(results))