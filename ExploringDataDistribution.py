import pandas as pd
import matplotlib.pyplot as plt
filedata = "/Volumes/unity/Pycharm/Projects/practical-statistics-for-data-scientists/data/state.csv"
state = pd.read_csv(filedata)
print(state['Murder.Rate'].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))
ax = (state['Population']/1_000_000).plot.box()
ax.set_xlabel('Population (millons)')
plt.show()
binnedPopulation = pd.cut(state['Population'],10)
binnedPopulation.value_counts()
ax =(state['Population']/1_000_000).plot.hist(figsize=(4, 4))
ax.set_xlabel('Population (millons)')
plt.show()
ax =state['Murder.Rate'].plot.hist(density=True,xlim=[0, 12],bins=range(1, 12))
state['Murder.Rate'].plot.density(ax=ax)
ax.set_xlabel('Murder Rate (per 100,00)')
plt.show()