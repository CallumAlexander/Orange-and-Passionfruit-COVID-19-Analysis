# Just with the uk right now

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  #

csv = 'Hospitalization_all_locs.csv'


def handle(csv):
    df = pd.read_csv(csv)
    is_UK = df['location_name'] == 'United Kingdom'
    df = df[is_UK]
    df = df.iloc[:, [2, 12]]
    df.set_index('date')
    return df


def display(df):
    fig, ax = plt.subplots()
    ax.plot(df.iloc[:, 0], df.iloc[:, 1])
    ax.grid()
    plt.show()


if __name__ == '__main__':
    df = handle(csv)
    display(df)

    print('\nDone')
