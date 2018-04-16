from datetime import datetime
from src import journeymanager as jm, journey as jy

class PopulateJourneyManager(object):

    def __init__(self):
        self.journey_manager = jm.JourneyManager()
        self.start_time = datetime.now()

    def get_journey_manager(self, amount_of_journeys):

        time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
        time2 = datetime(year=2018, month=2, day=27, hour=13, minute=30)
        time3 = datetime(year=2018, month=2, day=27, hour=14, minute=00)
        time4 = datetime(year=2018, month=2, day=27, hour=14, minute=30)
        time5 = datetime(year=2018, month=2, day=27, hour=15, minute=00)

        journey1 = jy.Journey(start_time=time1, starting_point=[0, 0], end_point=[10, 10], stop=["a"])
        self.journey_manager.add_journey(journey1)

        journey2 = jy.Journey(start_time=time1, starting_point=[0, 0], end_point=[10, 10], stop=["a"])
        self.journey_manager.add_journey(journey2)

        journey3 = jy.Journey(start_time=time1, starting_point=[0, 2], end_point=[0, 8], stop=["b"])
        self.journey_manager.add_journey(journey3)

        journey4 = jy.Journey(start_time=time1, starting_point=[0, 3], end_point=[0, 7], stop=["b"])
        self.journey_manager.add_journey(journey4)

        journey5 = jy.Journey(start_time=time1, starting_point=[0, 4], end_point=[0, 6], stop=["c"])
        self.journey_manager.add_journey(journey5)

        journey6 = jy.Journey(start_time=time5, starting_point=[0, 1], end_point=[0, 5], stop=["c"])
        self.journey_manager.add_journey(journey6)

        journey7 = jy.Journey(start_time=time5, starting_point=[0, 2], end_point=[0, 10], stop=["d"])
        self.journey_manager.add_journey(journey7)

        journey8 = jy.Journey(start_time=time5, starting_point=[0, 3], end_point=[0, 9], stop=["d"])
        self.journey_manager.add_journey(journey8)

        journey9 = jy.Journey(start_time=time5, starting_point=[0, 4], end_point=[0, 8], stop=["e"])
        self.journey_manager.add_journey(journey9)

        journey10 = jy.Journey(start_time=time5, starting_point=[0, 5], end_point=[0, 7], stop=["e"])
        self.journey_manager.add_journey(journey10)


        return self.journey_manager