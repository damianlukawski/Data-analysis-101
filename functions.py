import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

def print_groupby(grouptype, plot_type): #plot type among "bar", barh", "pie", etc.
    grouptype.plot(kind=plot_type)
    plt.show()

def print_ad(df):
    df.plot(x='Attack', y='Defense', kind='scatter', color='blue')
    plt.show()