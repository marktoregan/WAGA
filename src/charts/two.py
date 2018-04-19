import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y2 = [1525, 1375, 1425, 1475, 1425, 1325, 1425, 1450, 1400, 1350]

point =[1, 0]


#plt.plot(x, y, label='10 concurrent journeys')

plt.plot(1,1, marker='s', markersize=12, label='Start point of journeys')
plt.plot(10,10, marker='s', markersize=12, label='End point of journeys')


plt.plot(3,3, marker='o', markersize=10, label='A - CP')
plt.plot(4,4, marker='o', markersize=10, label='B - CP')
plt.plot(5,5, marker='o', markersize=10, label='C - CP')
plt.plot(6,6, marker='o', markersize=10, label='D - CP')
plt.plot(7,7, marker='o', markersize=10, label='E - CP')



plt.xlabel('X')
plt.ylabel('Y')
plt.title('Phenotype')
plt.legend()
plt.show()


