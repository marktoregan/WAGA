import random
from src import individual as ind
from src import population as pop
import itertools


i = ind.Individual(chromosome=[9, 0])

#print("{}".format(i.chromosome))

l = list(range(10))
#print(l)

l = [None] * 10
#print(l)



sc = pop.Population(population_size = 2, chromosome_length=9)

print("{}".format(sc.population))
aa = [i for i in sc.population]
for a in aa:
    print("aa  {}".format(a.fitness))

fit = sc.get_fittest(0)
print("fittest  {}".format(fit.fitness))

#lst1 = [1,5,6,7,3,98,1,4,0,9]
#di = dict(enumerate(lst1))
#print(di)

#res = min(di, key=di.get)
#print("lowest {}".format(res))
#di = {key: value for (key, value) in lst}

#di = {lambda x: x in lst}

#for k, v in di.items():
#    print("k {} v {}".format(k, v))

