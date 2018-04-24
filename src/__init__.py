from src import  runga as rga, ev_charge_point as evp
from datetime import datetime


if __name__ == '__main__':

    #Properties  Value

    #Crossover    probability 0.60

    #Power     mutation     index   0.25

   # Generation number 200

    #Number of runs 30

    print(datetime.now())
    cpoints = evp.EvChargePoint()
    all_stops = cpoints.load_all_evps()
    stop_ids = [stop.id for stop in all_stops]
    #print(stop_ids)
    run = rga.RunGA(available_stops=stop_ids, generations=1, population_size=10)
    #run = rga.RunGA(available_stops=['mnyydut2usrq-871'], generations=2)
    generation_results, pop = run.process()
    #
    print(generation_results)
    print(pop)
    #
    print('fitness: {pop.get_fittest().get_fitness()}')
    print(datetime.now())
