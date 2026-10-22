## Same thing as the notebook, just in a single script

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df_train = pd.read_csv("Wine-3.csv")
df_train.head()

# Number of rows in dataset
len(df_train)

rows = df_train.shape[0]
cols = df_train.shape[1]

print("Rows", rows)
print("Cols", cols)

mean_winter_rain = df_train['WinterRain'].mean()

france_pop_1957 = df_train[df_train['Year'] == 1957]

#plot of price against agst
sns.scatterplot(data = df_train, x='AGST',y='Price')