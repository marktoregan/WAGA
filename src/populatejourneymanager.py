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

        journey1 = jy.Journey(start_time=time1, starting_point=[0, 0], end_point=[10, 10], stop=["mnyydut2usrq-871"])
        self.journey_manager.add_journey(journey1)

        journey2 = jy.Journey(start_time=time1, starting_point=[0, 0], end_point=[10, 10], stop=["mnyydut2usrq-871"])
        self.journey_manager.add_journey(journey2)

        journey3 = jy.Journey(start_time=time1, starting_point=[0, 2], end_point=[0, 8], stop=["mnyydut2usrq-871"])
        self.journey_manager.add_journey(journey3)

        journey4 = jy.Journey(start_time=time1, starting_point=[0, 3], end_point=[0, 7], stop=["mnyydut2usrq-871"])
        self.journey_manager.add_journey(journey4)

        journey5 = jy.Journey(start_time=time1, starting_point=[0, 4], end_point=[0, 6], stop=["c"])
        #self.journey_manager.add_journey(journey5)

        journey6 = jy.Journey(start_time=time5, starting_point=[0, 1], end_point=[0, 5], stop=["c"])
        #self.journey_manager.add_journey(journey6)

        journey7 = jy.Journey(start_time=time5, starting_point=[0, 2], end_point=[0, 10], stop=["d"])
        #self.journey_manager.add_journey(journey7)

        journey8 = jy.Journey(start_time=time5, starting_point=[0, 3], end_point=[0, 9], stop=["d"])
        #self.journey_manager.add_journey(journey8)

        journey9 = jy.Journey(start_time=time5, starting_point=[0, 4], end_point=[0, 8], stop=["e"])
        #self.journey_manager.add_journey(journey9)

        journey10 = jy.Journey(start_time=time5, starting_point=[0, 5], end_point=[0, 7], stop=["e"])
        #self.journey_manager.add_journey(journey10)


        return self.journey_manager

    # def get_all_new(self):
    #
    #     ennis = co.Coordinate(latitude=52.847054, longitude=-8.988436)
    #     limerick = co.Coordinate(latitude=52.668018, longitude=-8.630498)
    #     waterford = co.Coordinate(latitude=52.25833, longitude=-7.11194)
    #     sligo = co.Coordinate(latitude=54.26969, longitude=-8.46943)
    #     portlaoise = co.Coordinate(latitude=53.032791, longitude=-7.298212)
    #     dublin_city = co.Coordinate(latitude=53.338313, longitude=-6.238713)
    #
    #     time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
    #     #time2 = datetime(year=2018, month=2, day=27, hour=13, minute=30)
    #     #time3 = datetime(year=2018, month=2, day=27, hour=14, minute=00)
    #     #time4 = datetime(year=2018, month=2, day=27, hour=14, minute=30)
    #     #time5 = datetime(year=2018, month=2, day=27, hour=15, minute=00)
    #
    #     journey1 = jy.Journey(start_time=time1, start_cord=dublin_city, end_cord=ennis)
    #     self.journey_manager.add_journey(journey1)
    #
    #     journey2 = jy.Journey(start_time=time1, start_cord=dublin_city, end_cord=limerick)
    #     self.journey_manager.add_journey(journey2)
    #
    #     return self.journey_manager


