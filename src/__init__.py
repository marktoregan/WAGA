from src import  runga as rga

if __name__ == '__main__':

    #Properties  Value

    #Crossover    probability 0.60

    #Power     mutation     index   0.25

   # Generation number 200

    #Number of runs 30

    run = rga.RunGA()
    run.process()