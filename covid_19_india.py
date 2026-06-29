import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("datasets/covid_19_india.csv")

print("Complete Dataset")
print(data)

x = data.head()
print("\nFirst 5 Records")
print(x)

y = data.tail()
print("\nLast 5 Records")
print(y)
df = data[['Date', 'Time', 'State/UnionTerritory', 'Cured', 'Deaths', 'Confirmed']]

df.columns = ['Dt', 'Ti', 'St', 'Cure', 'Death', 'Conf']

print("\nSelected Columns")
print(df.head())
today = df[df['Dt'] == '2020-07-14']

print("\nCOVID Data on 14-07-2020")
print(today)

confirmed = today.sort_values(by='Conf', ascending=False)
top10_confirmed = confirmed[:10]
print("\nTop 10 States by Confirmed Cases")
print(top10_confirmed)
plt.figure(figsize=(12,6))
sns.barplot(
    x='St',
    y='Conf',
    data=top10_confirmed,
    hue='St',
    legend=False
)

plt.title("Top 10 States by Confirmed COVID-19 Cases (14-07-2020)")
plt.tight_layout()
plt.show()

cured = today.sort_values(by='Cure', ascending=False)
top10_cured = cured[:10]
print("\nTop 10 States by Recovered Cases")
print(top10_cured)
plt.figure(figsize=(12,6))
sns.barplot(
    x='St',
    y='Cure',
    data=top10_cured,
    hue='St',
    legend=False
)
plt.title("Top 10 States by Recovered COVID-19 Cases (14-07-2020)")
plt.tight_layout()
plt.show()