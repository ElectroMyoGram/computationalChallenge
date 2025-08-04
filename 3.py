import matplotlib.pyplot as plt
import numpy as np

c = 345
L = 2
n = 1.0
y = 1


x = np.linspace(0, 2, 1000)

term1  = np.sqrt(x**2 + y**2) / (c / n)
term2 = np.sqrt((L-x)**2 + y**2) / (c / n)

t = term1 + term2

mint = np.min(t)
minx = x[np.argmin(t)]


plt.plot(x, t)
plt.scatter(minx, mint)
plt.show()