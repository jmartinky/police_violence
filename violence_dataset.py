import pandas as pd
from icecream import ic

## read officer involved death data
violence = pd.read_excel('data.xlsx')

## read abbreviations with full state names
states = pd.read_csv('states.csv')

## merge officer data with full state names
violence_states = pd.merge(violence, states, on='state', how='left')

## define function to combine county and state name into one column 
def combine_columns(row):
    return str(row['county']) + ' ' + str(row['state_name'])

## call the above function 
violence_states['StateCounty'] = violence_states.apply(combine_columns, axis = 1)

## read crime statistic data
offenses = pd.read_excel('Table_10_Offenses_Known_to_Law_Enforcement_by_State_by_Metropolitan_and_Nonmetropolitan_Counties_2022.xlsx')

## define function to combine county and state in crime statistic data
def combine_2(row):
    return str(row['County']) + ' ' + str(row['State'])

## call the above function
offenses['StateCounty'] = offenses.apply(combine_2, axis = 1)

## merge officer involved death data with crime statistics data
totality = pd.merge(violence_states, offenses, on='StateCounty', how='left')

totality.to_csv('totality.csv', index=False)