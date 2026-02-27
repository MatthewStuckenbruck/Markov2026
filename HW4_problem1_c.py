import numpy as np

q = 0.4
p = 0.35
s = 0.25

n = 1000000000

sum = 0

for i in range(n):

    x = 10
        
    #print("New attempt")

    while x != 0:

        u = np.random.random()
        if u < q:
            x = x-1
        elif u < p+q:
            x = x+1
        else:
            #print(x)
            sum += x
            break

print(sum/n)
    