import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")
# print(data)
x = data[:,0]
y = data[:,2]
# print(x, '\n', y)
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]


f1p = np.polyfit(x, y, 1, full=False)
f1 = np.poly1d(f1p)
fx = np.linspace(0, x, 500) 

plt.scatter(x, y, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='r')
plt.title('Стоймость квартиры от площади')
plt.xlabel("Площадь")
plt.ylabel("Стоймость")
# plt.xticks([w*7*24 for w in range(30)],["%i" % w for w in range(30)])
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.8')
print(f1([1650.3, 2200.4]))
plt.show()