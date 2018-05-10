from src import runga as rga
from datetime import datetime
from functools import reduce
from collections import namedtuple

if __name__ == '__main__':
    print('V1')
    print(datetime.now())
    stopIDs =['mnvgub2px9b3-703','mnvf57xc8p2b-778','mntwqrh1bf1v-789','mntwqrh1bf1v-789','mntesudtd1rg-823',
              'mntesudtd1rg-824','mntesudtd1rg-825','mnmrnj9x9d0g-708']


    fitness_mean =[]
    bench_mean = []
    num_journeys =5
    totals=[]
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    #for j in range(0,10):
    fitness = []
    bench = []
    for i in range(0,10):
        print(f'on {i} of 10')
        run = rga.RunGA(generations=100, population_size=50, num_of_journeys=100, initialise=True)
        fit, ben = run.process(stopIDs)
        fitness.append(fit)
        bench.append(ben)

    fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
    bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
    res = [num_journeys, fit_mean, bench_mean]
    totals.append(res)
    print(f'jour: x fit: {fit_mean} bench: {bench_mean}')
        #num_journeys +=20

    for t in totals:
        print(t)







