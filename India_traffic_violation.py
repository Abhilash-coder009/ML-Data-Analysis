import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("datasets/Indian_Traffic_Violations.csv")
print(data)
x = data.head()
print(x)
y = data.tail()
print(y)
df = data[['Violation_Type', 'Fine_Amount', 'Location','Registration_State', 'License_Type']]
df.columns = ['Viol', 'Fine', 'Loc', 'St', 'Lic']
print(df)

state = df.groupby('St').size().reset_index(name='Total_Violations')
print(state)

plt.figure(figsize=(12,6))
sns.barplot(x='St', y='Total_Violations', data=state, hue='St')
plt.title("State-wise Traffic Violations")
plt.tight_layout()
plt.show()

reason = df.groupby(['St', 'Viol']).size().reset_index(name='Total')
print(reason)
plt.figure(figsize=(14,6))
sns.barplot(x='St', y='Total', hue='Viol', data=reason)
plt.title("State-wise Violation Reasons")
plt.legend(title="Violation Type",bbox_to_anchor=(1.02, 1),loc='upper left')

plt.tight_layout()
plt.show()