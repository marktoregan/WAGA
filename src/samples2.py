from datetime import datetime, timedelta
from itertools import groupby

current_time1 = datetime(year=2018, month=2, day=27, hour=13, minute=00)
current_time2 = datetime(year=2018, month=2, day=27, hour=13, minute=10)
current_time3 = datetime(year=2018, month=2, day=27, hour=13, minute=15)
current_time4 = datetime(year=2018, month=2, day=27, hour=14, minute=16)
current_time5 = datetime(year=2018, month=2, day=27, hour=14, minute=22)

charge_time = 25

stop1 = {"ev_point_id": 1,
                   "arrival_time": current_time4,
                   "departure_time": 0,
                   "wait_time": 0,
                   "charge_time": 25}

stop2 = {"ev_point_id": 2,
                   "arrival_time": current_time1,
                   "departure_time": 0,
                   "wait_time": 0,
                   "charge_time": 25}


stop3 = {"ev_point_id": 1,
                   "arrival_time": current_time3,
                   "departure_time": 0,
                   "wait_time": 0,
                   "charge_time": 25}

stop4 = {"ev_point_id": 2,
                   "arrival_time": current_time2,
                   "departure_time": 0,
                   "wait_time": 0,
                   "charge_time": 25}

stop5 = {"ev_point_id": 1,
                   "arrival_time": current_time5,
                   "departure_time": 0,
                   "wait_time": 0,
                   "charge_time": 25}

journeys = list()

journeys.append(stop1)
journeys.append(stop2)
journeys.append(stop3)
journeys.append(stop4)
journeys.append(stop5)


sorted_by_arrival_time = sorted(journeys, key=lambda k: k['arrival_time'])

#print(f'{sorted_by_arrival_time}')


def print_totals(arrival_time_array):
    total_time = 0
    print( f'ar {arrival_time_array}' )

    for x in arrival_time_array:
        print(x)
        arrive = x["arrival_time"]
        depart = x["departure_time"]
        diff = depart - arrive
        total_min = diff.total_seconds() / 60
        total_time += total_min
        print(f'total of one group {total_time}')



def calculate_stops_waits(wait_time, charge_point):
    for idx, val in enumerate(charge_point):
        if idx == 0:
            arrival_time = val['arrival_time']
            departure_time_wait = arrival_time + timedelta(minutes=wait_time)
            val['departure_time'] = departure_time_wait
            print(f"wait {idx} or {wait_time}")
        else:
            arrival_time = val['arrival_time']
            previous_depart_time = charge_point[idx-1]['departure_time']
            if arrival_time < previous_depart_time:
                departure_time_wait = previous_depart_time - arrival_time
            else:
                departure_time_wait = timedelta(minutes=0)
            minutes = departure_time_wait.seconds/60
            val['wait_time'] = minutes
            departure_time_wait += timedelta(minutes=wait_time)
            dt = arrival_time + departure_time_wait
            val['departure_time'] = dt
            #print(f'wait {idx} and {departure_time_wait}')



for group, items in groupby(sorted_by_arrival_time, key=lambda x: x['ev_point_id']):
    c_point = list(items)
    calculate_stops_waits(25, list(items))
    print_totals(list(items))

print("#################")
print("calculate total time")


#print_totals()





