
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

url = 'https://github.com/HamoyeHQ/HDSC-Introduction-to-Python-for-machine-learning/files/7768140/FoodBalanceSheets_E_Africa_NOFLAG.csv'

foa_data = pd.read_csv(url, encoding = "ISO-8859-1", engine='python')

foa_data

foa_data.describe(include = 'all')

foa_data['Y2014']

foa_data['Y2015'].describe()

foa_data['Y2016'].isnull().sum()

foa_data.corr()

len(foa_data['Area'].unique())

