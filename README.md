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

## 🚀 Portfolio Highlights

- End-to-end Machine Learning workflows
- Statistical Analytics & Hypothesis Testing
- Exploratory Data Analysis (EDA)
- Feature Engineering & Model Evaluation
- Business-focused Data Storytelling
- Professional Git + GitHub workflow

###  What You'll Find

| Project | Domain | Description |
|---------|--------|-------------|
| 🏠 House Price Prediction | Machine Learning • Regression | Predict housing prices using Random Forest & XGBoost regression models |
| 🧪 A/B Test Analysis | Statistical Analytics | Perform hypothesis testing & conversion analysis for e-commerce experiments |
| 🏡 Airbnb NYC EDA | Exploratory Data Analysis | Analyze Airbnb listings to uncover pricing & neighborhood insights |
| 📉 Customer Churn Prediction | Machine Learning • Classification | Predict telecom customer churn using ensemble ML models |

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
├── AB-Test-Analysis/
│   ├── ab_test_analysis.py
│   ├── ab_data.csv
│   ├── README.md
│   └── plots/
├── Airbnb-EDA/
│   ├── airbnb_eda.py              # Main EDA script
│   ├── AB_NYC_2019.csv           # Dataset (~49K listings)
│   ├── README.md
│   └── plots/                   # 7 visualizations
├── House-Price-Prediction/
│   ├── house_price_prediction.py
│   ├── house_price_model.pkl
│   ├── README.md
│   └── plots/
└── Customer-Churn-Prediction/
    ├── churn_prediction.py       # Main ML pipeline
    ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
    ├── README.md
    └── plots/                   # 7 visualizations

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

---

### 📉 Customer Churn Prediction

> **Objective:** Build an end-to-end ML pipeline to predict telecom customer churn.

| Component | Details |
|-----------|---------|
| **Models** | Logistic Regression, Random Forest, XGBoost |
| **Evaluation** | Accuracy, F1 Score, ROC-AUC |
| **Feature Engineering** | AvgCharges (TotalCharges/tenure) |


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

## 🧪 Phase 2 Project • A/B Test Analysis for E-Commerce

<p align="center">
  <img src="https://img.shields.io/badge/A--B%20Testing-Experiment-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Statistics-Hypothesis%20Testing-2b9eb3?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/T--Test-SciPy-ff6b6b?style=for-the-badge"/>
</p>

> **Objective:** Determine whether a new e-commerce landing page (treatment) improves conversion rate vs the current page (control) using a statistically defensible A/B testing workflow.

### Project Overview
- Data cleaning & validation (missing values, duplicates, group checks)
- Conversion rate analysis (descriptive + visualization)
- Hypothesis testing with **independent two-sample T-test**
- Confidence-interval-ready interpretation (conversion lift framing)
- Time-series conversion trend analysis
- Business-ready conclusion (recommendation or no decision)

### Tech Stack
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- SciPy (hypothesis testing)

### Key Features
- Conversion distribution + conversion-by-group visuals
- Daily conversion trend line plot
- Clear statistical decision rule based on **p-value < 0.05**

### Statistical Testing (What’s Used)
- Outcome `converted` is treated as a binary variable (0/1)
- **SciPy `ttest_ind`** compares mean conversion between `control` and `treatment`
- Outputs:
  - **T-statistic** (separation of group means)
  - **p-value** (evidence against H₀)

### Business Conclusion (Decision Logic)
- **If p-value < 0.05:** recommend rollout of the new landing page
- **Else:** no statistically reliable improvement → hold / iterate

### Key Insights (Storytelling)
- Lift direction: treatment vs control conversion rate
- Statistical reliability: significant vs not significant
- Temporal stability: whether daily trends support consistency

### Project Link
- **A/B Test Analysis for E-Commerce:** [AB-Test-Analysis/README.md](./AB-Test-Analysis/README.md)
- Script: `AB-Test-Analysis/ab_test_analysis.py`

---

<p align="center">
  <b> Building real-world Machine Learning, Analytics, and Data Science projects consistently.
</p>

