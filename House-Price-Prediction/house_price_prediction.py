import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


#load data
df = pd.read_csv("house_prices.csv")
print(df.head())
print(df.info())

#preprocessing
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)

#duplicate values
df.duplicated().sum()

#handling missing values
df.isnull().sum()
df.ffill(inplace=True)
print(df.isnull().sum())

#data cleaning
df.drop(columns=['Index'],inplace=True)

#Remove Useless Columns
df.drop(columns=['Title','Description','Society'], inplace=True)

#Clean Amount(in rupees)
def convert_amount(x):
    x = str(x)
    if 'Cr' in x:
        return float(x.replace('Cr','')) * 10000000
    elif 'Lac' in x:
        return float(x.replace('Lac','')) * 100000
    else:
        return np.nan
    
df['Amount(in rupees)'] = df['Amount(in rupees)'].apply(convert_amount)


#Clean Carpet Area
df['Carpet Area'] = df['Carpet Area'].str.replace(
    'sqft',
    '',
    regex=False
)

df['Carpet Area'] = pd.to_numeric(df['Carpet Area'], errors='coerce')


#Convert Categorical Columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col].astype(str))

# remove problematic columns
df.drop(columns=['Super Area','Dimensions','Plot Area'], inplace=True)

# remove remaining null values
df.dropna(inplace=True)

# check null values again
print(df.isnull().sum())

#Remove Extreme Outliers
df = df[df['Amount(in rupees)'] < 50000000]

#define X and y
X = df.drop(columns=['Amount(in rupees)', 'Price (in rupees)'])
y = df['Amount(in rupees)']

#Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

## ================= LR MODEL =====================

#Train Linear Regression

model = LinearRegression()
model.fit(X_train, y_train)

#Predictions
y_pred = model.predict(X_test)

#Evaluation

print("\nLINEAR REGRESSION RESULTS")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ================= RANDOMFOREST MODEL =================

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# train model
rf_model.fit(X_train, y_train)

# predictions
rf_y_pred = rf_model.predict(X_test)

# evaluation

print("\nRANDOM FOREST RESULTS")
print("MAE:", mean_absolute_error(y_test, rf_y_pred))
print("R2 Score:", r2_score(y_test, rf_y_pred))
rmse = np.sqrt(mean_squared_error(y_test, rf_y_pred))
print("RMSE:", rmse)

cv_scores = cross_val_score(
    rf_model,
    X,
    y,
    cv=5,
    scoring='r2'
)

print("\nCROSS VALIDATION R2 SCORES:")
print(cv_scores)
print("\nAverage CV R2 Score:", cv_scores.mean())

# ================ FEATURE IMPORTANCE ================

importance = rf_model.feature_importances_

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importance
})

feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print(feature_importance.head(10))
plt.figure(figsize=(10,6))

sns.barplot(
    x='Importance',
    y='Feature',
    data=feature_importance.head(10)
)

plt.title("Top 10 Important Features")
plt.savefig("feature_importance.png")
plt.show()


# ================= ACTUAL VS PREDICTED PLOT =================

plt.figure(figsize=(8,6))
plt.scatter(y_test, rf_y_pred, alpha=0.5)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")

plt.savefig("actual_vs_predicted.png")
plt.show()


# =============== CORRELATION HEATMAP ===============

plt.figure(figsize=(12,10))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")
plt.show()


# =============== XGBOOST MODEL ===============
xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_pred = xgb_model.predict(X_test)

print("\nXGBOOST RESULTS")
print("MAE:", mean_absolute_error(y_test, xgb_pred))
print("R2 Score:", r2_score(y_test, xgb_pred))

# ========= COMPARING ALL MODELS TOGETHER ========

print("\nBEST MODEL PERFORMANCE")

print("Linear Regression R2:",
      r2_score(y_test, y_pred))

print("Random Forest R2:",
      r2_score(y_test, rf_y_pred))

print("XGBoost R2:",
      r2_score(y_test, xgb_pred))

results = pd.DataFrame({
    'Model': ['Linear Regression', 'Random Forest', 'XGBoost'],
    'R2 Score': [
        r2_score(y_test, y_pred),
        r2_score(y_test, rf_y_pred),
        r2_score(y_test, xgb_pred)
    ]
})
print(results)


#Save Model

joblib.dump(xgb_model, "house_price_model.pkl")
print("Model Saved Successfully!")

print("\nPROJECT COMPLETED SUCCESSFULLY")