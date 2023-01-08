import urllib.request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from sqlalchemy import create_engine
import sys
import urllib

def spotify_capstone():
    spotify_client_id = "<client_id>"
    spotify_client_secret = "<client_secret>"
    spotify_redirect_url = "http://localhost:8080"

    #Recently Played
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                   client_secret=spotify_client_secret,
                                                   redirect_uri=spotify_redirect_url,
                                                   scope="user-read-recently-played user-top-read user-read-playback-state user-read-private user-follow-read"))
    recently_played = sp.current_user_recently_played(limit=50)
    user_top_artist = sp.current_user_top_artists(limit=20)
    devices = sp.devices()
    device_list = []
    for row in devices['devices']:
        device_id = row['id']
        device_name = row['name']
        device_type = row['type']
        device_element = {'Device_ID': device_id, 'Device_Name': device_name,
                         'Device_Type': device_type}
        device_list.append(device_element)

    #User_personal_Information
    user_details = sp.me()
    print("********",user_details)
    all_user_details = []
    user_details_list = []
    user_details_list.append(user_details['id'])
    user_details_list.append(user_details['display_name'])
    user_details_list.append(user_details['country'])
    user_details_list.append(user_details['product'])
    all_user_details.append(user_details_list)


    if len(recently_played) ==0:
        sys.exit("No results recieved from Spotify")

    # Creating the Album Data Structure: Album List
    album_list = []
    for row in recently_played['items']:
        album_id = row['track']['album']['id']
        album_track_name = row['track']['name']
        album_name = row['track']['album']['name']
        album_total_tracks = row['track']['album']['total_tracks']
        album_element = {'album_id': album_id, 'name': album_name,
                         'total_tracks': album_total_tracks,'track_name':album_track_name}
        album_list.append(album_element)

    # Details of Top Artist
    top_artist = []

    for row in user_top_artist['items']:
        top_artist_name = row['name']
        uri = row['uri']
        top_artist.append((top_artist_name, uri))
    top_artist = [list(x) for x in top_artist]
    print(top_artist)

    image_list = []

    for i in top_artist:
        results = sp.search(q='artist:' + i[0], type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            image_list.append(artist['images'][1]['url'])
    print(image_list)

    # Details of Top Playlist
    playlists = sp.current_user_playlists(limit=50, offset=0)
    playlist = []
    for row in playlists['items']:
        playlist_name = row['name']
        # different_artists = row['artists']
        playlist.append(playlist_name)
    print("--------xoxoxo----------",playlist)

    # User Followed Artist
    followed_artist_data = []
    following_artists = sp.current_user_followed_artists(10)
    for row in following_artists['artists']['items']:
        followed_artist_data.append((row['name'], row['popularity'], row['followers']['total']))

    print(followed_artist_data)

    user_top_tracks = sp.current_user_top_tracks(25, time_range='long_term')

    top_tracks_user25 = []
    for row in user_top_tracks['items']:
        top_tracks_user25.append((row['album']['name'], row['name'], row['popularity']))

    # Artist Top Tracks
    top_tracks = {}
    for i in top_artist:
        artists_top_tracks_data = sp.artist_top_tracks(i[1].split(':')[2])
        for j in artists_top_tracks_data['tracks']:
            if i[0] in top_tracks:
                top_tracks[i[0]].append(j['name'])
            else:
                top_tracks[i[0]] = [j['name']]

    print("***************",top_tracks)

    # Structuring Data with Pandas Data Frame
    # Recently Played Dataframe
    album_df = pd.DataFrame.from_dict(album_list)
    album_df = album_df.drop_duplicates(subset=['album_id'])
    album_df['ID'] = user_details['id']
    print(album_df)

    # User_table Details
    column_names = ["ID","User_Name","Country","Account_type"]
    user_details_df = pd.DataFrame(all_user_details,columns=column_names)
    print(user_details_df)

    # Artist_Personal_Details
    column_values = ["Artist_name","Popularity","Followers"]
    artist_details_df = pd.DataFrame(followed_artist_data,columns=column_values)
    print(artist_details_df)

    # User Top Artist
    top_artist_column = ["Artist_name","spotify_URI"]
    top_artist_df = pd.DataFrame(top_artist,columns=top_artist_column)
    top_artist_df["ID"] = user_details['id']
    top_artist_df["Image_URL"] = image_list
    print(top_artist_df)

    #User PlayList
    user_playlist_column = ["User_playlists"]
    user_playlist_df = pd.DataFrame(playlist,columns=user_playlist_column)
    user_playlist_df["ID"] = user_details['id']
    print(user_playlist_df)

    #Device Details
    devices_df = pd.DataFrame(device_list)
    devices_df["ID"] = user_details['id']
    print(devices_df)

    #Top artists Albums
    top_tracks_df = pd.DataFrame(top_tracks)
    top_tracks_df = top_tracks_df.T
    top_tracks_df = top_tracks_df[0:]
    top_tracks_df.columns = ['Song_1','Song_2','Song_3','Song_4','Song_5','Song_6','Song_7','Song_8','Song_9','Song_10']
    top_tracks_df = top_tracks_df.rename_axis('Artist_name').reset_index()
    print(top_tracks_df)

    #User Top Tracks
    top_tracks_user25_cols = ["Album_Name", "Track_Name",'Popularity']
    top_tracks_user25_df = pd.DataFrame(top_tracks_user25,columns=top_tracks_user25_cols)
    top_tracks_user25_df['ID'] = user_details['id']
    print(top_tracks_user25_df)

    quoted = urllib.parse.quote_plus(
        "DRIVER={SQL Server};SERVER=<yourservername>;DATABASE=<yourdatabasename>;Trusted_Connection=yes")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

    # user top artists sql table
    sql_functions.user_top_artist(top_artist_df,engine)
    # recently played sql table
    sql_functions.recently_played(album_df, engine)
    # user details sql table
    sql_functions.user_details(user_details_df,engine)
    # artist details sql table
    sql_functions.artist_details(artist_details_df,engine)
    # user playlist sql table
    sql_functions.user_playlist(user_playlist_df,engine)
    # devices sql table
    sql_functions.devices(devices_df,engine)
    # artist top tracks sql table
    sql_functions.artist_top_tracks(top_tracks_df,engine)
    # user top tracks sql table
    sql_functions.user_top_tracks(top_tracks_user25_df,engine)


    return album_list

print(spotify_capstone())