import pandas as pd
import numpy as np
import matplotlib as plt

violence = pd.read_excel('data.xlsx')
#violence['StateCounty'] = violence[['state', 'county']].agg(','.join, axis=1 )
#print(violence.info())

states = pd.read_csv('states.csv')
#print(states)

violence_states = pd.merge(violence, states, on='state', how='left')
print(violence_states.head())

#offenses = pd.read_excel('Table_10_Offenses_Known_to_Law_Enforcement_by_State_by_Metropolitan_and_Nonmetropolitan_Counties_2022.xlsx')
#offenses['StateCounty'] = offenses[['State', 'County']].agg(','.join, axis=1)
#print(offenses.head())

