import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x_label = ["danceability","energy","valence","tempo","loudness","mode","key","acousticness","instrumental","liveness","speechiness","explicit"]

data = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.34,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0.34,0,0,0,0,0.002,0.928,0,0.002],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.002,0,0,0,0,0],[0,0,0,0,0,0,0.928,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.002,0,0,0,0,0]])
ax = sns.heatmap(data, linewidth=0.5, annot=True, cmap="YlGnBu", xticklabels=x_label, yticklabels=x_label)
ax.set_title('2-tailed p-value for dependence of features')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize = 6)
ax.set_yticklabels(ax.get_yticklabels(), fontsize = 6)
#plt.setp(ax.get_xticklabels() , rotation = 90)
plt.savefig("./dependencePvalue.png")