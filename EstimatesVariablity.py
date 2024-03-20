import pandas as pd
import statsmodels.api as sm

filedata = "/Volumes/unity/Pycharm/Projects/practical-statistics-for-data-scientists/data/state.csv"
state = pd.read_csv(filedata)
print(state['Population'].std())
print(state['Population'].quantile(0.75))
print(state['Population'].quantile(0.25))
print(sm.robust.mad(state['Population']))
