import random
from functools import reduce
from datetime import datetime, timedelta
from src import journeystop as js, journeystops as jss, ev_charge_point as evp
from itertools import groupby
from tinydb import TinyDB, Query


class Sample():
    current_time = datetime.now()
    charge_time = 25

    stop1 = js.JourneyStop(ev_point_id='b',
                                arrival_time=current_time,
                                departure_time=0,
                                wait_time=0,
                                charge_time=charge_time)
    stop2 = js.JourneyStop(ev_point_id='a',
                                arrival_time=current_time,
                                departure_time=0,
                                wait_time=0,
                                charge_time=charge_time)
    stop3 = js.JourneyStop(ev_point_id='b',
                                arrival_time=current_time,
                                departure_time=0,
                                wait_time=0,
                                charge_time=charge_time)
    stop4 = js.JourneyStop(ev_point_id='a',
                                arrival_time=current_time,
                                departure_time=0,
                                wait_time=0,
                                charge_time=charge_time)
    stop5 = js.JourneyStop(ev_point_id='b',
                                arrival_time=current_time,
                                departure_time=0,
                                wait_time=0,
                                charge_time=charge_time)

    journeys = list()
    journeys.append(stop1)
    journeys.append(stop2)
    journeys.append(stop3)
    journeys.append(stop4)
    journeys.append(stop5)
    jstops = jss.JourneyStops()

    print(jstops.total_time_of_stops(journeys))
    #225



    # ney = Query()
    # db.insert({'name': 'John', 'age': 22})
    #
    # self.id = kwargs.get("id", 0)
    # self.charge_type = kwargs.get("charge_type", 0)
    # self.location = kwargs.get("location", [0, 0])
    # self.occupied = kwargs.get("occupied", False)
    # self.time_occupied = kwargs.get("time_occupied")
    # self.charge_time_required = kwargs.get("charge_time_required", 25)