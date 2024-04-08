import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency


df = pd.read_csv('totality.csv')

df = df[pd.to_numeric(df['age'], errors='coerce').notnull()]
df['age'] = df['age'].astype(int)
print(df['age'].describe())

## age histo
plt.figure(figsize=(10,6))
sns.histplot(df.age)
plt.title('Age Distribution',size=18)
plt.xlabel('Age',size=14)
plt.ylabel('Count',size=14)
plt.show()

## race plot
plt.figure(figsize=(10,6))
sns.countplot(x = 'race', data = df)
plt.title('Total Number by Race',size=18)
plt.xlabel('Race',size=14)
plt.show()

## categorical counts
print(df.race.value_counts())
print(df.cause_of_death.value_counts(100))
print(df.encounter_type.value_counts())

cross_tab_1 = pd.crosstab(df.race, df.encounter_type, margins=True)
cross_tab_1 = cross_tab_1.loc[:, ['Part 1 Violent Crime', 'Person with a Weapon', 'Other Non-Violent Offense', 'Traffic Stop']]
print(cross_tab_1)

chi2, p, dof, expected = chi2_contingency(cross_tab_1)
print("Chi-square statistic:", chi2)
print("P-value:", p)
print("Degrees of freedom:", dof)