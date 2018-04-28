# import random
# from functools import reduce
# from datetime import datetime, timedelta
# from src import journeystop as js, journeystops as jss, evchargepoint as evp
# from itertools import groupby
# from tinydb import TinyDB, Query
#
#
# class Sample():
#
#     charge_time = 25
#     current_time = datetime.now()
#     stop1 = js.JourneyStop(ev_point_id='b',
#                                 arrival_time=current_time,
#                                 departure_time=0,
#                                 wait_time=0,
#                                 charge_time=charge_time)
#     stop2 = js.JourneyStop(ev_point_id='a',
#                                 arrival_time=current_time,
#                                 departure_time=0,
#                                 wait_time=0,
#                                 charge_time=charge_time)
#     stop3 = js.JourneyStop(ev_point_id='b',
#                                 arrival_time=current_time,
#                                 departure_time=0,
#                                 wait_time=0,
#                                 charge_time=charge_time)
#     stop4 = js.JourneyStop(ev_point_id='a',
#                                 arrival_time=current_time,
#                                 departure_time=0,
#                                 wait_time=0,
#                                 charge_time=charge_time)
#     stop5 = js.JourneyStop(ev_point_id='b',
#                                 arrival_time=current_time,
#                                 departure_time=0,
#                                 wait_time=0,
#                                 charge_time=charge_time)
#     stop6 = js.JourneyStop(ev_point_id='c',
#                            arrival_time=current_time,
#                            departure_time=0,
#                            wait_time=0,
#                            charge_time=charge_time)
#
#     journeys = list()
#     journeys.append(stop1)
#     journeys.append(stop2)
#     journeys.append(stop3)
#     journeys.append(stop4)
#     journeys.append(stop5)
#     journeys.append(stop6)
#     jstops = jss.JourneyStops()
#
#     print(jstops.total_time_of_stops(journeys))
#
#     evt1 = datetime.now()
#     evt2 = datetime.now() + timedelta(minutes=5)
#     evt3 = datetime.now() + timedelta(minutes=10)
#     evt4 = datetime.now() + timedelta(minutes=15)
#
#     charge_time = 25
#
#     stop1 = js.JourneyStop(ev_point_id='a',
#                            arrival_time=evt1,
#                            departure_time=0,
#                            wait_time=0,
#                            charge_time=charge_time)
#     stop2 = js.JourneyStop(ev_point_id='a',
#                            arrival_time=evt2,
#                            departure_time=0,
#                            wait_time=0,
#                            charge_time=charge_time)
#     stop3 = js.JourneyStop(ev_point_id='a',
#                            arrival_time=evt3,
#                            departure_time=0,
#                            wait_time=0,
#                            charge_time=charge_time)
#     stop4 = js.JourneyStop(ev_point_id='a',
#                            arrival_time=evt4,
#                            departure_time=0,
#                            wait_time=0,
#                            charge_time=charge_time)
#
#     journeys = list()
#     journeys.append(stop1)
#     journeys.append(stop2)
#     journeys.append(stop3)
#     journeys.append(stop4)
#     jstops1 = jss.JourneyStops()
#
#     print(jstops1.total_time_of_stops(journeys))

s = (1,2)
print(s[0], s[1])