import numpy as np
import matplotlib.pyplot as plt

t = 0

maxt = 48
l = 3

# Problem c code

# ascores = []

# while t < maxt:
#     u = np.random.random()
#     t += -(1/l)*np.log(u)

#     if t < maxt:
#         ascores.append(t)

# t=0
# bscores = []

# while t < maxt:
#     u = np.random.random()
#     t += -(1/l)*np.log(u)

#     if t < maxt:
#         bscores.append(t)

# print(f'A score: {len(ascores)}')
# print(f'B score: {len(bscores)}')

# ascores = np.array(ascores)
# bscores = np.array(bscores)

# dumparr = np.concatenate([np.stack([ascores,np.zeros_like(ascores)]).T,np.stack([bscores,np.ones_like(bscores)]).T],axis=0)

# arr = dumparr[dumparr[:,0].argsort()]

#Problem d code

t = 0
scores = []

while t < maxt:
    u = np.random.random()
    t += -(1/(2*l))*np.log(u)

    if t < maxt:
        scores.append(t)

scores = np.array(scores)

arr = np.stack([scores,np.round(np.random.random( len(scores) ))]).T

print(f'A score: {sum(arr[:,1])}')
print(f'B score: {sum(1-arr[:,1])}')

#Together code

for x in arr:
    plt.plot([x[0],x[0]],[0,1],c='r' if x[1] == 0 else 'b',linewidth=1)

# for n in ascores:
#     plt.plot([n,n],[0,1],c='r')

# for n in bscores:
#     plt.plot([n,n],[0,1],c='b')

plt.xlabel('minutes elapsed')
plt.title('Superposition of HPPP')

plt.show()