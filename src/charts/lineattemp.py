from numpy import random
from scipy.spatial import distance

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
a = [[10,10], [5,5], [0,0], [1,0]]
some_pt = (1, 2)

p = closest_node(some_pt, a)

print(p)