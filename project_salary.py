import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def convert_to_float(s): # method for converting to float64 , if not possible make it NaN
    try:
        return np.float64(s)
    except ValueError:
        return np.nan

df = pd.read_csv("./data/Salaries.csv.bz2", 
                 converters = {'BasePay': convert_to_float,
                              'OvertimePay': convert_to_float,
                              'OtherPay': convert_to_float,
                              'Benefits': convert_to_float},
                 dtype = {'Status': str})

print(df.head())
sns.set_theme()
# visualize income distribution for 2014
base_pay_2014_max = df.loc[df["Year"] == 2014, "BasePay"].max() # get max basepay for 2014
print(base_pay_2014_max)
sns.histplot(data = df[df["Year"] == 2014], x = "BasePay", binwidth = 10000, binrange = (0, base_pay_2014_max)) # create hitogram for basepay in 2014
# plt.show()

df_2014 = df[df["Year"] == 2014]
df_jobs = df_2014\
    .groupby("JobTitle")\
    .agg(count = ("Id", len), avgPay = ("TotalPayBenefits", "mean"))\
    .sort_values("count", ascending = False)\
    .iloc[:10]
df_jobs.head()

ax = sns.barplot(x = df_jobs.index, y = df_jobs["avgPay"])
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='small'  
)
# plt.show()

df_grouped = df.groupby("Year").agg(avgP = ("TotalPayBenefits", "mean"))

sns.barplot(x = df_grouped.index, y = df_grouped["avgP"])
# plt.show()

df_grouped = df\
    .groupby("Year")\
    .agg(avgPay = ("TotalPayBenefits", "mean"), avgBasePay = ("BasePay", "mean"))\
    .reset_index()\
    .melt(id_vars = ["Year"])

sns.barplot(x = df_grouped["Year"], 
            y = df_grouped["value"], 
            hue = df_grouped["variable"], 
            hue_order = ["avgBasePay", "avgPay"])
# plt.show()