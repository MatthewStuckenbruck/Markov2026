import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

N = 60

tvals = np.linspace(0,90,901)
pvals = np.zeros_like(tvals)

for i,t in enumerate(tvals[:600]):
    sum = 0
    for n in range(N):
        sum += 3**n*(1-t/90)**(2*n)/(fact(n))**2
    sum *= np.exp(-3.5*(1-t/90))
    pvals[i] = sum

for i, t in enumerate(tvals[600:]):
    sum = 0
    for n in range(N):
        sum += 3**n*(1-t/90)**(2*n)/((n+1)*(fact(n))**2)
    sum *= 2*(1-t/90)*np.exp(-3.5*(1-t/90))
    pvals[i+600] = sum

plt.plot(tvals,pvals)
plt.ylim(0,1.05)
plt.xlabel('t')
plt.ylabel(r'$P(N_A=N_B)$')
plt.title(r'Probability of a tie assuming team $A$ scores at $t=60$')
plt.show()
