
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.filters import roberts, sobel, scharr, prewitt


image = imread('images/Figure-41.jpg')
#green channel
image=image[:,:,1]
#edges = roberts(image)
edges = sobel(image)

# needs Qt
#from skimage.viewer import ImageViewer
#viewer = ImageViewer(image)
#viewer.show()

plt.imshow(image)
plt.show()

plt.imshow(edges)
plt.show()



