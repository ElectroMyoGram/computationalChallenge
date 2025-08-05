import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import map_coordinates

# --- Load image ---
img = mpimg.imread("omi.jpg").astype(np.float32)
if img.max() > 1: img /= 255.0
h, w, c = img.shape

f_const = 0.002
eps = 1e-6
# --- Define your custom functions ---
f = lambda x: -(f_const*x)/(x-f_const + eps)       # Horizontal wave
g = lambda y, x: (y * f(x)) / (x+eps)   # Vertical wave

# --- Create pixel grids ---
Y, X = np.indices((h, w))  # shape (h, w)
X_norm = X/w
Y_norm = Y/h
# --- Apply per-axis warping ---
X_warped = f(X_norm)
Y_warped = g(Y_norm, X_norm)
print(X)
print(X_warped)
print("X_warped range:", X_warped.min(), X_warped.max())
print("Y_warped range:", Y_warped.min(), Y_warped.max())
coords = np.array([Y_warped, X_warped])  # shape (2, h, w)

# --- Interpolate warped image ---
warped = np.ones_like(img)  # white background
for ch in range(c):
    warped[..., ch] = map_coordinates(
        img[..., ch], coords,
        order=1, mode='constant', cval=1.0
    )

print(warped)
# --- Pad original vertically if needed ---
# if warped.shape[0] > h:
#     pad_top = (warped.shape[0] - h) // 2
#     pad_bot = warped.shape[0] - h - pad_top
#     original_padded = np.pad(img, ((pad_top, pad_bot), (0, 0), (0, 0)), constant_values=1.0)
# else:
#     original_padded = img

# --- Concatenate side-by-side ---
# side_by_side = np.concatenate([original_padded, warped], axis=1)
# --- Show the result ---
# plt.figure(figsize=(12, 6))
plt.imshow(warped)
plt.title("Original (Left) and f(x), g(y) Warped (Right)")
plt.axis('off')
plt.show()
