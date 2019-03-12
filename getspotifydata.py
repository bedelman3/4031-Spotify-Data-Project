# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:23:09 2019

@author: Brice
"""

import pandas as pd
import spotipy
import spotipy.oauth2


c_id = "id_here"
c_secret = "secret_here"

songdf = pd.read_csv("regional-us-weekly-latest.csv",header=0)





credentials = spotipy.oauth2.SpotifyClientCredentials(client_id = c_id,client_secret = c_secret)
spotify = spotipy.Spotify(client_credentials_manager = credentials)


features_dict = spotify.audio_features(['4uLU6hMCjMI75M1A2tKUQC'])[0]



features_df = pd.DataFrame()
i=0
while i<4:

    id_df = songdf.iloc[50*i:50*(i+1),5:6]
    
    id_list_list = id_df.values.tolist()
    
    id_list = [x[0] for x in id_list_list]
    
    features_list = spotify.audio_features(id_list)
    
    features_df = features_df.append(pd.DataFrame(features_list))
    
    i = i + 1
    
full_df = pd.merge(songdf,features_df.reset_index(),left_index=True,right_index=True)

full_df.to_csv("song_data.csv")