import math


class MidPoint:

    def __init__(self, coord1, coord2):
        self.lon1 = math.radians(coord1.longitute)
        self.lat1 = math.radians(coord1.latitude)
        self.lon2 = math.radians(coord2.longitute)
        self.lat2 = math.radians(coord2.latitude)

    def get_midpoint_cordinates(self):
        bx = math.cos(self.lat2) * math.cos(self.lon2 - self.lon1)
        by = math.cos(self.lat2) * math.sin(self.lon2 - self.lon1)
        lat3 = math.atan2(math.sin(self.lat1) + math.sin(self.lat2), \
               math.sqrt((math.cos(self.lat1) + bx) * (math.cos(self.lat1) \
               + bx) + by**2))
        lon3 = self.lon1 + math.atan2(by, math.cos(self.lat1) + bx)

        return midwayCoord
