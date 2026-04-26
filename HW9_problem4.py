import numpy as np
import matplotlib.pyplot as plt

maxn = 50

xvals = np.arange(1,maxn)

beta = 1

y1vals = np.zeros_like(xvals,dtype='float64')
y2vals = np.zeros_like(xvals,dtype='float64')

for m in range(1,maxn):
    sum = 0
    for k in range(1,m):
        sum += 1/k

    y1vals[m-1] = 1/beta*sum
    y2vals[m-1] = 1/beta*np.log(m)

plt.plot(xvals,y1vals,label=r'$\frac{1}{\beta}\sum_{k=1}^{m-1}1/k$')
plt.plot(xvals,y2vals,label=r'$\frac{1}{\beta}\ln(m)$')
plt.xlabel('m')
plt.legend()
plt.show()
