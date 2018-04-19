from numpy import random
from scipy.spatial import distance
from src import ev_charge_point as evp
#from mpl_toolkits.basemap import Basemap
from pyproj import Proj, transform


p1 = [0, 0]
p2 = [10, 10]



def midpoints(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    point = ((x1 + x2)/2, (y1 + y2)/2)
    return point

s = midpoints(p1,p2)

print(s)


def closest_node(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]

#a = random.randint(1000, size=(50000, 2))

cpoints = evp.EvChargePoint()

x = cpoints.all_ev_charge_points()

print(x)

some_pt = (5, 5)

p = closest_node(some_pt, x)

print(p)

inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')

x1,y1 = -11705274.6374,4826473.6922
x2,y2 = transform(inProj,outProj,x1,y1)

print(x2,y2)


#all_ev_charge_points