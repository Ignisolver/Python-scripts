import matplotlib.pyplot as plot
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

f1 = lambda x: 65/np.log(2*x+3) - 10
f2 = lambda x: x
f3 = lambda x: np.exp(x/10)/4
f4 = lambda x: -1/(np.exp((x-30)/10)/4)+99
f5 = lambda x: np.sin(x/30)*30 + 20
f6 = lambda x: np.sin((x+75)/50)*30 + 10
f7 = lambda x: np.log(x)*50
f8 = lambda x: -x/10+60
f9 = lambda x: np.sin(x/30)*40 + 15
f10 = lambda x: np.log(x+8)*21.75-30
f11 = lambda x: np.log(-x+100)*20+4

xs = list(map(lambda x: x/100, range(0, 10000)))
doors = [82]*2500 + [65]*2500 + [21]*3000 + [5]*2000
alice_presence = [53]*3000 + [74]*3000 + [102]*4000
alice_impact = list(map(f4,xs))
running = list(map(f1,xs))
assembly = list(map(f6,xs))
normal = list(map(f8,xs))
python = list(map(f5,xs))
cpp = list(map(f9,xs[0:3800]))+list(map(f10,xs[3800:10000]))
bug = list(map(f11, xs))

sets = (alice_impact, running, assembly, normal, python, cpp, bug)
names = ('A.S. incentive', 'running', 'assembly', 'normal', 'python', 'cpp', 'special', 'doors', 'A.S. presence', "predicted")
colors = ('red', 'orange', 'deeppink', 'deepskyblue', 'mediumblue', 'gray', 'green')

fig, plt = plot.subplots(figsize=(12, 7))

for nr, ys in enumerate(sets):
    plt.plot(xs,ys,colors[nr],linewidth=2)

plt.plot(xs[0:2500], doors[0:2500],'black',linewidth=3)
plt.plot(xs[0:3000], alice_presence[0:3000],'lime',linewidth=3)

sums = [0]*10000
set2 = (alice_impact, running, assembly, normal, python, cpp, bug,doors, alice_presence)
for i in range(10000):
    for el in set2:
        sums[i] += el[i]

sums = list(map(lambda x:x/len(set2), sums))
plt.plot(xs, sums, '--')

plt.plot(xs[2500:5000], doors[2500:5000],'black',linewidth=3)
plt.plot(xs[5000:8000], doors[5000:8000],'black',linewidth=3)
plt.plot(xs[8000:10000], doors[8000:10000],'black',linewidth=3)


plt.plot(xs[3000:6000], alice_presence[3000:6000],'lime',linewidth=3)
plt.plot(xs[6000:10000], alice_presence[6000:10000],'lime',linewidth=3)

plt.legend(names, fontsize=12, loc="center left", bbox_to_anchor=(1, 0.5))

plt.xaxis.set_major_locator(MultipleLocator(10))
plt.yaxis.set_major_locator(MultipleLocator(10))

plt.xaxis.set_minor_locator(AutoMinorLocator(5))
plt.yaxis.set_minor_locator(AutoMinorLocator(5))


plt.grid(which='minor', color='#CCCCCC', linestyle=':')
plt.axis([0,100,0,103])
plt.grid()
plt.grid(which='major', color='#CCCCCC', linestyle='-',linewidth=1.4)
plt.grid()
plot.ylabel("MG presence probability [ % ]", fontsize=15)
plot.xlabel("Impact strength [ % ]", fontsize=15)
# fig.set_size_inches(15, 10)
plot.tight_layout()
# plot.savefig("wykres.jpg", dpi=1000)

fig.show()


