import matplotlib.pyplot as plt


plt.style.use('seaborn-whitegrid')


crunched3 = [[75, 83183.19985099109, 20555.040456111426],
[106, 66401.06025326622, 17746.69935997649],
[571, 26295.57008029251, 11705.449166303879],
[572, 26311.37901528037, 12242.956195692244],
[683, 23941.58110125631, 11163.646836378142],
[716, 23543.47509907076, 11359.708815095164],
[720, 23539.269192006257, 11503.774984041658],
[745, 23175.109826328546, 11352.704790820413],
[747, 23167.574178083476, 11175.900354392881],
[759, 23259.38162791772, 11300.787878664583],
[825, 22005.754368685215, 11065.596740057386],
[837, 22434.37818830002, 11309.69235985205],
[872, 21766.53286591194, 11238.003864507287]]

time3 = [x[0] for x in crunched3]
fit_mean3 = [x[1] for x in crunched3]
bench_mean3 = [x[2] for x in crunched3]

print(time3, fit_mean3, bench_mean3)

times3 = time3
fit3 = fit_mean3
bench3 = bench_mean3
plt.plot(times3, fit3, color='green', label='GA')
plt.plot(times3, bench3, color='blue' , label='Bench Mark')
plt.xlabel('Number of journeys')
plt.ylabel('Cumulative wait time')
plt.title('5 charge points available - multi times and multi start and finish points')
plt.legend()
plt.show()
#
# #################################
#
crunched2 = [[75, 83101.26317144485, 20528.512917044176],
[106, 66539.94148680611, 18054.17120477128],
[571, 26559.926786395954, 11736.757201790442],
[572, 25907.513634357358, 11686.912928112073],
[683, 24256.57104646654, 11314.228207250435],
[716, 23764.74763665083, 11510.11049448694],
[720, 23618.79340946221, 11282.18614322227],
[745, 22947.102026203782, 11311.595762914189],
[747, 23385.54635657384, 11193.754091272898],
[759, 23188.111730792396, 10970.68000374198],
[825, 22373.937332161062, 11087.375365291697],
[837, 21877.816684302423, 11202.764187133642],
[872, 21688.84906223692, 11260.58323585117]]

time2 = [x[0] for x in crunched2]
fit_mean2 = [x[1] for x in crunched2]
bench_mean2 = [x[2] for x in crunched2]

print(time2, fit_mean2, bench_mean2)

times2 = time2
fit2 = fit_mean2
bench2 = bench_mean2
plt.plot(times2, fit2, color='green', label='GA')
plt.plot(times2, bench2, color='blue' , label='Bench Mark')
plt.xlabel('Number of journeys')
plt.ylabel('Cumulative wait time')
plt.title('5 charge points available - same times and multi start and finish points')
plt.legend()
plt.show()

####################################

crunched1 = [[75, 81660.75401146119, 137473.99970016265],
[106, 65760.03596832865, 137473.99970016265],
[571, 25880.406445724446, 137473.99970016265],
[572, 25977.222911474477, 137473.99970016265],
[683, 23665.653423732845, 137473.99970016265],
[716, 23311.466202071497, 137473.99970016265],
[720, 23153.001692608133, 137473.99970016265],
[745, 22828.32815946241, 137473.99970016265],
[747, 22856.53842105502, 137473.99970016265],
[759, 22428.220064748337, 137473.99970016265],
[825, 21566.815698861254, 137473.99970016265],
[837, 21649.27944417213, 137473.99970016265],
[872, 21388.91051808237, 137473.99970016265]]

time1 = [x[0] for x in crunched1]
fit_mean1 = [x[1] for x in crunched1]
bench_mean1 = [x[2] for x in crunched1]

print(time1, fit_mean1, bench_mean1)

times1 = time1
fit1 = fit_mean1
bench1 = bench_mean1
plt.plot(times1, fit1, color='green', label='GA')
plt.plot(times1, bench1, color='blue' , label='Bench Mark')
plt.xlabel('Number of journeys')
plt.ylabel('Cumulative wait time')
plt.title('5 charge points available - same point and time')
plt.legend()
plt.show()

