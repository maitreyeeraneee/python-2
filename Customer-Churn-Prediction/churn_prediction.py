# Customer Churn Prediction - Production-Level ML Code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (      
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    f1_score,
    roc_curve
)
from xgboost import XGBClassifier

warnings.filterwarnings('ignore')
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("CUSTOMER CHURN PREDICTION")
print("=" * 40)

# Load Dataset
file_path = r"c:\Users\Maitreyee\Desktop\python-2\Customer-Churn-Prediction\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)
print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Data Cleaning
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].mean(), inplace=True)
df.drop("customerID", axis=1, inplace=True)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
print(f"Cleaned | Churn distribution: {dict(df['Churn'].value_counts())}")

# EDA Plots
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x="Churn", data=df, ax=ax, palette="viridis")
ax.set_title("Churn Distribution")
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.savefig("plots/churn_distribution.png", dpi=150)
plt.show()

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["tenure"], kde=True, ax=ax, color="steelblue")
ax.set_title("Tenure Distribution")
plt.tight_layout()
plt.savefig("plots/tenure_distribution.png", dpi=150)
plt.show()

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df, ax=ax, palette="viridis")
ax.set_title("Monthly Charges vs Churn")
plt.tight_layout()
plt.savefig("plots/monthly_charges_vs_churn.png", dpi=150)
plt.show()

# Feature Engineering
df["AvgCharges"] = np.where(df["tenure"] > 0, df["TotalCharges"] / df["tenure"], 0)

# Feature Preparation
X = df.drop("Churn", axis=1)
y = df["Churn"]

X = pd.get_dummies(X, drop_first=True)
X = X.fillna(0)  # Fix NaN error

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Train: {len(X_train)} | Test: {len(X_test)}")

# Scaler for LR
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Unscaled for tree models
X_train_unscaled = X_train.copy()
X_test_unscaled = X_test.copy()

print("Features ready.")

# Model Training
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_scaled, y_train)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_model.fit(X_train_unscaled, y_train)

xgb_model = XGBClassifier(
    learning_rate=0.01,
    max_depth=5,
    n_estimators=200,
    eval_metric='logloss',
    random_state=42,
    use_label_encoder=False,
    n_jobs=-1
)
xgb_model.fit(X_train_unscaled, y_train)

print("Models trained.")

# Predictions
lr_pred = lr_model.predict(X_test_scaled)
lr_probs = lr_model.predict_proba(X_test_scaled)[:, 1]

rf_pred = rf_model.predict(X_test_unscaled)
rf_probs = rf_model.predict_proba(X_test_unscaled)[:, 1]

xgb_pred = xgb_model.predict(X_test_unscaled)
xgb_probs = xgb_model.predict_proba(X_test_unscaled)[:, 1]

# Evaluate Model Function
def evaluate_model(name, y_true, y_pred, y_probs):
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    roc_auc = roc_auc_score(y_true, y_probs)
    
    print(f"\n{name}")
    print("-" * 30)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC-AUC:  {roc_auc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    
    return {
        'model': name,
        'accuracy': accuracy,
        'f1_score': f1,
        'roc_auc': roc_auc
    }

# Model Evaluation
print("\nMODEL EVALUATION")
print("=" * 40)

results = []
results.append(evaluate_model("Logistic Regression", y_test, lr_pred, lr_probs))
results.append(evaluate_model("Random Forest", y_test, rf_pred, rf_probs))
results.append(evaluate_model("XGBoost", y_test, xgb_pred, xgb_probs))

# ROC-AUC Curves
fig, ax = plt.subplots(figsize=(10, 8))

fpr_lr, tpr_lr, _ = roc_curve(y_test, lr_probs)
ax.plot(fpr_lr, tpr_lr, 'b-', linewidth=2, 
        label=f'Logistic Regression (AUC = {roc_auc_score(y_test, lr_probs):.4f})')

fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_probs)
ax.plot(fpr_rf, tpr_rf, 'g-', linewidth=2, 
        label=f'Random Forest (AUC = {roc_auc_score(y_test, rf_probs):.4f})')

