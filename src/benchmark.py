from scipy.spatial import distance
from src import evchargepoint as evp

from src.calc import distance as dis

#from mpl_toolkits.basemap import Basemap
from numpy import random


#h = dis.Distance([-6.270447, 53.339791], [-2.991028, 53.402061])
#

#h2 = dis.Distance([53.339479, -6.241077],[53.016218, -7.300986])

#h2 = dis.Distance([-6.241077, 53.339479],[-7.300986, 53.016218])

#Curriersbog
#Co. Laois

#53.016218, -7.300986

#print(h2.km)


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

all = cpoints.load_all_evps()

for a in all:
    print(a.location)

#print(x)

some_pt = (5, 5)

p = closest_node(some_pt, x)

print(p)



#print(x2, y2)


#all_ev_charge_points


#Treasury Building
#Grand Canal Street Lower, Grand Canal Dock, Dublin 2

#53.339479, -6.241077

#Curriersbog
#Co. Laois

#53.016218, -7.300986


#{"_default": {"1": {"evp": "mnwmp00vzsyr-0", "charge_type": "Type-2 AC Socket 3.7kW", "location": [0.0004859709617290923, -6.789089625130105e-05], "charge_time_required": 480, "longitude": 54.09804, "latitude": -7.55758, "name": "Slieve Russell Hotel, Belturbet-Ballyconnell Road (N87), Ballyconnell, County Cavan"},