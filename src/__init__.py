from src import runga as rga
from datetime import datetime
from functools import reduce
from collections import namedtuple
from src import evchargepoints as evps

if __name__ == '__main__':
    print('V1')
    print(datetime.now())
    stopIDs =['mnvgub2px9b3-703','mnvf57xc8p2b-778','mntwqrh1bf1v-789','mntwqrh1bf1v-789','mntesudtd1rg-823',
              'mntesudtd1rg-824','mntesudtd1rg-825','mnmrnj9x9d0g-708']

    RunResult = namedtuple('RunResult', 'id fitness bench converged')

    fitness_mean =[]
    bench_mean = []
    num_population = 10
    totals=[]
    result_lst = []
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    #for j in range(0,10):
    fitness = []
    bench = []
    converge = []
    stop_details ={}
    runs = 7
    number_of_times = 10
    for j in range(0,runs): #7
        for i in range(0,number_of_times): #10
            print(f'on {i} of {number_of_times} and {j} of {runs}')
            #run = rga.RunG1(generations=100, population_size=50, num_of_journeys=100, initialise=True)
            run = rga.RunGA(generations=200, population_size=30, num_of_journeys=10, initialise=True)
            jo = run.journey_manager
            evp = evps.EvChargePoints()
            points, preloaded = evp.get_stop_ids(journey_manager=jo,speeds=['fast'])
            x = [k for k, v in preloaded.items()]
            #print(x)
            #print("say what ", len(points))
            res_dict = run.process(x)
            fit = res_dict['fit']
            ben = res_dict['ben']
            converged = res_dict['converged']
            converge.append(converged)
            #fit, ben = run.process(stopIDs)
            fitness.append(fit)
            bench.append(ben)
            res = RunResult(id=num_population, fitness=fit, bench=ben, converged=converged)
            result_lst.append(res)
            pop = res_dict['pop']
            jm = pop.journey_manager
            details = []
            for jou in jm.stops:
                details.append(jou.stop_details)
            stop_details[f'outer{j}-inner{i}'] = details

        print(f'whats {result_lst}')
        fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
        con_mean = reduce(lambda x, y: x + y, converge) / len(converge)
        bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
        res2 = [num_population, con_mean]
        print(res2)
        num_population += 30
        totals.append([num_population, con_mean])

    print(f'jour: {i} fit: {fit_mean} bench: {bench_mean}')
    print(totals)
    print(datetime.now())
    #print(stop_details)









