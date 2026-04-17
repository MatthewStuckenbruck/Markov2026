import numpy as np
import matplotlib.pyplot as plt

f = lambda t : 0.5*(1+(t/30)**2)

tmax = 120

maxl = f(tmax)

t = 0

origsamples = []

while t < tmax:
    u = np.random.random()
    t += -1/maxl*np.log(u)
    if t < tmax:
        origsamples.append(t)

samples = []

for samp in origsamples:
    u = np.random.random()
    if u < f(samp)/maxl:
        samples.append(samp)

plt.hist(samples,range=(0,tmax),bins=tmax)

print(f'Number of reports: {len(samples)}')

xvals = np.linspace(0,tmax,200)
plt.plot(xvals,f(xvals),c='r',label=r'Expected daily rate ($\lambda(t)$)')

plt.xlabel('Time (days)')
plt.ylabel('Number of flu reports')
plt.legend()
plt.show()
