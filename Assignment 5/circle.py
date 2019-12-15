import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
a = np.random.rand (40)

t1 = np.linspace (0, np.pi/2, len(a))
x1 = np.cos (t1)
y1 = np.sin (t1)

t2 = np.linspace (-np.pi/2, 0, len(a))
x2 = np.cos (t2)
y2 = np.sin (t2)

t3 = np.linspace (0, -np.pi/2, len(a))
x3 = np.cos (t3)
y3 = np.sin (t3)

t4 = np.linspace (-np.pi/2, 0, len(a))
x4 = np.cos (t4)
y4 = np.sin (t4)


fig = plt.figure()
ax1 = fig.add_subplot(111)

#sopra destra
ax1.scatter(x1, y1, c = 'red', marker = 'o')
#sotto destra
ax1.scatter (x2, y2, c = 'blue', marker = 'x')
#sopra sinistra
ax1.scatter (-x3, -y3, c = 'blue', marker = 'x')
#sotto sinistra
ax1.scatter (-x4, y4, c = 'red', marker = 'o')



fig2 = plt.figure()
ax = plt.axes(projection='3d')
x = x1
y = y1
z = abs(x+y)
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c='red', marker = 'o');

x = x2
y = y2
z = abs(x+y)
ax.scatter(x, y, z, c='blue', marker = 'x');

x = -x3
y = -y3
z = abs(x+y)
ax.scatter(x, y, z, c='blue', marker = 'x');

x = -x4
y = y4
z = abs(x+y)
ax.scatter(x, y, z, c='red', marker = 'o');

plt.show()
plt.show()