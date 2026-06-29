import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("datasets/india_lpg_crisis.csv")

print("Complete Dataset")
print(data)

print("\nFirst 5 Rows")
print(data.head())
print("\nLast 5 Rows")
print(data.tail())
df = data[['Year','State','Monthly_Demand_MT','Supply_Received_MT','Supply_Deficit_Percent',
           'Avg_Cylinder_Price_INR','Households_Affected_Percent','Black_Market_Index','Crisis_Severity']]
print("\nSelected Columns")
print(df)
today = df[df['Year'] == 2026]

print("\n2026 LPG Crisis Data")
print(today)
plt.figure(figsize=(16,6))

sns.barplot(
    x='State',
    y='Supply_Deficit_Percent',
    data=today,
    hue="State"
)

plt.xticks(rotation=90)
plt.title("India LPG Crisis 2026 - Supply Deficit by State")
plt.show()

plt.figure(figsize=(16,6))
sns.barplot(
    x='State',
    y='Households_Affected_Percent',
    data=today,
    hue="State"
)
plt.tight_layout()
plt.show()