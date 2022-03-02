#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_csv("data/heights.csv",dtype={"height_in":np.float64})

print(df.head(1))

print(df.dtypes)
# %%
