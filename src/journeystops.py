from datetime import timedelta
from itertools import groupby


class JourneyStops:

    def total_time_of_stop(self, arrival_time_array):
        total_time = 0
        for x in arrival_time_array:
            # print(x)
            arrive = x.arrival_time
            depart = x.departure_time
            diff = depart - arrive
            total_min = diff.total_seconds() / 60
            total_time += total_min
        return total_time

    def calculate_stops_waits(self, wait_time, charge_point):
        for idx, val in enumerate(charge_point):
            if idx == 0:
                arrival_time = val.arrival_time
                departure_time_wait = arrival_time + timedelta(minutes=wait_time)
                val.departure_time = departure_time_wait
                #print(f"wait {idx} or {wait_time}")
            else:
                arrival_time = val.arrival_time
                previous_depart_time = charge_point[idx - 1].departure_time
                if arrival_time < previous_depart_time:
                    departure_time_wait = previous_depart_time - arrival_time
                else:
                    departure_time_wait = timedelta(minutes=0)
                minutes = departure_time_wait.seconds / 60
                val.wait_time = minutes
                departure_time_wait += timedelta(minutes=wait_time)
                dt = arrival_time + departure_time_wait
                val.departure_time = dt
                # print(f'wait {idx} and {departure_time_wait}')

    def total_time_of_stops(self, journeys):
        total_time = 0
        s = set()
        for journey in journeys:
            s.add(journey.ev_point_id.lower())
        for point in s:
            c_point = list(filter(lambda x: x.ev_point_id.lower() == point, journeys))
            c_points = sorted(c_point, key=lambda x: x.arrival_time, reverse=False)
            self.calculate_stops_waits(25, c_points)
            total_time += self.total_time_of_stop(c_points)
        return total_time