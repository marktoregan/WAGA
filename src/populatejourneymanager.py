from datetime import datetime
from src import journeymanager as jm, journey as jy
from src.calc import normalize as nl, randomtimes as rd
from src.db import towns as tn
import random
from collections import namedtuple

class PopulateJourneyManager(object):

    def __init__(self):
        self.journey_manager = jm.JourneyManager()
        self.start_time = datetime.now()

    def get_journey_manager(self, amount_of_journeys):
        City = namedtuple('City', 'name location')
        time = datetime.now()
        for i in range(0,amount_of_journeys):
            s_town = tn.Towns.get_start_town()
            e_town = tn.Towns.get_end_town()
            journey = jy.Journey(start_time=time,
                                 starting_point=[s_town.location.x, s_town.location.y],
                                 end_point=[e_town.location.x, e_town.location.y],
                                 from_city=s_town.name,
                                 to_city=e_town.name)
            self.journey_manager.add_journey(journey)
        return self.journey_manager



