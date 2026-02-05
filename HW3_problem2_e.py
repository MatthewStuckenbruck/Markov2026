import numpy as np
import matplotlib.pyplot as plt

def advance(state):
    u = np.random.random()
    match state:
        case 'G':
            return 'G' if u<9/10 else 'S'
        case 'S':
            return 'S' if u<7/8 else 'D'
        case 'D':
            return 'D' if u<3/5 else 'G'

n = 1000000
m = 'G'

countG = 1
countS = 0
countD = 0

countGhist = []

for i in range(n):
    m = advance(m)
    match m:
        case 'G':
            countG += 1
        case 'S':
            countS += 1
        case 'D':
            countD += 1
    if i % 1000 == 0:
        countGhist.append(countG)

#Plot the value of the fraction over time - this is just for my own interest
countGhist = np.array(countGhist)
ivals = np.arange(1,n+1,1000)
frachist = countGhist/ivals
err = np.abs(frachist-20/41)

plt.plot(ivals,err)
plt.yscale('log')
plt.show()

#Print output proportion
print(countG/(n+1))