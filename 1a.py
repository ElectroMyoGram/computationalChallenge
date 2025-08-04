import matplotlib.pyplot as plt
import numpy as np

#sellmier coefficients
a = np.array([1.03961212, 0.231792344, 1.01146945])
b = np.array([0.00600069867, 0.0200179144, 103.560653])

l = np.arange(400, 800, 0.1)
lsqrd = l**2
numerator = lsqrd[:, None] * a
denominator = lsqrd[:, None] - b

s = np.sum(numerator/denominator, axis=1)
n = np.sqrt(1 + s)

plt.plot(l, n)
plt.show()

