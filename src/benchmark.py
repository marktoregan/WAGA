import random


class Benchmark(object):

    def __init__(self, **kwargs):
        self.random_allocation = []
        self.journey_manager = kwargs.get("journey_manager")
        self.stops_available = kwargs.get("stops")
        for journey in self.journey_manager:
            self.random_allocation.append(random.choice(self.stops_available))


    def print_it(self):
        for j in self.random_allocation:
            print(f'val : {j}')

