from src import journeystop as js
from datetime import datetime, timedelta
from itertools import groupby


class JourneyStops:

    def print_totals(self, arrival_time_array):
        total_time = 0
        for x in arrival_time_array:
            # print(x)
            arrive = x.arrival_time
            depart = x.departure_time
            diff = depart - arrive
            total_min = diff.total_seconds() / 60
            total_time += total_min
            print(f'total of group {total_time}')
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

    def run_it(self, sorted_by_arrival_time):
        tots = 0

        for group, items in groupby(sorted_by_arrival_time, key=lambda x: x.ev_point_id):
            c_point = list(items)
            self.calculate_stops_waits(25, c_point)
            tots += self.print_totals(c_point)
            print("#################")
            print(f"calculate total time {tots}")

charge_time = 25
current_time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
current_time2 = datetime(year=2018, month=2, day=27, hour=13, minute=10)
current_time3 = datetime(year=2018, month=2, day=27, hour=13, minute=15)
current_time4 = datetime(year=2018, month=2, day=27, hour=14, minute=16)
current_time5 = datetime(year=2018, month=2, day=27, hour=14, minute=22)

stop1 = js.JourneyStop(ev_point_id=1, arrival_time=current_time4, departure_time=0, wait_time=0, charge_time=charge_time)
stop2 = js.JourneyStop(ev_point_id=2, arrival_time=current_time1, departure_time=0, wait_time=0, charge_time=charge_time)
stop3 = js.JourneyStop(ev_point_id=1, arrival_time=current_time3, departure_time=0, wait_time=0, charge_time=charge_time)
stop4 = js.JourneyStop(ev_point_id=2, arrival_time=current_time2, departure_time=0, wait_time=0, charge_time=charge_time)
stop5 = js.JourneyStop(ev_point_id=1, arrival_time=current_time5, departure_time=0, wait_time=0, charge_time=charge_time)

journeys = list()

journeys.append(stop1)
journeys.append(stop2)
journeys.append(stop3)
journeys.append(stop4)
journeys.append(stop5)

sorted_by_arrival_time = sorted(journeys, key=lambda k: k.arrival_time)

for j in sorted_by_arrival_time:
    print(f'{j.arrival_time}')

jstops = JourneyStops()

jstops.run_it(sorted_by_arrival_time)

