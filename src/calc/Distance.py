import math


class Distance:
    '''
    use the haversine class to calculate the distance between
    two lon/lat coordnate pairs.
    output distance available in kilometers, meters, miles, and feet.
    example usage: Haversine([lon1,lat1],[lon2,lat2]).feet

    '''

    def __init__(self, coord1, coord2):
        lon1, lat1 = coord1
        lon2, lat2 = coord2

        R = 6371000  # radius of Earth in meters
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)

        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2.0) ** 2 + \
            math.cos(phi_1) * math.cos(phi_2) * \
            math.sin(delta_lambda / 2.0) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        self.meters = R * c  # output distance in meters
        self.km = self.meters / 1000.0  # output distance in kilometers
        self.miles = self.meters * 0.000621371  # output distance in miles
        self.feet = self.miles * 5280  # output distance in feet


if __name__ == "__Distance__":
    h = Distance.Distance([-6.270447, 53.339791], [-2.991028, 53.402061])
    print(h.km)