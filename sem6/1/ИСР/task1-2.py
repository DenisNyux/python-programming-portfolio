import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")
square = data[:,0]
rooms = data[:,1]
cost = data[:,2]

# Удаляем nan
square = square[~np.isnan(square)]
rooms = rooms[~np.isnan(rooms)]
cost = cost[~np.isnan(cost)]
# print(square, rooms, cost)

# Среднее значение
avr_square = np.mean(square)
avr_rooms = np.mean(rooms)
avr_cost = np.mean(cost)
# print(avr_square, avr_rooms, avr_cost)

# Диспресия
var_square = np.var(square)
var_rooms = np.var(rooms)
var_cost = np.var(cost)
# print(var_square, var_rooms, var_cost)

# Среднеквадратичное отклонение
std_square = np.std(square)
std_rooms = np.std(rooms)
std_cost = np.std(cost)
print(std_square, std_rooms, std_cost)


