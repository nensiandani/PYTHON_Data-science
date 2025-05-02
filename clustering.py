import matplotlip.pyplot as plt
from sklearn.cluster import KMeans
x=[[1,2],[2,3],[3,3],[8,7],[8,8],[7,7]]
kmeans=KMeans(n_clusters=2,random_state=42)
kmeans.fit(x)
plt.scatter(*zip(*x),c=kmeans.Labels_,cmap='virdis')
plt.scatter(*zip(*kmeans.cluster_centers_),s=200,c='red',marker='x')
plt.show()