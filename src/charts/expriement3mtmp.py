import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


crunched3 = [[5, 776.7443471681083, 747.3927500018164],
[25, 5988.81446830129, 6847.416793996776],
[45, 14457.091662778079, 17932.146139342858],
[65, 25846.675052364262, 31198.35912640958],
[85, 40037.777833015425, 53268.816777230124],
[105, 57175.28014059953, 76955.51210174963],
[125, 77128.30897707536, 106708.97286222168],
[145, 99695.89595531326, 142606.33138398017],
[165, 125669.00928930144, 183005.59869888544],
[185, 154016.5297949988, 229220.7455804435]]

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

#################################

crunched2 = [[5, 772.0528702068648, 712.7176682692079],
            [25, 5992.652883417106, 6634.702564613833],
            [45, 14388.80802750834, 17226.605924306612],
            [65, 25652.211373385653, 33691.220005707866],
            [85, 40031.08219922263, 48812.33005509842],
            [105, 57032.10485283892, 80610.52828174431],
            [125, 77127.8955705863, 108904.73841742885],
            [145, 100010.55921788535, 141517.95087459107],
            [165, 125501.85725885925, 185651.34511548586],
            [185, 154039.59655248612, 234308.5230361232]]

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

crunched1 = [[5, 961.9634974587159, 1021.8231979729992],
[25, 6897.833149872169, 11359.115989864995],
[45, 15656.099669769905, 31696.40878175699],
[65, 27241.42723233764, 62033.70157364897],
[85, 41653.180691758, 102370.994365541],
[105, 58887.80273929345, 152708.28715743302],
[125, 78942.26831030069, 213045.579949325],
[145, 101820.39779123015, 283382.87274121697],
[165, 127521.46587738574, 363720.16553310904],
[185, 156049.73204517964, 454057.45832500106]]

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