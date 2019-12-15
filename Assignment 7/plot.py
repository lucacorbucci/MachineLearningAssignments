import numpy as np
import matplotlib.pyplot as plt

# Construct lines
# x > 0
x = np.linspace(2, 20, 2000)


# y >= 2
y1 = (x*0) + 2

# 2y <= 12 -x 
y2 = (x*-1) + 12
# 4y >= 2x - 8 
y3 = (x - 3)/2
# y <= 2x - 5 
y4 = ((5*x)-4)/3

y5 = (2*x)/3

# Make plot
# x > 2
plt.axvline(x=2, label=r'$\Theta_1\geq2$')
#plt.axhline(y=2, color="black", label=r'$\Theta_2\geq2$')
plt.plot(x, y1, label=r'$\Theta_2\geq2$')

plt.plot(x, y2, label=r'$\Theta_1 + \Theta_2\leq12$')
plt.plot(x, y3, label=r'$-\Theta_1 + 2\Theta_2\geq-3$')
plt.plot(x, y4, label=r'$-5\Theta_1 + 3\Theta_2\leq-4$')
plt.plot(x, y5, label=r'$2\Theta_1 + 3\Theta_2$')

plt.xlim((0, 15))
plt.ylim((0, 20))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y2, y4)
y6 = np.maximum(y1, y3)
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
