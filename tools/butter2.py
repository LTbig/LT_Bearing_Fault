import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def butterworth_kernel(size, cutoff, n):
    x, y = np.meshgrid(np.arange(-size//2+1, size//2+1), np.arange(-size//2+1, size//2+1))
    radius = np.sqrt(x**2+y**2)
    kernel = 1 / (1 + (radius/cutoff)**(2*n))
    kernel = kernel / np.sum(kernel)
    return kernel

size = 7
cutoff = 2
n = 2
kernel = butterworth_kernel(size, cutoff, n)

plt.imshow(kernel, cmap='Blues')
plt.axis('off')
plt.show()