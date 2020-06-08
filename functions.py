import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

def print_groupby(grouptype):
    grouptype.plot(kind='bar', color='blue')
    plt.show()

def print_ad(df):
    df.plot(x='Attack', y='Defense', kind='scatter', color='blue')
    plt.show()