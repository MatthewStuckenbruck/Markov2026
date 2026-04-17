import numpy as np
from scipy.integrate import quad

f1 = lambda z : np.exp(-1/2*z/(1-z)-1/5400*(z/(1-z))**3)*1/((1-z)**2)
f2 = lambda z : z/(1-z)*0.5*(1+(z/(1-z)/30)**2)*np.exp(-1/2* z/(1-z) -1/5400* (z/(1-z))**3)*1/((1-z)**2)

print(quad(f1,0,1))
print(quad(f2,0,1))
