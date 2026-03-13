import numpy as np
import matplotlib.pyplot as plt
print('Program start')

x = 5

n = int(1e6)+1

xvals = []

for i in range(n):
    u = np.random.random()
    # print(x)
    # print(u)
    # print(0.1*np.exp(0.04*x))
    # print(1-0.1*np.exp(0.16*x))

    if x != 5:
        if u < 0.1*np.exp(0.04*x):
            x += 1
    if x != 1:
        if u > 1-0.1*np.exp(0.16*(x-1)): # We check the 'other side' of the unit interval,
            x -= 1                       # so there are no overlap issues 
    
    xvals.append(x)

xvals.append(6)
#Necessary to line up the histogram

plt.hist(xvals,bins=5,density=True,range=(0.5,5.5))

# plt.scatter(np.array([1,2,3,4,5])-0.2,np.array([0.29651214, 
#                                                 0.26298267, 
#                                                 0.2068695, 
#                                                 0.14432795,
#                                                 0.08930774]),label=r'eigenvector of $p^T$',c='r')

# plt.scatter(np.array([1,2,3,4,5])+0.2,
#             1/(1+np.exp(-0.12)+np.exp(-0.36)+np.exp(-0.72)+np.exp(-1.2))
#             *np.array([1,np.exp(-0.12),np.exp(-0.36),np.exp(-0.72),np.exp(-1.2)]),            
#             label='Detailed balance result',c='y')

plt.ylabel('Fraction of time spent')
plt.xlabel('State')

plt.legend()
plt.show()
