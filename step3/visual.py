import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

artist_df=pd.read_csv("artists.csv")
clusters_df=pd.read_csv("clusters.csv")
mcc_random_df = pd.read_csv("mcc_random.csv")
mcc_describe = mcc_random_df.describe()
genre_list = artist_df['genre'].unique()
genre_list.sort()
N_CLUSTERS = len(genre_list)

fig = go.Figure()
fig.add_trace(go.Bar(name="Max Clustering Coefficient", x=genre_list, y=clusters_df["Max Clustering"]))
fig.add_trace(go.Bar(name='Randomized Clustering', x=genre_list, y=mcc_describe.loc['mean'],
                     error_y=dict(type='data', array=[2*mcc_describe.loc['std'][genre] for genre in genre_list])))
fig.update_layout(barmode='group', title={'text': "AB Tested Max Clustering Coefficient", 'x': 0.5,
                             'xanchor': 'center', 'font': {'size': 20}}, yaxis_title="Max Clustering Coefficient")
fig.show()
fig.write_image("permutation_test_MCC.jpg")

sorted_clusters_df = clusters_df.sort_values("Max Clustering", ascending=False)
fig = px.bar(sorted_clusters_df, y="Max Clustering")
fig.update_layout(title={'text': "Max Clustering Coefficient (sorted)", 'x': 0.5,
                             'xanchor': 'center', 'font': {'size': 20}})
fig.show()
fig.write_image("MCC.jpg")