
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.filters import roberts, sobel, scharr, prewitt

image = imread('images/Figure_41.jpg')
#green channel
image=image[:,:,1]
#edges = roberts(image)
edges = sobel(image)



