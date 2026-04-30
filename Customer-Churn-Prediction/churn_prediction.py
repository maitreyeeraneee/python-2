# 📌 1. Import Libraries
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Evaluation
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 📌 2. Load Dataset
df = pd.read_csv("c:/Users/Maitreyee/Desktop/python-2/Customer-Churn-Prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Preview:")
print(df.head())


# 📌 3. Basic Info & Cleaning
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Drop missing values (simple approach)
df.dropna(inplace=True)


# 📌 4. Encode Categorical Data
df = pd.get_dummies(df, drop_first=True)
print("\nAfter Encoding:")
print(df.head())


# 📌 5. Feature Selection
X = df.drop("Churn", axis=1)
y = df["Churn"]


# 📌 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 📌 7. Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 📌 8. Model Training

# Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)


# 📌 9. Predictions
lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)


# 📌 10. Evaluation
print("\n Logistic Regression ")
print("Accuracy:", accuracy_score(y_test, lr_pred))
print("\nClassification Report:\n", classification_report(y_test, lr_pred))

print("\n Random Forest ")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print("\nClassification Report:\n", classification_report(y_test, rf_pred))


# 📌 11. Confusion Matrix Visualization
def plot_conf_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

plot_conf_matrix(y_test, lr_pred, "Logistic Regression Confusion Matrix")
plot_conf_matrix(y_test, rf_pred, "Random Forest Confusion Matrix")


# 📌 12. Feature Importance (Random Forest)
feature_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
feature_importances.sort_values(ascending=False).plot(kind='bar')
plt.title("Feature Importance")
plt.show()
























