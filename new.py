import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


plt.close('all')
#x = input("Please provide the filename and path ")
pd.set_option( "display.max_columns", None)
#pokemon_pandas = pd.read_csv('{}'.format(x))
pp = pd.read_csv('pokemon.csv') #pp - pokemon pandas
#pp.set_option("display.max_rows", max_rows, "display.max_columns", max_cols)
#print(pokemon_pandas)
#print(pp.columns)
#print(pp.loc[pp['Type 1'] == "Fire"])

group = pp.groupby(['Type 1']).count()
print(group["#"])

plt.figure()
group["#"].plot(kind='bar', color='green')
plt.show()