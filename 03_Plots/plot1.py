__author__ = "Fabian Ha"

import math
import matplotlib.pyplot as plt

PI = math.pi
CNT = 1024
X = sorted([ (-PI / (CNT / 2)) * i if i <= CNT / 2 else (PI / (CNT / 2)) * (CNT-i) for i in range(1024)])
C = [ math.cos(x) for x in X ]
S = [ math.sin(x) for x in X ]

plt.plot(X, C)
plt.plot(X, S)
plt.savefig("plot1_ha.png", dpi=72)

plt.show()
