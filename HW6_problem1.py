import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(edgeitems=30, linewidth=100, 
    formatter=dict(float=lambda x: "%.3g" % x))

# p = np.array([[0,   1/2, 0,   1/2, 0,   0,   0,   0,   0  ],
#               [1/3, 0,   1/3, 0,   1/3, 0,   0,   0,   0  ],
#               [0,   1/2, 0,   0,   0,   1/2, 0,   0,   0  ],
#               [1/3, 0,   0,   0,   1/3, 0,   1/3, 0,   0  ],
#               [0,   1/4, 0,   1/4, 0,   1/4, 0,   1/4, 0  ],
#               [0,   0,   1/3, 0,   1/3, 0,   0,   0,   1/3],
#               [0,   0,   0,   1/2, 0,   0,   0,   1/2, 0  ],
#               [0,   0,   0,   0,   1/3, 0,   1/3, 0,   1/3],
#               [0,   0,   0,   0,   0,   1/2, 0,   1/2, 0  ]])

p = np.array([[0,1,0,0,0],
              [1/3,0,2/3,0,0],
              [0,1/2,0,1/2,0],
              [0,0,2/3,0,1/3],
              [0,0,0,1,0]])

evls, evcs = np.linalg.eig(p.T)

print(evls)
print(evcs)

p2 = p @ p
p4 = p2 @ p2
p8 = p4 @ p4
p16 = p8 @ p8
p32 = p16 @ p16

p50 = p32 @ p16 @ p2

q = np.array([0,1,0,0,0]) @ p50

xvals = np.array([1,2,3,4,5])

plt.scatter(xvals,q,label=r'$q_{50}(i)$')
plt.scatter(xvals,np.array([1/12,1/4,1/3,1/4,1/12]),label=r'$\pi(i)$')
plt.xlabel('i')
plt.legend()
plt.show()