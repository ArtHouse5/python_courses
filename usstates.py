import pandas as pd
import numpy as np

pop = pd.read_csv('data/state-population.csv')
areas = pd.read_csv('data/state-areas.csv')
abbrevs = pd.read_csv('data/state-abbrevs.csv')

print(pop.head())
print('###############################')
print(areas.head())
print('###############################')
print(abbrevs.head())

merged = pd.merge(pop, abbrevs, how = 'outer',
                 left_on = 'state/region',
                 right_on = 'abbreviation')
merged = merged.drop('abbreviation', 1)
print('After the merge: ')
print(merged.head())

#checking for NaN

print('Checking null values :', merged.isnull().any())

merged[merged['population'].isnull()].head()
merged.loc[merged['state'].isnull(), 'state/region'].unique()

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()#no more nulls in the state column

final = pd.merge(merged, areas, on='state', how='left')
print('Final merge')
print(final.head())

final['state'][final['area (sq. mi)'].isnull()].unique()
final.dropna(inplace=True)

data2010 = final.query("year == 2010 & ages == 'total'")
data2010.head()

data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']

print('density estimation')
density.sort_values(ascending=False, inplace=True)
print(density.head(),'...', density.tail())
