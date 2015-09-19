
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.filters import roberts, sobel, scharr, prewitt

image = imread('images/Figure-41.jpg')

edges = roberts(image)
edges = sobel(image)


