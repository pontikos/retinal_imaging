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

# probably need to threshold for clustering...

# do clustering
from sklearn import cluster
from sklearn.neighbors import kneighbors_graph
X = StandardScaler().fit_transform(X)
connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
connectivity = 0.5 * (connectivity + connectivity.T)
clustering = cluster.AgglomerativeClustering(linkage="average", affinity="cityblock", connectivity=connectivity, n_clusters=5000)
clustering.fit(X)
np.savetxt('clusters.csv',ward.labels_.astype(np.int))


