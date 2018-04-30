from datetime import datetime
from src import journeymanager as jm, journey as jy
from src.calc import normalize as nl, randomtimes as rd

import random

class PopulateJourneyManager(object):

    def __init__(self):
        self.journey_manager = jm.JourneyManager()
        self.start_time = datetime.now()

    def get_journey_manager(self, amount_of_journeys):
        print(f"in {amount_of_journeys}")
        for i in range(0,amount_of_journeys):
            time = rd.random_time("28/4/2018 1:30 PM", "28/4/2018 2:50 PM", random.random())
            dublin_city = nl.Normalize(latitude=53.338313, longitude=-6.238713)
            ennis = nl.Normalize(latitude=52.847054, longitude=-8.988436)
            journey1 = jy.Journey(start_time=time, starting_point=[ennis.x, ennis.y],
                                  end_point=[dublin_city.x, dublin_city.y])
            self.journey_manager.add_journey(journey1)
        return self.journey_manager

        Crumlin, Dublin, Ireland(53.328430, -6.304864)
        Cork, Ireland(51.903614, -8.468399)
        Limerick, Ireland(52.668018, -8.630498)
        Dublin, Ireland(53.353584, -6.251495)
        Dublin, Ireland(53.350140, -6.266155)
        Ballinasloe, Co.Galway, Ireland(53.328053, -8.224597)
        Gort, Co.Galway, Ireland(53.066643, -8.818749)


    # print(s)
    #
    # time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
    # time2 = datetime(year=2018, month=2, day=27, hour=13, minute=30)
    # time3 = datetime(year=2018, month=2, day=27, hour=14, minute=00)
    # time4 = datetime(year=2018, month=2, day=27, hour=14, minute=30)
    # time5 = datetime(year=2018, month=2, day=27, hour=15, minute=00)
    #
    # # print(f' ennis {ennis.x} {ennis.y}')
    #
    # # print(f'dublin {dublin_city.x} {dublin_city.y}')
    #
    # sligo = nl.Normalize(latitude=54.26969, longitude=-8.46943)
    # #
    #
    #
    # journey2 = jy.Journey(start_time=time1, starting_point=[sligo.x, sligo.y], end_point=[dublin_city.x, dublin_city.y])
    # # self.journey_manager.add_journey(journey2)
    #
    # journey3 = jy.Journey(start_time=time2, starting_point=[ennis.x, ennis.y], end_point=[dublin_city.x, dublin_city.y])
    # self.journey_manager.add_journey(journey3)
    #
    # journey4 = jy.Journey(start_time=time1, starting_point=[0, 3], end_point=[0, 7], stop=["mnyydut2usrq-871"])
    # # self.journey_manager.add_journey(journey4)
    #
    # journey5 = jy.Journey(start_time=time1, starting_point=[0, 4], end_point=[0, 6], stop=["c"])
    # # self.journey_manager.add_journey(journey5)
    #
    # journey6 = jy.Journey(start_time=time5, starting_point=[0, 1], end_point=[0, 5], stop=["c"])
    # # self.journey_manager.add_journey(journey6)
    #
    # journey7 = jy.Journey(start_time=time5, starting_point=[0, 2], end_point=[0, 10], stop=["d"])
    # # self.journey_manager.add_journey(journey7)
    #
    # journey8 = jy.Journey(start_time=time5, starting_point=[0, 3], end_point=[0, 9], stop=["d"])
    # # self.journey_manager.add_journey(journey8)
    #
    # journey9 = jy.Journey(start_time=time5, starting_point=[0, 4], end_point=[0, 8], stop=["e"])
    # # self.journey_manager.add_journey(journey9)
    #
    # journey10 = jy.Journey(start_time=time5, starting_point=[0, 5], end_point=[0, 7], stop=["e"])
    # # self.journey_manager.add_journey(journey10)


