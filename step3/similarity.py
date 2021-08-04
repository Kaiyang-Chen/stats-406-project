import pandas as pd
import numpy as np

def simi(x,y):
    return 1/(np.sqrt(np.sum((x - y) ** 2))+0.01)

artists_df=pd.read_csv("std/artists.csv")
influence_df=pd.read_csv("../2021_ICM_Problem_D_Data_std/influence_data.csv")

influence_list=influence_df.influencer_id.append(influence_df.follower_id).unique()


artists_features={}
for _,row in artists_df.iterrows():
    artists_features[row[2]]=row[3:-2]

influence_list=np.intersect1d(np.array(list(artists_features.keys())),influence_list)
similarity_df=pd.DataFrame(index=influence_list,columns=influence_list)
for influencer in influence_list:
    for follower in influence_list:
        similarity_df[influencer][follower]=simi(artists_features[influencer],artists_features[follower])

