# Step 1: Import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 2: Dataset
data = {
    'studytime': [1,2,3,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4],
    'absences': [10,2,5,1,7,3,12,0,6,2,15,1,8,3,14,0,9,4,11,1],
    'G3':        [5,12,14,18,10,15,4,19,11,16,3,20,9,17,2,19,8,14,6,18]
}

df = pd.DataFrame(data)

# Step 3: Features & Target
X = df[['studytime','absences']]
y = (df['G3'] >= 10).astype(int)

# Step 4: Train FULL Decision Tree (no limit)
dtree = DecisionTreeClassifier(random_state=0)
dtree.fit(X, y)

# ==============================
# 🌳 BIG TREE DIAGRAM
# ==============================
plt.figure(figsize=(20,10))  # bigger size

plot_tree(
    dtree,
    feature_names=['studytime','absences'],
    class_names=['Fail','Pass'],
    filled=True,
    rounded=True,
    fontsize=9
)

plt.title("FULL DECISION TREE (Detailed)", fontsize=16)
plt.show()

# ==============================
# 📊 OUTPUT
# ==============================
df['Prediction'] = dtree.predict(X)
df['Result'] = df['Prediction'].map({0:'Fail',1:'Pass'})

print("\n===== OUTPUT =====")
print(df[['studytime','absences','G3','Result']])

# ==============================
# 🎯 FINAL INPUT
# ==============================
new = pd.DataFrame({'studytime':[3],'absences':[4]})
final = dtree.predict(new)

print("\n===== FINAL PREDICTION =====")
print("Input → Studytime=3, Absences=4")
print("Output →", "Pass" if final[0]==1 else "Fail")
