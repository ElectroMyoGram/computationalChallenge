import matplotlib.pyplot as plt
import numpy as np

c = 345
L = 2
n1 = 1.0
n2 = 1.5

c1 = c / n1
c2 = c / n2

y = 1

x = np.linspace(0, 2, 1000)




term1  = np.sqrt(x**2 + y**2) / c1
term2 = np.sqrt((L-x)**2 + y**2) / c2

t = term1 + term2

mint = np.min(t)
minx = x[np.argmin(t)]


h1 = np.sqrt(minx**2 + y **2)
h2 = np.sqrt((L-minx)**2 + y**2)

sintheta = minx / h1
sinphi = (L-minx) / h2
print(sintheta / c1)
print(sinphi / c2)


plt.plot(x, t)
plt.scatter(minx, mint)
plt.show()