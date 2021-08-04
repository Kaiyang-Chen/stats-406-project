import pandas as pd
import numpy as np

def simi(x,y):
    return 1/(np.sqrt(np.sum((x - y) ** 2))+0.01)

artists_df=pd.read_csv("../step3/std/artists.csv")
influence_df=pd.read_csv("../2021_ICM_Problem_D_Data_std/influence_data.csv")
ranks_df=pd.read_csv("influence_page_rank_0.5_0.csv")

influencer_list=influence_df.influencer_id.unique()
high=ranks_df.id.to_list()[:int(ranks_df.__len__()/2)]

artists_features={}
for _,row in artists_df.iterrows():
    artists_features[row[2]]=row[3:-2]

SS_df=pd.DataFrame(0,columns=["SS","influential"],index=influencer_list)

for _,row in influence_df.iterrows():
    influencer=row.influencer_id
    follower=row.follower_id
    if influencer in artists_features.keys() and follower in artists_features.keys():
        SS_df.loc[influencer,"SS"]+=simi(artists_features[influencer],artists_features[follower])
        if influencer in high:
            SS_df.loc[influencer, "influential"] = "high"
        else:
            SS_df.loc[influencer, "influential"] = "low"

SS_df.to_csv("SS.csv")
