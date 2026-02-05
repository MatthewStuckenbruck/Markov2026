import numpy as np

p = np.array([[9/10,1/10,0],[0,7/8,1/8],[2/5,0,3/5]])

#Method 1 (efficient)
p2 = p @ p
p4 = p2 @ p2
p8 = p4 @ p4
p16 = p8 @ p8
p32 = p16 @ p16
p50 = p32 @ p16 @ p2

#Method 2 to check if method 1 worked
def pow(p,n):
    ans = p
    for i in range(n-1):
        ans = ans @ p
    return ans

print(p50)
print(pow(p,50))
print(20/41)