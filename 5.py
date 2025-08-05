import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


image = "omi.jpg"


ax = plt.gca()
ax.set_xlim(-15, 15)
ax.set_ylim(0, 20)


img=mpimg.imread(image)
img = np.array(img)

tx, ty = 1, 5
midx = 4
size = 10
w = img.shape[1]
h = img.shape[0]


img2 = np.empty(img.shape, dtype=img.dtype)
print(w, h)
print(img2.shape)
for hindex in range(h):
    for windex in range(w):
        pixel = img[hindex][windex]

        newxpos = w - windex - 1
        img2[hindex, newxpos] = pixel
ax.imshow(img, extent=(midx + tx, midx + tx + size, ty, ty + size))
ax.imshow(img2, extent=(midx - tx - size, midx - tx, ty, ty + size))

plt.show()