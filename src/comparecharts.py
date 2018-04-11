import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [1525, 1375, 1425, 1475, 1425, 1325, 1425, 1450, 1400, 1350]

plt.plot(x, y, label='GA Selected')
plt.plot(x2, y2, label='Random Selected')

plt.xlabel('Simlation')
plt.ylabel('Total Wait at EV Point')
plt.title('Genetic Algorithm Optimization and Ramdon Selection Chart')
plt.legend()
plt.show()