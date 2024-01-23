import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from PIL import Image


def calculate_h(s, k):
    identity_filter = np.zeros((s, s))
    identity_filter[s // 2, s // 2] = 1
    box_filter = np.ones((s, s)) / (s ** 2)
    h = (k + 1) * identity_filter - k * box_filter
    return h


s = int(input("Enter s: "))
k = int(input("Enter k: "))
image = Image.open('sample images/moon.tif')


h = calculate_h(s, k)
print("h =")
print(h)

sharpened_image = convolve2d(np.array(image.convert('L')), h, mode="same")

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(sharpened_image, cmap="gray")
plt.title("Sharpened")
plt.show()
