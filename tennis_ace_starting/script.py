import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv("tennis_stats.csv")
print(df.head())
print(df.info())
print(df.describe())






# perform exploratory analysis here:

plt.scatter(df.BreakPointsOpportunities,df.Winnings)
plt.title('Break Points opportunities vs winnings')
plt.show()
plt.clf()
plt.scatter(df.TotalPointsWon,df.Winnings)
plt.title("Total points won vs winnings")
plt.show()
plt.clf()













## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:
