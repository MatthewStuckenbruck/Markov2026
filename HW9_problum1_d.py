import numpy as np

i = 0

L=20

N = 1000

t = 0

tsum = 0

ivals = []

for q in range(N):
    i = 0
    #ivals = []
    while i != L:
        u = np.random.random()
        if i == 0:
            t += -np.log(u)
            i = 1
        else:
            t += -1/2*np.log(u)
            i += 1 if np.random.random() > 0.5 else -1
        #ivals.append(i)
    tsum += t

print(tsum)
