import numpy as np
import pandas as pd

sug = pd.read_csv("sug_users_vids_all.csv")

just_users = sug[['user_name', 'n_followers', 'n_total_likes', 'n_total_vids']].drop_duplicates('user_name')
by_user = {}
for i in just_users['user_name']:
    by_user[i] = sug[sug['user_name'] == i][1:].reset_index(drop = True)

sug_df = pd.concat([by_user[i] for i in by_user]).reset_index(drop = True)
def hashtoarray(x):
    hash_array = []
    for i in range(41677):

        tags_list = x.iloc[i]['hashtags'].replace("'", "").strip('][').split(', ')
        for tag in tags_list:
            row = [x.iloc[i]['id'], tag, x.iloc[i]['video_length'], x.iloc[i]['n_likes'], x.iloc[i]['n_shares'], x.iloc[i]['n_comments'], x.iloc[i]['n_plays'], x.iloc[i]['n_followers'], x.iloc[i]['n_total_likes']]
            hash_array.append(row)
        
    return hash_array

newtags = hashtoarray(sug)
pd.DataFrame(newtags).to_csv('hashtag.csv', header  = ['id','hashtag','video_length', 'n_likes', 'n_shares', 'n_comments', 'n_plays', 'n_followers', 'n_total_likes']) 