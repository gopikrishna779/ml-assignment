# ============================================
# PCA WITH FULL CALCULATION EXPLANATION
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

print("\n===== STEP 1: ORIGINAL DATA =====")
print(df)

# ============================================
# STEP 2: MEAN & STD
# ============================================
print("\n===== STEP 2: MEAN & STANDARD DEVIATION =====")
print("Mean:\n", df.mean())
print("\nStandard Deviation:\n", df.std())

# ============================================
# STEP 3: STANDARDIZATION
# ============================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

print("\n===== STEP 3: STANDARDIZED DATA =====")
print(np.round(X_scaled, 2))

# ============================================
# STEP 4: COVARIANCE MATRIX
# ============================================
cov_matrix = np.cov(X_scaled.T)

print("\n===== STEP 4: COVARIANCE MATRIX =====")
print(np.round(cov_matrix, 2))

# ============================================
# STEP 5: EIGEN VALUES & VECTORS
# ============================================
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\n===== STEP 5: EIGEN VALUES =====")
print(np.round(eigenvalues, 3))

print("\n===== STEP 5: EIGEN VECTORS =====")
print(np.round(eigenvectors, 3))

# ============================================
# STEP 6: PCA TRANSFORMATION (sklearn)
# ============================================
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(X_pca, columns=['PC1','PC2'])

print("\n===== STEP 6: PCA TRANSFORMED DATA =====")
print(pca_df)

# ============================================
# STEP 7: EXPLAINED VARIANCE
# ============================================
print("\n===== STEP 7: EXPLAINED VARIANCE =====")
print("PC1:", round(pca.explained_variance_ratio_[0], 3))
print("PC2:", round(pca.explained_variance_ratio_[1], 3))
print("Total:", round(sum(pca.explained_variance_ratio_), 3))

# ============================================
# STEP 8: FINAL OUTPUT TABLE
# ============================================
final_df = df.copy()
final_df['PC1'] = pca_df['PC1']
final_df['PC2'] = pca_df['PC2']

print("\n===== STEP 8: FINAL OUTPUT =====")
print(final_df)

# ============================================
# STEP 9: GRAPH
# ============================================
plt.figure()

plt.scatter(X_pca[:,0], X_pca[:,1])

for i in range(len(X_pca)):
    plt.text(X_pca[i,0], X_pca[i,1], f"P{i}")

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Visualization (Detailed)")

plt.show()
