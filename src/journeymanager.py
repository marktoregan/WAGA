class TourManager:
    journeys = []

    def add_journey(self, journey):
        self.journeys.append(journey)

    def get_journey(self, index):
        return self.journeys[index]

    def number_of_journeys(self):
        return len(self.journeys)
