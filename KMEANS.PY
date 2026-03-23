# ============================================
# CLEAN K-MEANS CLUSTER GRAPH (USING PCA)
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Dataset
data = {
    'fever':     [1,1,0,1,0,1,0,1,0,1],
    'cough':     [1,0,1,1,0,1,0,1,1,0],
    'headache':  [1,1,0,1,0,1,0,1,0,1],
    'fatigue':   [1,1,0,1,0,1,0,1,1,0],
    'nausea':    [0,1,0,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

# Step 2: Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Step 3: PCA (for clean 2D visualization)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 4: K-Means
kmeans = KMeans(n_clusters=2, random_state=0)
clusters = kmeans.fit_predict(X_pca)

# Step 5: Plot clean graph
plt.figure(figsize=(8,6))

# Plot clusters
plt.scatter(X_pca[:,0], X_pca[:,1], c=clusters)

# Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:,0], centroids[:,1], marker='X', s=200)

# Labels
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Clean Disease Pattern Clustering (K-Means + PCA)")

plt.grid()

plt.show()
