import pandas as pd

def user_top_artist(top_artist_df,engine):
    top_artist_df.to_sql('user_top_artist', schema='dbo', con=engine, if_exists='replace', index=False)
    top_artist_data = pd.read_sql('select * from dbo.user_top_artist', engine)
    print(top_artist_data)

def recently_played(album_df,engine):
    album_df.to_sql('recently_played', schema='dbo', con=engine,if_exists='replace', index=False)
    album_df = pd.read_sql('select * from dbo.recently_played', engine)
    print(album_df)

def user_details(user_details_df,engine):
    user_details_df.to_sql('user_details', schema='dbo', con=engine,if_exists='replace', index=False)
    user_details_df = pd.read_sql('select * from dbo.user_details', engine)
    print(user_details_df)

def artist_details(artist_details_df,engine):
    artist_details_df.to_sql('artist_details', schema='dbo', con=engine,if_exists='replace', index=False)
    artist_details_df = pd.read_sql('select * from dbo.artist_details', engine)
    print(artist_details_df)

def user_playlist(user_playlist_df,engine):
    user_playlist_df.to_sql('user_playlist', schema='dbo', con=engine,if_exists='replace', index=False)
    user_playlist_df = pd.read_sql('select * from dbo.user_playlist', engine)
    print(user_playlist_df)

def devices(devices_df,engine):
    devices_df.to_sql('devices', schema='dbo', con=engine,if_exists='replace', index=False)
    devices_df = pd.read_sql('select * from dbo.devices', engine)
    print(devices_df)

def artist_top_tracks(top_tracks_dataframe,engine):
    top_tracks_dataframe.to_sql('artist_top_tracks', schema='dbo', con=engine,if_exists='replace', index=False)
    top_tracks_dataframe = pd.read_sql('select * from dbo.artist_top_tracks', engine)
    print(top_tracks_dataframe)

def user_top_tracks(top_tracks_user25_df,engine):
    top_tracks_user25_df.to_sql('user_top_tracks', schema='dbo', con=engine,if_exists='replace', index=False)
    top_tracks_user25_df = pd.read_sql('select * from dbo.user_top_tracks', engine)
    print(top_tracks_user25_df)