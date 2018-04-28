from src import populatejourneymanager as pjm, evchargepoint as evp
from numpy import random
from scipy.spatial import distance


class Benchmark(object):

    def __init__(self, **kwargs):
        jm = pjm.PopulateJourneyManager()
        self.journey_manager = jm.get_journey_manager(10)


    def midpoint(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        point = ((x1 + x2) / 2, (y1 + y2) / 2)
        return point

    def midpoints(self):
        #print(self.journey_manager)
        points = {}
        cpoints = evp.EvChargePoint()
        #all_points = cpoints.all_ev_charge_points()
        all_points, all = cpoints.get_ev_charge_point_by_type(['Fast AC Type-2 44kW',
                                                          'Fast AC Type-2 50kW'
                                                            'CHAdeMO DC 44kW',
                                                            'Fast AC Type-2 43kW',
                                                            'Fast AC Type-2 44kW',
                                                            'Fast AC Type-2 50kW',
                                                            'CHAdeMO DC 45kW',
                                                            'CHAdeMO DC 50kW',
                                                            'CHAdeMO DC 22kW',
                                                            'Combo DC 44kW',
                                                            'Combo DC 45kW',
                                                            'Combo DC 50kW'])
        print(all)


        l = list(map(lambda x: (x.location,x.id), all_points))
        print(l)
        print(len(all_points))
        print(len(l))

        for j in self.journey_manager.stops:
            pass
            #print(len(all_points))
            #mid = (self.midpoint(j.starting_point, j.end_point))
            #p = self.closest_node(mid, all_points)
            #print(p)

    def closest_node(self, node, nodes):
        closest_index = distance.cdist([node], nodes).argmin()
        return nodes[closest_index]

    def run(self):
        self.midpoints()
        #cpoints = evp.EvChargePoint()
        #all_points = cpoints.all_ev_charge_points()
        #p = self.closest_node((5, 5), all_points)
        #print(p)


b = Benchmark()
b.run()





