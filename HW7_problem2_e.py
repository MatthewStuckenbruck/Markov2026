import numpy as np

def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def genPoiss(l):
    #Algorithm by Donald Knuth
    L=np.exp(-l)
    k=0
    p=np.random.random()

    while p > L:
        k += 1
        p *= np.random.random()

    return k
    # i = 0
    # p = np.exp(-l)*l**i/fact(i)
    # while True:
    #     print(f'looping with i={i}, u={u}, p={p}, l={l}')
    #     if u < p:
    #         return i

    #     if i > 100000:
    #         print('overflow')
    #         break

    #     i += 1
    #     p += np.exp(-l)*l**i/fact(i)

l = 3
t = 48

n = int(1e5)

dsum = 0
d2sum = 0

for i in range(n):
    N = genPoiss(2*l*t)
    NA = sum(np.round(np.random.random(N)))
    D=2*(2*NA-N)
    #print(N,NA,D)

    dsum += D
    d2sum += D**2

print(f'Expectation: {dsum/n}')
print(f'Variance: {d2sum/n-(dsum/n)**2}')
