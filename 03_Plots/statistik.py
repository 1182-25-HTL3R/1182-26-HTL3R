__author__ = "Fabian Ha"

import subprocess
from matplotlib import pyplot as plt
from dateutil import parser

subpro = subprocess.Popen(
    ['/usr/bin/git', 'log', '--format=%an;%ad', '--author', 'Fabian Ha'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = subpro.communicate()

if stderr:
    print(stderr)
    exit()

lines = stdout.decode("utf-8").splitlines()
dates = []
for line in lines:
    date = line.split(";")[1]
    dt = parser.parse(date)
    dates.append(dt)

counter = dict()
for date in dates:
    if (date.hour, date.strftime("%a")) not in counter:
        counter[(date.hour, date.strftime("%a"))] = 1
        continue

    counter[(date.hour, date.strftime("%a"))] += 1

X = []
Y = []
sizes = []
wochentage = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for (hour, day), count in counter.items():
    X.append(hour)
    Y.append(wochentage.index(day))
    sizes.append(count * 100)

plt.figure(figsize=(5, 4), dpi=80)
plt.title(f"Fabian Ha: {len(dates)}")
plt.scatter(X, Y, s=sizes, alpha=0.7)
plt.xticks(range(0, 24, 2))
plt.yticks(range(len(wochentage)),
           ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"])
plt.ylabel("Wochentag")
plt.xlabel("Uhrzeit")
plt.grid(True, linestyle="-", alpha=0.5)
plt.xlim(-1, 24)
plt.ylim(-0.5, 6.5)
plt.savefig("plot2_ha.png")
plt.show()
