import numpy as np
import matplotlib.pyplot as plt

a = 0.99

n = 100

x = np.ones(n)
#print(x)

f = []

maxn = 300

for i in range(maxn):
    u = np.random.random(n)
    x = 1*(u>a)*(x==1)+2*(u<a)*(x==1)+1*(u<a)*(x==2)+3*(u>a)*(x==2)+2*(u>a)*(x==3)+3*(u<a)*(x==3)

    #print(x)

    f.append(sum(x==1)/n)

plt.scatter(np.linspace(1,maxn,maxn),f,s=1,label=r'Experimental $q_n(1)$')
plt.plot([1,maxn],[1/3,1/3],linestyle='--',label='Stationary distribution',c=(1,0.5,0))

xvals = np.linspace(0,300,301)
yvals = 0.3333+(-0.985038)**xvals*0.705305*0.705305-0.985038**xvals*0.411353*(-0.411353)
plt.scatter(xvals,yvals,label=r'Theoretical $q_n(1)$',s=1,c='r')

plt.xlabel('n')
plt.ylabel('Fraction of chains in state 1')
plt.title(f'N={n}')
plt.legend()
plt.show()
