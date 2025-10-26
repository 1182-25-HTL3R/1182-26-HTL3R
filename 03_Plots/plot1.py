__author__ = "Fabian Ha"

import math
import matplotlib.pyplot as plt

PI = math.pi
CNT = 1024
X = sorted([(-PI / (CNT / 2)) * i if i <= CNT / 2 else (PI / (CNT / 2)) * (CNT - i) for i in range(1024)])
C = [math.cos(x) for x in X]
S = [math.sin(x) for x in X]

plt.plot(X, C)
plt.plot(X, S)

plt.figure(figsize=(10, 6), dpi=80)
plt.plot(X, C, color="green", linewidth=2.5, linestyle="--", label="cosine")
plt.plot(X, S, color="purple", linewidth=2.5, linestyle="-.", label="sine")
plt.xlim(min(X) * 1.1, max(X) * 1.1)
plt.ylim(-1.05, 1.05)
plt.xticks([-PI, -PI / 2, 0, PI / 2, PI],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 1],
           [r'$-1$', r'$+1$'])
plt.legend(loc='upper left', frameon=False)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.annotate(
    '', xy=(1.01, 0.5), xytext=(1, 0.5),
    xycoords='axes fraction',
    arrowprops=dict(arrowstyle='->', lw=2, color='k')
)

ax.annotate(
    '', xy=(0.5, 1.01), xytext=(0.5, 1),
    xycoords='axes fraction',
    arrowprops=dict(arrowstyle='->', lw=2, color='k')
)

t = 2 * PI / 3
plt.plot([t, t], [0, math.cos(t)], color='green', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [math.cos(t), ], 50, color='green')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, math.cos(t)), xycoords='data',
             xytext=(-80, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, math.sin(t)], color='purple', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [math.sin(t), ], 50, color='purple')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, math.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

t = -PI / 4
plt.plot([t, t], [0, math.cos(t)], color='green', linewidth=2.5, linestyle="--")
plt.scatter([t], [math.cos(t)], 50, color='green')
plt.annotate(r'$\cos(-\frac{\pi}{4})=\frac{\sqrt{2}}{2}$',
             xy=(t, math.cos(t)), xycoords='data',
             xytext=(-110, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, math.sin(t)], color='purple', linewidth=2.5, linestyle="--")
plt.scatter([t], [math.sin(t)], 50, color='purple')
plt.annotate(r'$\sin(-\frac{\pi}{4})=-\frac{\sqrt{2}}{2}$',
             xy=(t, math.sin(t)), xycoords='data',
             xytext=(-60, -80), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

ax.set_axisbelow(True)

plt.title("Plot von Fabian Ha, HTL3R", fontsize=20)

plt.savefig("plot1_ha.png", dpi=72)

plt.show()