fpr_xgb, tpr_xgb, _ = roc_curve(y_test, xgb_probs)
ax.plot(fpr_xgb, tpr_xgb, 'r-', linewidth=2, 
        label=f'XGBoost (AUC = {roc_auc_score(y_test, xgb_probs):.4f})')

ax.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')

ax.set_xlabel('False Positive Rate', fontsize=12)
ax.set_ylabel('True Positive Rate', fontsize=12)
ax.set_title('ROC-AUC Curves - Model Comparison', fontsize=14, fontweight='bold')
ax.legend(loc='lower right', fontsize=10)
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("plots/roc_auc_curves.png", dpi=150)
plt.show()

# Model Comparison Bar Chart
model_names = [r['model'] for r in results]
accuracies = [r['accuracy'] for r in results]

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#3498db', '#2ecc71', '#e74c3c']
bars = ax.bar(model_names, accuracies, color=colors, edgecolor='black', linewidth=1.5)

for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax.annotate(f'{acc:.4f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=12, fontweight='bold')

ax.set_xlabel('Model', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Model Accuracy Comparison', fontsize=14, fontweight='bold')
ax.set_ylim([0, 1.0])
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig("plots/model_comparison_accuracy.png", dpi=150)
plt.show()

# Confusion Matrices
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

models = [('Logistic Regression', lr_pred, lr_probs),
          ('Random Forest', rf_pred, rf_probs),
          ('XGBoost', xgb_pred, xgb_probs)]

for idx, (name, preds, probs) in enumerate(models):
    cm = confusion_matrix(y_test, preds)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx])
    axes[idx].set_title(f'{name}\nROC-AUC: {roc_auc_score(y_test, probs):.4f}', 
                       fontsize=12, fontweight='bold')
    axes[idx].set_xlabel('Predicted')
    axes[idx].set_ylabel('Actual')

plt.tight_layout()
plt.savefig("plots/confusion_matrices.png", dpi=150)
plt.show()

# Feature Importance (Top 10)
feature_importances = pd.Series(
    rf_model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

top_10_features = feature_importances.head(10)

fig, ax = plt.subplots(figsize=(10, 8))
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(top_10_features)))
bars = ax.barh(range(len(top_10_features)), top_10_features.values, color=colors)

ax.set_yticks(range(len(top_10_features)))
ax.set_yticklabels(top_10_features.index)

ax.set_xlabel('Importance Score', fontsize=12)
ax.set_ylabel('Feature', fontsize=12)
ax.set_title('Top 10 Feature Importance (Random Forest)', fontsize=14, fontweight='bold')
ax.invert_yaxis()

for i, (bar, val) in enumerate(zip(bars, top_10_features.values)):
    ax.text(val + 0.002, bar.get_y() + bar.get_height()/2, 
            f'{val:.4f}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig("plots/feature_importance_top10.png", dpi=150)
plt.show()

print(f"\nTop 5 Features:")
for i, (feat, imp) in enumerate(top_10_features.head(5).items(), 1):
    print(f"  {i}. {feat}: {imp:.4f}")

# Results Summary
results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by='roc_auc', ascending=False)

print("\nFINAL RESULTS SUMMARY")
print("=" * 40)
print("\nModel Performance (sorted by ROC-AUC):")
print(results_df.to_string(index=False))

best_model = results_df.iloc[0]['model']
best_roc_auc = results_df.iloc[0]['roc_auc']
best_accuracy = results_df.iloc[0]['accuracy']

print(f"\nBest Model: {best_model}")
print(f"ROC-AUC: {best_roc_auc:.4f}")
print(f"Accuracy: {best_accuracy:.4f}")

print("\nKEY INSIGHTS")
print("=" * 40)
print("""
1. Customers with lower tenure tend to churn more.
2. Higher monthly charges increase churn likelihood.
3. Engineered feature 'AvgCharges' adds meaningful signal.
4. Tree-based models (RF, XGBoost) work better with unscaled data.
5. Logistic Regression requires scaled data for optimal performance.
6. XGBoost provides competitive performance with proper tuning.
7. ROC-AUC is a better metric than accuracy for imbalanced data.
""")

print("\nDone! Plots saved to Customer-Churn-Prediction/plots/")
