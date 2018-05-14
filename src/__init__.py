from src import runga as rga
from datetime import datetime
from functools import reduce
from collections import namedtuple

if __name__ == '__main__':
    print('V1')
    print(datetime.now())
    stopIDs =['mnvgub2px9b3-703','mnvf57xc8p2b-778','mntwqrh1bf1v-789','mntwqrh1bf1v-789','mntesudtd1rg-823',
              'mntesudtd1rg-824','mntesudtd1rg-825','mnmrnj9x9d0g-708']

    RunResult = namedtuple('RunResult', 'id fitness bench')

    fitness_mean =[]
    bench_mean = []
    increase =1
    totals=[]
    result_lst = []
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    #for j in range(0,10):
    fitness = []
    bench = []
    runs = 7
    number_of_times = 10
    for j in range(1,runs+1):
        for i in range(0,number_of_times):
            print(f'on {i} of {number_of_times} and {j} of {runs}')
            #run = rga.RunGA(generations=100, population_size=50, num_of_journeys=100, initialise=True)
            run = rga.RunGA(generations=200, population_size=30, num_of_journeys=25, initialise=True)
            stps = stopIDs[:j]
            #print(stps)
            fit, ben = run.process(stps)
            fitness.append(fit)
            bench.append(ben)
            res = RunResult(id=increase, fitness=fit, bench=ben)
            result_lst.append(res)
        print(f'whats {result_lst}')
        fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
        bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
        res = [increase, fit_mean, bench_mean]
        totals.append(res)
        increase += 1
    print(f'jour: {i} fit: {fit_mean} bench: {bench_mean}')
    print(totals)









