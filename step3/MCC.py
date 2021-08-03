import numpy as np
import pandas as pd
import random
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import plotly.graph_objects as go
import plotly.express as px


LOOK_AT = 10
SEED = 42
np.random.seed(SEED)
random.seed(SEED)


data_by_artist = pd.read_csv("../2021_ICM_Problem_D_Data/data_by_artist.csv")
influence_data = pd.read_csv("../2021_ICM_Problem_D_Data/influence_data.csv")
features_list = data_by_artist.columns[2:]

# creating dict
id_genre_dict = {}

for i in range(len(influence_data)):
    row = influence_data.loc[i]
    in_id = row['influencer_name']
    fol_id = row['follower_name']
    in_genre = row['influencer_main_genre']
    fol_genre = row['follower_main_genre']
    if in_id not in id_genre_dict:
        id_genre_dict[in_id] = set()
    id_genre_dict[in_id].add(in_genre)

    if fol_id not in id_genre_dict:
        id_genre_dict[fol_id] = set()
    id_genre_dict[fol_id].add(fol_genre)

# generate artist_df
artist_df = pd.DataFrame()
artists_not_included = []
for i in range(len(data_by_artist)):
    try:
        for genre in id_genre_dict[data_by_artist.loc[i]['artist_name']]:
            if genre == "Unknown" or genre == "Children's":
                continue
            tmp_df = pd.DataFrame(data_by_artist.loc[i]).T
            tmp_df['genre'] = genre
            artist_df = pd.concat((artist_df, tmp_df))
    except:
        artists_not_included.append(data_by_artist.loc[i]['artist_name'])

artist_df = artist_df.reset_index().drop("index", axis=1)

# kmeans
genre_list = artist_df['genre'].unique()
genre_list.sort()
N_CLUSTERS = len(genre_list)

cluster_pipeline = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=N_CLUSTERS, n_init=50, max_iter=1000, random_state=SEED))])
X = artist_df.loc[:, features_list]
cluster_pipeline.fit(X)
artist_df['cluster'] = cluster_pipeline.predict(X)


# MCC
clusters = artist_df.groupby(['genre', 'cluster']).size()
clusters_df = pd.DataFrame()
r = 0
for f in genre_list:
    tmp_cluster = clusters[f]
    tmp_cluster = tmp_cluster.reindex(np.arange(N_CLUSTERS))
    tmp_cluster = tmp_cluster.fillna(0)
    clusters_df[f] = tmp_cluster

clusters_df = clusters_df.T
max_perc = []
for genre in clusters_df.index:
    max_perc.append(max(clusters_df.loc[genre]) / clusters_df.loc[genre].sum(axis=0))

clusters_df["Max Clustering"] = max_perc

# permutation test
def mcc_AB(artist_df, N_CLUSTERS):
    random_df = artist_df.copy()
    np.random.shuffle(random_df['genre'].to_numpy())

    cluster_pipeline = Pipeline([('scaler', StandardScaler()), (
    'kmeans', KMeans(n_clusters=N_CLUSTERS, n_init=50, max_iter=1000, random_state=SEED))])
    X = random_df.loc[:, features_list]
    cluster_pipeline.fit(X)
    random_df['cluster'] = cluster_pipeline.predict(X)

    r_clusters = random_df.groupby(['genre', 'cluster']).size()
    r_clusters_df = pd.DataFrame()
    r = 0
    for f in genre_list:
        tmp_cluster = r_clusters[f]
        tmp_cluster = tmp_cluster.reindex(np.arange(N_CLUSTERS))
        tmp_cluster = tmp_cluster.fillna(0)
        r_clusters_df[f] = tmp_cluster

    r_clusters_df = r_clusters_df.T
    max_perc = []
    for genre in r_clusters_df.index:
        max_perc.append(max(r_clusters_df.loc[genre]) / r_clusters_df.loc[genre].sum(axis=0))

    r_clusters_df["Max Clustering"] = max_perc
    return r_clusters_df["Max Clustering"]


mcc_random_df = pd.DataFrame()
AB_ITERATIONS = 50
for i in range(AB_ITERATIONS):
    mcc_series = mcc_AB(artist_df, N_CLUSTERS)
    mcc_random_df[f"Iteration {i}"] = mcc_series

mcc_random_df = mcc_random_df.T
mcc_describe = mcc_random_df.describe()

# save results
clusters_df.to_csv("original/clusters.csv")
mcc_describe.to_csv("original/mcc_null.csv")
artist_df.to_csv("original/artists.csv")

# visualization
fig = go.Figure()
fig.add_trace(go.Bar(name="Max Clustering Coefficient", x=genre_list, y=clusters_df["Max Clustering"]))
fig.add_trace(go.Bar(name='Randomized Clustering', x=genre_list, y=mcc_describe.loc['mean'],
                     error_y=dict(type='data', array=[2*mcc_describe.loc['std'][genre] for genre in genre_list])))
fig.update_layout(barmode='group', title={'text': "MCC Permutation Test", 'x': 0.5,
                             'xanchor': 'center', 'font': {'size': 20}}, yaxis_title="Max Clustering Coefficient")
fig.show()
# fig.write_image("permutation_test_MCC.jpg")

sorted_clusters_df = clusters_df.sort_values("Max Clustering", ascending=False)
fig = px.bar(sorted_clusters_df, y="Max Clustering")
fig.update_layout(title={'text': "MCC (sorted)", 'x': 0.5,
                             'xanchor': 'center', 'font': {'size': 20}})
fig.show()
# fig.write_image("MCC.jpg")
