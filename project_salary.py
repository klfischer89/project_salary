import numpy as np
import pandas as pd
import seaborn as sns

def convert_to_float(s):
    try:
        return np.float(s)
    except ValueError:
        return np.nan

df = pd.read_csv("./data/Salaries.csv.bz2", 
                 converters = {'BasePay': convert_to_float,
                              'OvertimePay': convert_to_float,
                              'OtherPay': convert_to_float,
                              'Benefits': convert_to_float},
                 dtype = {'Status': str})

df.head()