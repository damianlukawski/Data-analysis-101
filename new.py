import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import functions


pd.set_option( "display.max_columns", None)
pp = pd.read_csv('pokemon.csv') #pp - pokemon pandas
pp['Total']= pp['HP']+pp['Attack']+pp['Defense']+pp['Sp. Atk']+pp['Sp. Def']+pp['Speed']
print(pp.columns)


Group = pp.groupby(['Type 1']).size()

Legendary = pp.loc[pp['Legendary'] == True] #filtering only legendary pokemons
Group_Legendary = Legendary.groupby(['Type 1']).size()

NonLegendary = pp.loc[pp['Legendary'] == False]
Group_NonLegendary = NonLegendary.groupby(['Type 1']).size()

#print(Group_NonLegendary)

Group_mean = pp.groupby(['Type 1']).mean()
#functions.print_ad(Legendary)
functions.print_groupby(Group_mean['Total'], 'bar')