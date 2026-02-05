import numpy as np

n = 10000

for steps in range(20):
    success = 0

    for i in range(n):
        x = 1

        for j in range(steps):
            u = np.random.rand()
            match x:
                case 1:
                    x = 1 if u<1/2 else 2
                case 2:
                    x = 2 if u<1/2 else 3
                case 3:
                    x = 3 if u<1/3 else 1 if u<2/3 else 4
                case 4: 
                    x = 4 if u<1/2 else 5
                case 5:
                    x = 6
                case 6:
                    x = 5
        if x == 4:
            success += 1

    print(f'{steps} steps: {success/n}')
#print(19/108)
