import random
import calculatetotalminutes as ctm

genes = ["a", "b", "c", "d", "e"]


gene_set = [random.choice(genes) for x in range(10)]

print(gene_set)

v = (not 1 > 2)

lst = [0, 1, 2, 3, 4, 5]

for i in range(len(genes) - 1):
    start = genes[i]
    end = genes[i + 1]
    print("{},{}".format(start, end))
    #fitness += get_distance(start, end)

print(lst[-1])
print(v)

print(round(375.0, 2))

res = (345 > 399)
print('before not {}'.format(res))
l = (not 345 > 399)

print(l)


est_ev_points = ['a', 'e', 'd', 'b', 'e']
calc = ctm.CalculateTotalMinutes(est_ev_points)
result = calc.total_wait_time(25)
print(result)
