import random
from src import individual as ind
from src import population as pop
from functools import reduce
from datetime import datetime, timedelta
from collections import OrderedDict


i = ind.Individual(chromosome=[9, 0])

#print("{}".format(i.chromosome))

l = list(range(10))
#print(l)

l = [None] * 10
#print(l)



sc = pop.Population(population_size = 2, chromosome_length=9)

print("{}".format(sc.population))
aa = [i for i in sc.population]
for a in aa:
    print("aa  {}".format(a.fitness))

fit = sc.get_fittest(0)
print("fittest  {}".format(fit.fitness))

#lst1 = [1,5,6,7,3,98,1,4,0,9]
#di = dict(enumerate(lst1))
#print(di)

#res = min(di, key=di.get)
#print("lowest {}".format(res))
#di = {key: value for (key, value) in lst}

#di = {lambda x: x in lst}

#for k, v in di.items():
#    print("k {} v {}".format(k, v))
lst = [0, 1, 2, 3, 4, 5]
x = reduce(lambda x, y: x+25, lst,25)

#print(x)

y = list(range(0,3))
#print("y {}".format(y))

def less_than(x):
    res = x < 0
    return res

#a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
#d = {x:a.count(x) for x in a}
#d

stop_list = ['a', 'a', 'c', 'a', 'd', 'd', 'e']
d = {x:stop_list.count(x) for x in stop_list}
print(d)

#less_than_zero = list(filter(lambda x: less_than(x), number_list))
#print(less_than_zero)


stops = {"stops": {"ev_point_id": 1,
                   "arrival_time": datetime.now(),
                   "departure_time": 0,
                   "wait_time": 0}}

ct = stops["stops"]["arrival_time"]
now_plus_10 = ct + timedelta(minutes=10)
print("{}".format(ct))
print("{}".format(now_plus_10))

a = datetime.now()
b = datetime.now() + timedelta(minutes=10)
c = datetime.now() + timedelta(minutes=10)
d = datetime.now() + timedelta(minutes=10)

#a9 = datetime.fromtimestamp(a).isoformat()


def to_epoch(ee):
    return datetime(ee.year, ee.month, ee.day, ee.hour, ee.second).timestamp()

print('aaaa {} '.format(x))

#d = {"aa": a, "bb": b, "cc": c, "dd": d}
#s = [(k, d[k]) for k in sorted(d, key=d.get)]

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

#print(lst)
#for k, v in s:
    #print("{} : {}".format(k, v))

newlist = sorted(lst, key=lambda k: k['stops']['arrival_time'])

print(newlist)