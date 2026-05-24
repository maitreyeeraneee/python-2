import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

df = pd.read_csv("ab_data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.shape)
print("Duplicate Values:", df.duplicated().sum())

#Check Group Distribution
print(df['group'].value_counts())
print(df['landing_page'].value_counts())

#Check Conversion Rates
conversion_rates = df.groupby(
    'group'
)['converted'].mean()

print(conversion_rates)


sns.barplot(
    x=conversion_rates.index,
    y=conversion_rates.values
)

#Visualize Conversion Rates
plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.savefig("plots/basic_conversion_comparison.png")
plt.show()

#T-Test
control = df[
    df['group'] == 'control'
]['converted']

treatment = df[
    df['group'] == 'treatment'
]['converted']

t_stat, p_value = ttest_ind(
    control,
    treatment
)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Statistically Significant Result")
else:
    print("No Statistically Significant Difference")

# ================= CONVERSION RATE BARPLOT =================
conversion_rates = df.groupby(
    'group'
)['converted'].mean().reset_index()

plt.figure(figsize=(6,5))

sns.barplot(
    x='group',
    y='converted',
    data=conversion_rates
)

plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.savefig("plots/conversion_rates.png")
plt.show()

# ================= DISTRIBUTION PLOT =================

plt.figure(figsize=(6,5))
sns.histplot(
    data=df,
    x='converted',
    hue='group',
    multiple='dodge'
)

plt.title("Conversion Distribution")
plt.savefig("plots/conversion_distribution.png")
plt.show()

# ================= CONFIDENCE INTERVAL =================

control_mean = control.mean()
treatment_mean = treatment.mean()
difference = treatment_mean - control_mean
print("\nConversion Rate Difference:", difference)

# ===============- TIMESTAMP ANALYSIS ==================
df['timestamp'] = pd.to_datetime(df['timestamp'])

df['date'] = df['timestamp'].dt.date

daily_conversion = df.groupby(
    ['date', 'group']
)['converted'].mean().reset_index()

plt.figure(figsize=(12,6))

sns.lineplot(
    data=daily_conversion,
    x='date',
    y='converted',
    hue='group'
)

plt.title("Daily Conversion Trends")
plt.xticks(rotation=90)
plt.savefig("plots/daily_conversion_trends.png")
plt.show()


#=======================================

print("\nFINAL BUSINESS CONCLUSION")

if p_value < 0.05:
    print("The new landing page significantly improved conversions.")
else:
    print("The new landing page showed no statistically significant improvement in conversion rates.")

print("\nPROJECT COMPLETED SUCCESSFULLY")
