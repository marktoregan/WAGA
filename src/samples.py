from src import evchargepoints as evps

charge_types = ['Fast AC Type-2 44kW', 'Fast AC Type-2 50kW']
a, b = evps.EvChargePoints.get_by_type(charge_types)
print(len(a))
print(len(b))
#
# #print(a)
# #print(b)
#
# names = [k for k,v  in b.items()]
# print(len(names))
#
# print(list(set(names) - set(a)))
#
#
# ['mnmk3rzvj7vx-797','mnw5wx1023br-799']

crunched = [[5, 776.7443471681083, 747.3927500018164],
[25, 5988.81446830129, 6847.416793996776],
[45, 14457.091662778079, 17932.146139342858],
[65, 25846.675052364262, 31198.35912640958],
[85, 40037.777833015425, 53268.816777230124],
[105, 57175.28014059953, 76955.51210174963],
[125, 77128.30897707536, 106708.97286222168],
[145, 99695.89595531326, 142606.33138398017],
[165, 125669.00928930144, 183005.59869888544],
[185, 154016.5297949988, 229220.7455804435]]

time = [x[0] for x in crunched]
fit_mean = [x[1] for x in crunched]
bench_mean = [x[2] for x in crunched ]

print(time, fit_mean, bench_mean)