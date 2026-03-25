import numpy as np

n = int(1e3)

a = 0.5

n3 = 0

for i in range(n):
    x = 1

    sum = 1
    while x != 0:
        x = 2*np.random.binomial(x,1-a)
        sum += x
        if sum > 3:
            break
    
    if sum == 3:
        n3 += 1

print(n3/n)