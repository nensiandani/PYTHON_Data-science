import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from SKimage import io

image=io.imread("tower.jpg")/255.0
h,w,c=image.shape

pixels=image.reshape(-1,c)
kmeans=KMeans(n_clusters=8,random_state=42,n_init=10).fit(pixels)

compressed_image=kmeans.cluster_centers_[kmeans.labels_].reshape(h,w,c)

plt.subplot(1,2,1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(compressed_image)
plt.title("compressed")
plt.show()