from datetime import datetime
from src import journeymanager as jm, journey as jy

class PopulateJourneyManager(object):

    def __init__(self):
        self.journey_manager = jm.JourneyManager()
        self.start_time = datetime.now()

    def get_journey_manager(self, amount_of_journeys):
        for i in range(0, amount_of_journeys):
            journey = jy.Journey(start_time=self.start_time)
            self.journey_manager.add_journey(journey)
        return self.journey_manager
