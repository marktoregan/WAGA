from src import  runga as rga
from datetime import datetime


if __name__ == '__main__':

    #Properties  Value

    #Crossover    probability 0.60

    #Power     mutation     index   0.25

   # Generation number 200

    #Number of runs 30

    print(datetime.now())

    run = rga.RunGA(available_stops=['mnyydut2usrq-871'], generations=2)
    generation_results, pop = run.process()

    print(generation_results)

    print(pop)
    print(datetime.now())
