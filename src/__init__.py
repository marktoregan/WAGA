from src import  runga as rga
from datetime import datetime


if __name__ == '__main__':

    #vars

    print(datetime.now())
    #stop_ids = evcps.EvChargePoints.get_by_type("Fast AC Type-2 44kW")
    #run = rga.RunGA(generations=10, population_size=1000)
    run = rga.RunGA(generations=100, population_size=1000)
    run.process()
    print(datetime.now())
