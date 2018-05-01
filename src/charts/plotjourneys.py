import matplotlib.pyplot as plt

class PlotJourneys(object):

    def __init__(self, **kwargs):
        self.pop = kwargs.get("population")


    def plot_j(self):
        #x = range(0,1000)
        #y = range(0,1000)
        print('when am i called?')

        #plt.plot(x, y, label='10 concurrent journeys')

        print(self.pop.journey_manager.stops)
        for journey in self.pop.journey_manager.stops:
            #print(journey.starting_point)
            print(f'start {journey.starting_point[0]*10,journey.starting_point[1]*10}')
            print(f'end {journey.end_point[0] * 10, journey.end_point[1] * 10}')
            #plt.plot(journey.starting_point[0]*10,journey.starting_point[1]*10, marker='s', markersize=12, label='Start point of journeys')
            #plt.plot(journey.end_point[0]*10,journey.end_point[1]*10, marker='v', markersize=12, label='End point of journeys')
            #plt.plot(journey.starting_point*10, journey.end_point*10, label='10 concurrent journeys')
            #plt.plot(3,3, marker='o', markersize=10, label='A - CP')
            #plt.plot(4,4, marker='o', markersize=10, label='B - CP')
            #plt.plot(5,5, marker='o', markersize=10, label='C - CP')
            #plt.plot(6,6, marker='o', markersize=10, label='D - CP')
            #plt.plot(7,7, marker='o', markersize=10, label='E - CP')
            self.connectpoints(journey.starting_point, journey.end_point)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Phenotype')
        plt.legend()
        plt.show()


    def connectpoints(self, p1, p2):
        x1, x2 = p1[0], p2[0]
        print('f{x1, x2}')
        y1, y2 = p1[1], p2[1]
        plt.plot([x1, x2], [y1, y2], 'k-')
        plt.plot(x1, y1, 'ro')
        plt.plot(x2, y2, 'ro')
        #plt.axis('equal')
        #plt.show()



