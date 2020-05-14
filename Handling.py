# Just with the uk right now

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt#


df = pd.read_csv('Hospitalization_all_locs.csv')
is_UK = df['location_name'] == 'United Kingdom'
df = df[is_UK]
df = df.iloc[:, [1, 2, 12]]
df.set_index('date')

fig, ax = plt.subplots()
ax.plot(df.iloc[:, 1], df.iloc[:, 2])
plt.show()

print('\nDone')
