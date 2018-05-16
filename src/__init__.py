from src import runga as rga
from datetime import datetime
from functools import reduce
from collections import namedtuple

if __name__ == '__main__':
    print('V1')
    print(datetime.now())
    stopIDs =['mnvgub2px9b3-703','mnvf57xc8p2b-778','mntwqrh1bf1v-789','mntwqrh1bf1v-789','mntesudtd1rg-823',
              'mntesudtd1rg-824','mntesudtd1rg-825','mnmrnj9x9d0g-708']

    RunResult = namedtuple('RunResult', 'id fitness bench converged')

    fitness_mean =[]
    bench_mean = []
    increase =10
    totals=[]
    result_lst = []
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    #for j in range(0,10):
    fitness = []
    bench = []
    converge = []
    for j in range(0,5):
        for i in range(0,10):
            print(f'on {i} of 10')
            #run = rga.RunG1(generations=100, population_size=50, num_of_journeys=100, initialise=True)
            run = rga.RunGA(generations=200, population_size=increase, num_of_journeys=80, initialise=True)
            res_dict = run.process(stopIDs)
            fit = res_dict['fit']
            ben = res_dict['ben']
            converged = res_dict['converged']
            converge.append(converged)
            #fit, ben = run.process(stopIDs)
            fitness.append(fit)
            bench.append(ben)
            res = RunResult(id=increase, fitness=fit, bench=ben, converged=converged)
            result_lst.append(res)

        print(f'whats {result_lst}')
        fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
        con_mean = reduce(lambda x, y: x + y, converge) / len(converge)
        bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
        res2 = [increase, con_mean]
        print(res2)
        increase += 40
        #totals.append([increase, con_mean])
        totals.append([increase, fit_mean, bench_mean, con_mean])

    #print(f'jour: {i} fit: {fit_mean} bench: {bench_mean}')
    print(totals)
    print(datetime.now())