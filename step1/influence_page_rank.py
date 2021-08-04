import networkx as nx
import csv
import pandas as pd
import matplotlib.pyplot as plt
import random


def pageRank(filename, alpha, sub_count=0, draw=False, max_iter=100000000):
    csv_data = pd.read_csv(filename)
    csv_df = pd.DataFrame(csv_data)
    G = nx.DiGraph()
    nodes=[]
    all={}
    for i in range(len(csv_df)):
        head = str(csv_df["influencer_id"][i]) + "***" + str(csv_df["influencer_name"][i])
        tail = str(csv_df["follower_id"][i]) + "***" + str(csv_df["follower_name"][i])
        G.add_edge(tail, head)
        all[str(csv_df["influencer_id"][i])] = csv_df["influencer_name"][i]
        all[str(csv_df["follower_id"][i])] = csv_df["follower_name"][i]
    keys=list(all.keys())
    values=list(all.values())
    total=range(len(keys))
    sample=random.sample(total, sub_count)
    for i in sample:
        nodes.append(keys[i] + "***" + values[i])
    if sub_count!=0:
        G=G.subgraph(nodes)
    in_degree = dict(G.in_degree)
    out_degree = dict(G.out_degree)
    pr = nx.pagerank(G, alpha=alpha, max_iter=max_iter)
    pr_sort = sorted(pr.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    # print(pr)
    with open("page_rank_result/influence_page_rank_" + str(alpha) + "_" + str(sub_count) + ".csv", 'w', encoding='utf-8',
              newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['id', 'name', 'influence_score', 'rank', 'out_degree', 'in_degree'])
        max_value = max(pr.values())
        i = 0
        color=[]
        scores=[]
        for key, value in pr_sort:
            i += 1
            color.append(i)
            scores.append(value / max_value)
            writer.writerow(
                [int(key.split("***")[0]), key.split("***")[1], value / max_value, i, in_degree[key], out_degree[key]])

    plt.clf()
    plt.scatter(in_degree.values(),scores)
    plt.xlabel("out_degree")
    plt.ylabel("scores")
    plt.savefig("out_degree/out_degree_" + str(alpha) + "_" + str(sub_count) + '.png', dpi=1000)

if __name__ == '__main__':
    filename = r"..\influence_data.csv"
    for i in range(21):
        alpha = round(i * 0.05, 2)
        print(alpha)
        pageRank(filename, alpha)