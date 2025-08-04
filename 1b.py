import matplotlib.pyplot as plt
import numpy as np

c = 3 * 10**8
fmax, fmin = c/(405*(10**-9)), c/(790*(10**-9))
f = np.linspace(fmin, fmax, 1000)

RHS = 1.731 - 0.261*(((f)/(10**15))**2)
print(RHS)
n = np.sqrt(np.sqrt(1/RHS) + 1)

plt.plot(f, n)
plt.show()