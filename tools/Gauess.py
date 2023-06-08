import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def gaussian_kernel(size, sigma):
    x, y = np.meshgrid(np.arange(-size//2+1, size//2+1), np.arange(-size//2+1, size//2+1))
    kernel = np.exp(-(x**2+y**2)/(2*sigma**2))
    kernel = kernel / np.sum(kernel)
    return kernel

size = 7
sigma = 1.5
kernel = gaussian_kernel(size, sigma)

plt.imshow(kernel, cmap='Blues')
plt.axis('off')
plt.show()