import numpy as np
import matplotlib.pyplot as plt

# Construct lines
# x > 0
x = np.linspace(0, 20, 2000)



# 2y <= 12 -x 
y2 = (x*-1) + 4

# Make plot
# x > 2
plt.axvline(x=3)

plt.axhline(y=2.5, color="black")
plt.plot(x, y2, label=r'$2y\leq25-x$')

plt.xlim((0, 8))
plt.ylim((0, 8))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Fill feasible region

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()