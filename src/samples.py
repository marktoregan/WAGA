import random
from functools import reduce
from datetime import datetime, timedelta


lst = [0, 1, 2, 3, 4, 5]
total_time = reduce(lambda x, y: x+25, lst,25)
print(f'aaaa {total_time}')

y = list(range(0,3))

def less_than(x):
    res = x < 0
    return res

stop_list = ['a', 'a', 'c', 'a', 'd', 'd', 'e']

d = {x:stop_list.count(x) for x in stop_list}

print(f'{d}')

stops = {"stops": {"ev_point_id": 1,
                   "arrival_time": datetime.now(),
                   "departure_time": 0,
                   "wait_time": 0}}

ct = stops["stops"]["arrival_time"]
now_plus_10 = ct + timedelta(minutes=10)

a = datetime.now()
b = datetime.now() + timedelta(minutes=11)
c = datetime.now() + timedelta(minutes=12)
d = datetime.now() + timedelta(minutes=13)

def to_epoch(ee):
    return datetime(ee.year, ee.month, ee.day, ee.hour, ee.second).timestamp()



stop1 = {"stops": {"ev_point_id": 1,
                   "arrival_time": a.isoformat(timespec='microseconds'),
                   "departure_time": 'a',
                   "wait_time": 0}}
stop2 = {"stops": {"ev_point_id": 1,
                   "arrival_time": b.isoformat(timespec='microseconds'),
                   "departure_time": 'b',
                   "wait_time": 0}}
stop3 = {"stops": {"ev_point_id": 1,
                   "arrival_time": c.isoformat(timespec='microseconds'),
                   "departure_time": 'c',
                   "wait_time": 0}}
stop4 = {"stops": {"ev_point_id": 1,
                   "arrival_time": d.isoformat(timespec='microseconds'),
                   "departure_time": 'd',
                   "wait_time": 0}}
lst = list()
lst.append(stop2)
lst.append(stop4)
lst.append(stop1)
lst.append(stop3)

newlist = sorted(lst, key=lambda k: k['stops']['arrival_time'])

print(newlist)

