from src import runga as rga
from datetime import datetime
from functools import reduce
from collections import namedtuple
from src import evchargepoints as evps

if __name__ == '__main__':
    print('V3')
    print(datetime.now())
    RunResult = namedtuple('RunResult', 'id fitness bench converged')
    fitness_mean =[]
    bench_mean = []
    increase = 10
    totals=[]
    result_lst = []
    Results = namedtuple('Results', 'journney_num fit_mean bench_mean')
    fitness = []
    bench = []
    converge = []
    stop_details ={}
    runs = 10
    number_of_times = 10
    for j in range(0,runs): #7
        for i in range(0,number_of_times): #10
            print(f'on {i} of {number_of_times} and {j} of {runs}')
            run = rga.RunGA(generations=200, population_size=increase, num_of_journeys=150, initialise=True)
            jo = run.journey_manager
            evp = evps.EvChargePoints()
            points, preloaded = evp.get_stop_ids(journey_manager=jo,speeds=['fast'])
            x = [k for k, v in preloaded.items()]
            #print(x)
            #print("say what ", len(points))
            #stps = x[:increase]
            #print(stps)
            res_dict = run.process(x)
            fit = res_dict['fit']
            ben = res_dict['ben']
            converged = res_dict['converged']
            converge.append(converged)
            #fit, ben = run.process(stopIDs)
            fitness.append(fit)
            bench.append(ben)
            res = RunResult(id=increase, fitness=fit, bench=ben, converged=converged)
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
        res2 = [increase, con_mean]
        #print(res2)
        totals.append([increase, fit_mean, bench_mean, con_mean])
        increase += 20


    print(f'jour: {i} fit: {fit_mean} bench: {bench_mean}')
    print(totals)
    print(datetime.now())
    #print(stop_details)









