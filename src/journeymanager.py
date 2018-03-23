class JourneyManager:
    stops = []
    #journey_route = []

    def add_journey(self, stop):
        self.stops.append(stop)

    def get_journey(self, index):
        return self.stops[index]

    def number_of_stops(self):
        return len(self.stops)

#Might need to added routes details here and accessing