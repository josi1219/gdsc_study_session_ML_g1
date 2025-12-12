import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. Loading and cleaning the dataset
# -----------------------------
data = pd.read_csv("breast_cancer_bd.csv")

# Drop the sample code column (not needed for prediction)
data.drop("Sample code number", axis=1, inplace=True)

# Replace '?' with NaN
data.replace("?", np.nan, inplace=True)

# Fill missing values in 'Bare Nuclei' with the mode
data.fillna({"Bare Nuclei": data["Bare Nuclei"].mode()[0]}, inplace=True)

# -----------------------------
# 2. Prepare features and target
# -----------------------------
X = data.drop("Class", axis=1)  # features
y = data["Class"]               # target

# -----------------------------
# 3. Scale the features
# -----------------------------
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -----------------------------
# 4. Splitting data into training and test sets
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# 5. Training the Logistic Regression model
# -----------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# -----------------------------
# 6. Make predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 7. Evaluate the model
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Model Accuracy: {accuracy*100:.2f}%\n")
print("Confusion Matrix:")
print(cm)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# 8. The first 10 test predictions
# -----------------------------
print("\nFirst 10 Test set predictions")
for i, (pred, actual) in enumerate(zip(y_pred[:10], y_test[:10]), 1):  # first 10 predictions
    pred_label = "Benign (2)" if pred == 2 else "Malignant (4)"
    actual_label = "Benign (2)" if actual == 2 else "Malignant (4)"
    correct = "Correct" if pred == actual else "Wrong"
    print(f"Sample {i}: Predicted → {pred_label}, Actual → {actual_label}, Result → {correct}")
