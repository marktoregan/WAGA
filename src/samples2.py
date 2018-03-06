from datetime import datetime, timedelta

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


def calcualte_stops_waits(wait_time):
    for idx, val in enumerate(sorted_by_arrival_time):
        if idx == 0:
            arrival_time = val['arrival_time']
            departure_time_wait = arrival_time + timedelta(minutes=wait_time)
            val['departure_time'] = departure_time_wait
            print(f"wait {idx} or {wait_time}")
        else:
            arrival_time = val['arrival_time']
            previous_depart_time = sorted_by_arrival_time[idx-1]['departure_time']
            if arrival_time < previous_depart_time:
                departure_time_wait = previous_depart_time - arrival_time
            else:
                departure_time_wait = timedelta(minutes=0)
            minutes = departure_time_wait.seconds/60
            val['wait_time'] = minutes
            departure_time_wait += timedelta(minutes=wait_time)
            dt = arrival_time + departure_time_wait
            val['departure_time'] = dt
            print(f'wait {idx} and {departure_time_wait}')

calcualte_stops_waits(25)
print(sorted_by_arrival_time)

print("#################")
print("calculate total time")

total_time= 0
for x in sorted_by_arrival_time:
    #print(x)
    arrive = x["arrival_time"]
    depart = x["departure_time"]
    diff = depart - arrive
    total_min = diff.total_seconds()/60
    total_time += total_min
    print(total_time)

    #total_mins += timedelta(diff)
    #print(total_mins)

# i now have the total time of a




