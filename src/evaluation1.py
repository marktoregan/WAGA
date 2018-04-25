from src import runga as rga, evchargepoint as evp
from datetime import datetime

class evvv():
    def __init__(self):
        pass
    def run(self):
        print(datetime.now())
        cpoints = evp.EvChargePoint()
        all_stops = cpoints.load_all_evps()
        stop_ids = [stop.id for stop in all_stops]
        print(stop_ids)
        run = rga.RunGA(available_stops=stop_ids, generations=1, population_size=10)
        generation_results, pop = run.process()

        print(generation_results)
        print(pop)

        print('fitness: {pop.get_fittest().get_fitness()}')
        print(datetime.now())

ev1 = evvv()

ev1.run()