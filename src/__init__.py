from src import  runga as rga
from datetime import datetime
from src import evchargepoints as evcps

if __name__ == '__main__':

    #vars

    print(datetime.now())
    stop_ids = evcps.EvChargePoints.get_by_type("Fast AC Type-2 44kW")
    #stop_ids = evcps.EvChargePoints.get_by_type("Fast AC Type-2 44kW")
    run = rga.RunGA(available_stops=stop_ids, generations=1, population_size=10)
    run.process()
    print(datetime.now())
