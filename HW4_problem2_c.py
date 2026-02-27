import numpy as np

x = np.array([0.2102, 0.2005, 0.2723, 0.4084, 0.8169, 0.0861])

print(x/np.linalg.norm(x,1))