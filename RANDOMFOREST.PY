# Step 1: Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Step 2: Dataset
data = {
    'studytime': [1,2,3,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4],
    'absences': [10,2,5,1,7,3,12,0,6,2,15,1,8,3,14,0,9,4,11,1],
    'G3':        [5,12,14,18,10,15,4,19,11,16,3,20,9,17,2,19,8,14,6,18]
}
df = pd.DataFrame(data)

# Step 3: Features and target
X = df[['studytime','absences']]
y = (df['G3'] >= 10).astype(int)  # Pass if marks >= 10

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train Random Forest
rf = RandomForestClassifier(n_estimators=5, random_state=42)
rf.fit(X_train, y_train)

# Step 6: Accuracy
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nRandom Forest Accuracy:", round(accuracy,2))

# ==============================
# Step 7: Visualize all trees
# ==============================
n_trees = len(rf.estimators_)
fig, axes = plt.subplots(nrows=1, ncols=n_trees, figsize=(20,5))

for i, tree in enumerate(rf.estimators_):
    plt.sca(axes[i])
    plot_tree(
        tree,
        feature_names=['studytime','absences'],
        class_names=['Fail','Pass'],
        filled=True,
        rounded=True
    )
    axes[i].set_title(f"Tree {i+1}")

plt.tight_layout()
plt.show()

# ==============================
# Step 8: Prediction Table
# ==============================
results = X_test.copy()
results['Actual Result'] = y_test.map({0:'Fail',1:'Pass'})
results['Predicted Result'] = pd.Series(y_pred).map({0:'Fail',1:'Pass'})
print("\n===== PREDICTION TABLE =====")
print(results)

# ==============================
# Step 9: Final Prediction
# ==============================
new_student = pd.DataFrame({'studytime':[3],'absences':[4]})
final_pred = rf.predict(new_student)
print("\n===== FINAL PREDICTION =====")
print("Input: Studytime=3, Absences=4")
print("Predicted Result:", "Pass" if final_pred[0]==1 else "Fail")
