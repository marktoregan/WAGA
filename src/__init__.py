from src import runga as rga
from datetime import datetime
from functools import reduce


if __name__ == '__main__':
    print(datetime.now())
    fitness = []
    bench = []

    for i in range(0,1):
        charge_types = ['Fast AC Type-2 43kW', 'Fast AC Type-2 44kW', 'Fast AC Type-2 50kW', 'CHAdeMO DC 44kW',
                    'CHAdeMO DC 45kW', 'CHAdeMO DC 50kW', 'CHAdeMO DC 22kW', 'Combo DC 44kW', 'Combo DC 45kW',
                    'Combo DC 50kW']

        run = rga.RunGA(generations=1, population_size=15, num_of_journeys=10, initialise=True)
        fit, ben = run.process(charge_types)
        print(f'{fit} {ben}')
        fitness.append(fit)
        bench.append(ben)
        print(datetime.now())

    #l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
    fit_mean = reduce(lambda x, y: x + y, fitness) / len(fitness)
    bench_mean =reduce(lambda x, y: x + y, bench) / len(bench)
    print(f'fit: {fit_mean} bench: {bench_mean}')





