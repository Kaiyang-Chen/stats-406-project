import networkx as nx
import csv
import pandas as pd
import matplotlib.pyplot as plt
import math

filename = r"C:\Users\fbl71\PycharmProjects\ICM_2021_Problem_D\2021_ICM_Problem_D_Data\influence_data.csv"
# pagerank =
csv_data = pd.read_csv(filename)
csv_df = pd.DataFrame(csv_data)
G = nx.DiGraph()
for i in range(len(csv_df)):
    head = csv_df["influencer_id"][i]
    tail = csv_df["follower_id"][i]
    G.add_edge(head, tail)

nodes=[785283,404463,781094,97182,936946,932858,488378,105618,138833,496097,692100,771297,573410,652255,556242,797056,891907,310789,143494,236287,477523,828768,1266,742673,67406,493412,95613,615026,259270,695019,887719,56913,804706,636106,16448,61273,166383,781732,852842,109669,828756,132940,104314,6613,159406,1016154,122037,744075,68898,69761,253397,753104,313128,230886,603621,1426748]
subgraph=G.subgraph(nodes)
nx.draw(subgraph,with_labels=True)
plt.savefig("plot.png")
plt.show()
