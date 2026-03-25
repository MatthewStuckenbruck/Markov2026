import numpy as np

nextinct = 0

n = int(1e3)

a = 0.49

for i in range(n):
    x = 1
    
    ext = True

    ct = 0
    while x != 0:
        x = 2*np.random.binomial(x,1-a)
        ct += 1
        if ct >= 200:
            ext = False
            break
    
    if ext:
        nextinct += 1

print(nextinct/n)
print(a/(1-a))
