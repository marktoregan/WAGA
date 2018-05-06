class JourneyManager:
    def __init__(self):
        self.stops = []

    def add_journey(self, stop):
        self.stops.append(stop)

    def get_journey(self, index):
        return self.stops[index]

    def number_of_stops(self):
        return len(self.stops)

    def set_journey_stop_details(self, index, details):
        jd = self.stops[index]
        jd.set_stop_details(details)
