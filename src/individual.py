import random


class Individual:

    def __init__(self, chromosome, chromosome_length=0):
        if chromosome_length == 0:
            self.chromosome = chromosome
        else:
            ev = [0,1]
            stops = [random.choice(ev) for x in range(chromosome_length)]
            self.chromosome = stops
        self.fitness = -1

    def __str__(self):
        output = ""
        for gene in self.chromosome:
            output += self.chromosome[gene]
        return output
