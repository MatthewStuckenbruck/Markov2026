import numpy as np

def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

N = 60

sum = 0
for n in range(1,N+1):
    for b in range(N):
        sum += (np.exp(-2)*2**(n+b))/fact(n+b)*(np.exp(-1.5)*1.5**b)/fact(b)

print(sum)

sum = 0

for a in range(1,N+1):
    for b in range(a):
        sum += np.exp(-2)*2**a/fact(a)*np.exp(-1.5)*1.5**b/fact(b)

print(sum)

sum = 0

for n in range(N):
    sum += np.exp(-2)*2**n/fact(n)*np.exp(-1.5)*1.5**n/fact(n)

print(sum)

sum = 0

for b in range(1,N+1):
    for a in range(b):
        sum += np.exp(-2)*2**a/fact(a)*np.exp(-1.5)*1.5**b/fact(b)

print(sum)
