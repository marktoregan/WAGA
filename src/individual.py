import random


class Individual(object):

    def __init__(self, **kwargs):
        self.fitness = -1
        if kwargs is not None:
            self.chromosome_length = kwargs.get("chromosome_length", 0)
            self.chromosome = kwargs.get("chromosome", None)
        if self.chromosome_length > 0:
            ev = ['a', 'b', 'c']
            stops = [random.choice(ev) for x in range(self.chromosome_length)]
            self.chromosome = stops
