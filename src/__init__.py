from src import runga as rga
from datetime import datetime
from functools import reduce
from collections import namedtuple

if __name__ == '__main__':
    print(datetime.now())
    fitness_mean =[]
    bench_mean = []
    num_journeys =5
    totals=[]
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    for j in range(0,10):
        fitness = []
        bench = []
        for i in range(0,10):
            charge_types = ['Fast AC Type-2 44kW', 'Fast AC Type-2 50kW']
            #'CHAdeMO DC 44kW',
             #           'CHAdeMO DC 45kW', 'CHAdeMO DC 50kW', 'CHAdeMO DC 22kW', 'Combo DC 44kW', 'Combo DC 45kW',
              #          'Combo DC 50kW']

            run = rga.RunGA(generations=10, population_size=150, num_of_journeys=num_journeys, initialise=True)
            fit, ben = run.process(charge_types)

            fitness.append(fit)
            bench.append(ben)

        fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
        bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
        res = [num_journeys, fit_mean, bench_mean]
        totals.append(res)
        print(f'jour: {num_journeys} fit: {fit_mean} bench: {bench_mean}')
        num_journeys +=20

    for t in totals:
        print(t)







