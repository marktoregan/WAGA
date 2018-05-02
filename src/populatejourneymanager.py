from datetime import datetime
from src import journeymanager as jm, journey as jy
from src.calc import normalize as nl, randomtimes as rd
from src.db import towns as tn
import random

class PopulateJourneyManager(object):

    def __init__(self):
        self.journey_manager = jm.JourneyManager()
        self.start_time = datetime.now()

    def get_journey_manager(self, amount_of_journeys):
        time = datetime.now()
        for i in range(0,amount_of_journeys):
            #time = rd.random_time("28/4/2018 1:30 PM", "28/4/2018 2:50 PM", random.random())
            dublin = nl.Normalize(latitude=53.350140, longitude=-6.266155)
            ennis = nl.Normalize(latitude=52.847054, longitude=-8.988436)
            #start_town = tn.Towns.get_start_town()
            #end_town = tn.Towns.get_end_town()
            journey = jy.Journey(start_time=time, starting_point=[ennis.x, ennis.y],
                                  end_point=[dublin.x, dublin.y])
            self.journey_manager.add_journey(journey)
        return self.journey_manager


