import pandas as pd
import numpy as np
import wquantiles
from scipy.stats import trim_mean

filedata = "/Volumes/unity/Pycharm/Projects/practical-statistics-for-data-scientists/data/state.csv"
state = pd.read_csv(filedata)
print("Mean ",state['Population'].mean())
print("Trim mean",trim_mean(state['Population'],0.1))
print("Median",state['Population'].median())
print("Murder mean rate weighted by population",np.average(state['Murder.Rate'], weights=state['Population']))
print("Murder median rate weighted by population",wquantiles.median(state['Murder.Rate'], weights=state['Population']))