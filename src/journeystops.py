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
                # print(f"wait {idx} or {wait_time}")
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
        sorted_by_arrival_time = sorted(journeys, key=lambda k: k.ev_point_id.lower())
        #newlist = sorted(ut, key=lambda x: x.count, reverse=True)
        total_time = 0
        for group, items in groupby(sorted_by_arrival_time, key=lambda x: x.ev_point_id.lower()):
            #print(f'group : {group}')
            c_point = list(items)
            self.calculate_stops_waits(25, c_point)
            total_time += self.total_time_of_stop(c_point)
        return total_time