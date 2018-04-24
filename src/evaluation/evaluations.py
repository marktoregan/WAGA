from collections import namedtuple
from src.calc import distance as dis, midpoint as mp
# eval 1
#ga v neariest

#eval 2

#more evs
# eval 3
#ga v neariest

#more points
#ga v neariest

# eval 4
#penalties

#optimization

Coordinate = namedtuple('Coordinate', ['longitute', 'latitude'])

h = dis.Distance(Coordinate(longitute=-6.270447, latitude=53.339791),
             Coordinate(longitute=-2.991028, latitude=53.402061))
print(h.km)

DublinCity = Coordinate(latitude=53.338313, longitute=-6.238713)
Portlaoise = Coordinate(latitude=53.032791, longitute=-7.298212)

n = dis.Distance(DublinCity,Portlaoise)
print(n.km)

mid = mp.MidPoint(DublinCity,Portlaoise)
midway = mid.calc_midpoint()

n1 = dis.Distance(DublinCity, midway)
print(n1.km)


n2 = dis.Distance(Portlaoise, midway)
print(n2.km)