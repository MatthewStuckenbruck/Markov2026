import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(0,15,200)

fvals = 1/3*xvals*(1+xvals)*np.exp(-xvals)
a = -1+np.sqrt(3)
c = 1/(3*a**2*(1-a)*np.exp(a))
cgvals = c*a**2*xvals*np.exp(-a*xvals)

plt.plot(xvals,fvals,label=r'$f(x)$')
plt.plot(xvals,cgvals,label=r'$c(a^*)g_{a^*}(x)')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title(r'Plot of $f(x)$ vs $c(a^*)g_{a^*}(x)$')
plt.show()