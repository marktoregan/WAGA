class Fitness:
    def __init__(self, total_time):
        self.TotalTime = total_time

    def __gt__(self, other):
        return self.TotalTime > other.TotalTime

    def __lt__(self, other):
        return self.TotalTime < other.TotalTime

    def __str__(self):
        return "{:0.2f}".format(self.TotalTime)

    def __eq__(self, other):
        return self.TotalTime == other.TotalTime
