import networkx as nx
import csv
import pandas as pd
import matplotlib.pyplot as plt
import math

width = 6400
height = 4800

id = "Cab Calloway"
filename = r"C:\Users\fbl71\PycharmProjects\ICM_2021_Problem_D\2021_ICM_Problem_D_Data\influence_data.csv"
csv_data = pd.read_csv(filename)
csv_df = pd.DataFrame(csv_data)
G = nx.DiGraph()
for i in range(len(csv_df)):
    head = csv_df["influencer_name"][i]
    tail = csv_df["follower_name"][i]
    G.add_edge(head, tail)
sub = [id]
second = []
third = []
for node in G.successors(id):
    sub.append(node)
    second.append(node)
    # for subnode in G.successors(node):
    #     sub.append(subnode)
    #     third.append(subnode)

subGraph = G.subgraph(sub)
second=list(set(second))
third=list(set(third))
print(len(subGraph),len(sub))
color = []
size = []
edge = []
postion = {}
nodes=[]
edges=[]
print(id in subGraph.nodes)
seconds=[]
thirds=[]
for n in subGraph.nodes:
    if n == id:
        color.append("#b11910")
        size.append(300)
    elif n in second:
        color.append("#8f8fff")
        size.append(50)
        seconds.append(n)
    else:
        color.append("#EE1289")
        size.append(30)
        thirds.append(n)
for e in subGraph.edges:
    edges.append(e)
    if id in e:
        edge.append("#b11910")
    elif e[0] in second or e[1] in second:
        edge.append("#8f8fff")
    else:
        edge.append("#A9A9A9")
center = (width / 2, height / 2)
postion[id] = center
r = 1000
len_second = len(seconds)
len_third = len(thirds)
print(len_second,len_third, len(subGraph.nodes))
for i in range(len_second):
    postion[seconds[i]] = (center[0] + math.cos(i / len_second * 2 * 3.14) * r,
                          center[1] + math.sin(i / len_second * 2 * 3.14) * r)
for i in range(len_third):
    postion[thirds[i]] = (center[0] + math.cos(i / len_third * 2 * 3.14) * 2*r,
                         center[1] + math.sin(i / len_third * 2 * 3.14) * 2*r)
nx.draw(subGraph, node_color=color, node_size=size, edge_color=edge, pos=postion)
plt.savefig('subsub.png', dpi=1000)
