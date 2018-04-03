import random


class Individual_OLD(object):

    def __init__(self, **kwargs):
        self.fitness = -1
        if kwargs is not None:
            self.chromosome_length = kwargs.get("chromosome_length", 0)
            self.chromosome = kwargs.get("chromosome", None)
        if self.chromosome_length > 0:
            ev = ['a', 'b', 'c', 'd', 'e']
            stops = [random.choice(ev) for x in range(self.chromosome_length)]
            self.chromosome = stops

    def __repr__(self):
        return '{}: {} '.format(self.__class__.__name__, self.fitness)

    def __lt__(self, other):
        return self.fitness < other.fitness
