import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift

x=np.array([[1,2],[2,3],[3,3],[8,8],[8,9]])
mean_shift=MeanShift()
mean_shift.fit(x)
plt.scatter(x[:,0],x[:,1],c=mean_shift.labels_,cmap='virdis',marker='0')
plt.show()