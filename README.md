<h1 align="center">🐍 Python-2 | Data Science Portfolio</h1>

<p align="center">
  Intermediate Data Science projects showcasing <b>EDA</b>, <b>Machine Learning</b>, and <b>Data Visualization</b> skills.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/NumPy-Computing-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Seaborn-Statistics-coral?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/XGBoost-Boosting-yellow?style=for-the-badge"/>
</p>

---

## 📖 Overview

Welcome to **Python-2** — my Phase 2 data science portfolio repository. This collection features hands-on projects that transition from Python fundamentals to real-world data science applications.

### 🎯 What You'll Find

| Project | Type | Description |
|---------|------|-------------|
| **Airbnb NYC EDA** | Exploratory Data Analysis | Analyze ~49K listings to uncover pricing trends, room types, and location insights |
| **Customer Churn Prediction** | Machine Learning | Build classification models to predict telecom customer churn |

---

## 🛠 Tech Stack

<p align="center">

| Category | Technologies |
|----------|---------------|
| **Languages** | Python 3.x |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Tools** | VS Code, Git, GitHub |

</p>

---

## 📂 Project Structure

```
python-2/
├── .gitignore
├── README.md
├── Airbnb-EDA/
│   ├── airbnb_eda.py              # Main EDA script
│   ├── AB_NYC_2019.csv           # Dataset (~49K listings)
│   ├── README.md
│   └── plots/                   # 7 visualizations
│       ├── price_distribution.png
│       ├── room_type_distribution.png
│       ├── neighbourhood_price.png
│       ├── correlation_heatmap.png
│       ├── geo_price_scatter.png
│       ├── neighbourhood_price_density.png
│       └── top_neigh_room_dist.png
└── Customer-Churn-Prediction/
    ├── churn_prediction.py       # Main ML pipeline
    ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
    ├── README.md
    └── plots/                   # 7 visualizations
        ├── churn_distribution.png
        ├── tenure_distribution.png
        ├── monthly_charges_vs_churn.png
        ├── roc_auc_curves.png
        ├── model_comparison_accuracy.png
        ├── confusion_matrices.png
        └── feature_importance_top10.png
```

---

## 📊 Featured Projects

### 🏡 House Price Prediction using Machine Learning

> **Objective:** Predict house prices with an end-to-end ML workflow—cleaning, feature engineering, cross-validation, and model evaluation.

| Feature | What I Did |
|--------|--------------|
| **Built with** | Python, Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, XGBoost |
| **Models** | Linear Regression, Random Forest, XGBoost |
| **Performance** | ~**0.90 R²** using Random Forest / XGBoost |
| **Pipeline** | Preprocessing → Feature Engineering → Cross-Validation → Evaluation → Model Saving |

#### 🔬 What Makes This Project Stand Out

- 🧹 Advanced preprocessing + encoding for a real-world regression task
- 🧠 Feature engineering to boost signal and reduce noise
- 🧪 Cross-validation for robust generalization
- 📊 Model evaluation with clean, recruiter-friendly visuals

#### 📈 Visual Insights

- 📌 **Feature importance analysis** (which variables matter most)
- 🔥 **Correlation heatmap** (multicollinearity awareness)
- 🏠 **Actual vs Predicted** visualization (prediction accuracy storytelling)

---

### 📉 Customer Churn Prediction

> **Objective:** Build an end-to-end ML pipeline to predict telecom customer churn.

| Component | Details |
|-----------|---------|
| **Models** | Logistic Regression, Random Forest, XGBoost |
| **Evaluation** | Accuracy, F1 Score, ROC-AUC |
| **Feature Engineering** | AvgCharges (TotalCharges/tenure) |

#### Workflow

```
Data Loading → Cleaning → Feature Engineering → Train-Test Split → Model Training → Evaluation
```

#### Model Comparison

| Model | Type | ROC-AUC Score |
|-------|------|--------------|
| **XGBoost** | Ensemble Boosting | Competitive |
| **Random Forest** | Ensemble Bagging | Strong |
| **Logistic Regression** | Linear | Reliable |

#### Key Insights

| Finding | Insight |
|---------|---------|
| 📉 Tenure & Churn | Lower tenure = higher churn risk |
| 💰 Monthly Charges | Higher charges → more churn |
| 🏆 Best Model | Tree-based models outperform linear |
| 🎯 Key Features | Tenure, MonthlyCharges, AvgCharges |

---

## 🚀 How to Run

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost
```

### 1️⃣ Airbnb NYC EDA

```bash
cd Airbnb-EDA
python airbnb_eda.py
```

**Output:**
- Console: Summary statistics
- `plots/`: 7 PNG visualizations

### 2️⃣ Customer Churn Prediction

```bash
cd Customer-Churn-Prediction
python churn_prediction.py
```

**Output:**
- Console: Model evaluation metrics
- `plots/`: 7 PNG visualizations

---

## ✨ What I Learned

✅ Working with messy real-world datasets  
✅ Missing value handling & outlier detection  
✅ Advanced Pandas transformations (groupby, pivot tables)  
✅ End-to-end ML pipeline development  
✅ Model comparison & evaluation  
✅ Data storytelling & business insights  
✅ Professional visualization practices  
✅ Git + GitHub workflow  

---

<p align="center">
  <b>📦 More projects coming soon | Stay tuned! 🚀</b>
</p>
