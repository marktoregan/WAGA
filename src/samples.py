import random
from functools import reduce
from datetime import datetime, timedelta
from src import journeystop as js, journeystops as jss
from itertools import groupby

class Sample():
# lst = [0, 1, 2, 3, 4, 5]
# total_time = reduce(lambda x, y: x+25, lst,25)
# print(f'aaaa {total_time}')
#
# y = list(range(0,3))
#
# def less_than(x):
#     res = x < 0
#     return res
#
# stop_list = ['a', 'a', 'c', 'a', 'd', 'd', 'e']
#
# d = {x:stop_list.count(x) for x in stop_list}
#
# #print(f'{d}')
#
# stops = {"stops": {"ev_point_id": 1,
#                    "arrival_time": datetime.now(),
#                    "departure_time": 0,
#                    "wait_time": 0}}
#
# ct = stops["stops"]["arrival_time"]
# now_plus_10 = ct + timedelta(minutes=10)
#
# a = datetime.now()
# b = datetime.now() + timedelta(minutes=11)
# c = datetime.now() + timedelta(minutes=12)
# d = datetime.now() + timedelta(minutes=13)
#
# def to_epoch(ee):
#     return datetime(ee.year, ee.month, ee.day, ee.hour, ee.second).timestamp()
#
#
# stop1 = {"stops": {"ev_point_id": 1,
#                    "arrival_time": a.isoformat(timespec='microseconds'),
#                    "departure_time": 'a',
#                    "wait_time": 0}}
# stop2 = {"stops": {"ev_point_id": 1,
#                    "arrival_time": b.isoformat(timespec='microseconds'),
#                    "departure_time": 'b',
#                    "wait_time": 0}}
# stop3 = {"stops": {"ev_point_id": 1,
#                    "arrival_time": c.isoformat(timespec='microseconds'),
#                    "departure_time": 'c',
#                    "wait_time": 0}}
# stop4 = {"stops": {"ev_point_id": 1,
#                    "arrival_time": d.isoformat(timespec='microseconds'),
#                    "departure_time": 'd',
#                    "wait_time": 0}}
# lst = list()
# lst.append(stop2)
# lst.append(stop4)
# lst.append(stop1)
# lst.append(stop3)
#
# newlist = sorted(lst, key=lambda k: k['stops']['arrival_time'])
#
# #print(newlist)

    def get_fitness(self, lst):
        charge_time = 25
        ctime = datetime.now()
        journeys = list()
        for alloc in lst:
            stop = js.JourneyStop(ev_point_id=alloc,
                                  arrival_time=ctime,
                                  departure_time=0,
                                  wait_time=0,
                                  charge_time=charge_time)
            journeys.append(stop)
        jstops = jss.JourneyStops()
        time_total = jstops.total_time_of_stops(journeys)
        # print(f'score {time_total} for {self.journey_allocation}')
        return time_total

s = Sample()
lst_750 = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'a']
lst_375 = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e']
lst_3 = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'a']
lst_a = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
samp = ['e', 'c', 'd', 'b', 'a', 'd', 'b', 'a', 'c', 'd']
samp_order = ['a','a','b','b','c','c','d','d','d','e']
print(f'{s.get_fitness(lst_750)} {lst_750}')
print(f'{s.get_fitness(lst_375)} {lst_375}')
print(f'{s.get_fitness(lst_3) } should be 400')
print(f'{s.get_fitness(lst_a) } should be 1375')
print(f'{s.get_fitness(samp) } should be 400')
print(f'{s.get_fitness(samp_order) } should be 400')

words = 'aaAaAAbBbcCdDdDeEa'
w = list(words)

ww = sorted(w)

ww = [x.lower() for x in w]
print(ww)
for group, items in groupby(ww, lambda x: x.lower()):
    print(group, list(items))