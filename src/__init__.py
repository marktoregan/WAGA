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
    num_population =10
    totals=[]
    result_lst = []
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    #for j in range(0,10):
    fitness = []
    bench = []
    converge = []
    for j in range(0,7):
        for i in range(0,10):
            print(f'on {i} of 10')
            #run = rga.RunG1(generations=100, population_size=50, num_of_journeys=100, initialise=True)
            run = rga.RunGA(generations=200, population_size=100, num_of_journeys=100, initialise=True)
            res_dict = run.process(stopIDs)
            fit = res_dict['fit']
            ben = res_dict['ben']
            converged = res_dict['converged']
            converge.append(converged)
            #fit, ben = run.process(stopIDs)
            fitness.append(fit)
            bench.append(ben)
            res = RunResult(id=num_population, fitness=fit, bench=ben, converged=converged)
            result_lst.append(res)

        print(f'whats {result_lst}')
        #fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
        con_mean = reduce(lambda x, y: x + y, converge) / len(converge)
        #bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
        res2 = [num_population, con_mean]
        print(res2)
        num_population += 30
        totals.append([num_population, con_mean])

    #print(f'jour: {i} fit: {fit_mean} bench: {bench_mean}')
    print(totals)
    print(datetime.now())









