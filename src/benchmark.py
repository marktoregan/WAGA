from scipy.spatial import distance
from src import evchargepoint as evp
from src.calc import distance as dis

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

cpoints = evp.EvChargePoint()

x = cpoints.all_ev_charge_points()

all = cpoints.load_all_evps()

for a in all:
    print(a.location)

#print(x)

some_pt = (5, 5)

p = closest_node(some_pt, x)

print(p)


