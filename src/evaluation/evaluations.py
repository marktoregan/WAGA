from collections import namedtuple
from src.calc import distance as dis
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


DublinCity = Coordinate(latitude=53.338313, longitute=-6.238713)
Portlaoise = Coordinate(latitude=53.032791, longitute=-7.298212)


mid = mp.MidPoint(DublinCity,Portlaoise)
midway = mid.calc_midpoint()

