import spotipy
import csv
from spotipy.oauth2 import SpotifyClientCredentials
import json



spotify_client_id=input("enter the client id: ")
spotify_client_secret=input("enter the client secret id: ")



auth_manager=SpotifyClientCredentials(spotify_client_id,spotify_client_secret)

sp=spotipy.Spotify(auth_manager=auth_manager)

playlist_url=input("Enter the playlist url: ")
playlist_data=sp.playlist(playlist_url)
number_of_songs = playlist_data["tracks"]["total"]
item=playlist_data["name"]
collab=playlist_data["collaborative"]
followers=playlist_data["followers"]["total"]
public_account=playlist_data["public"]
creator_name=playlist_data["owner"]["display_name"]
total_number_of_songs=playlist_data["tracks"]["total"]
    
with open("result.txt",'w',encoding='utf-8') as output_file:
    output_file.write(f'Playlist Name: {item}\n')
    output_file.write(f'Creator Name: {creator_name}\n')
    output_file.write(f'Number of Followers: {followers}\n')
    output_file.write(f'Total Songs: {total_number_of_songs}\n')
    output_file.write(f'Collaborative: {collab}\n')
    output_file.write(f'Public Account: {public_account}')


offset = 0
limit = 100

csv_file_path = input("Enter the csv file name: ")

with open(csv_file_path, 'w', newline="", encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Added_date', 'Track_name', 'Artists', 'Album_name'])

    while offset < number_of_songs:
        playlist_data = sp.playlist_tracks(playlist_url, offset=offset, limit=limit)

        for item in playlist_data["items"]:
            added_date = item["added_at"]
            track_name = item["track"]["name"]
            artists = ', '.join([artist['name'] for artist in item['track']['artists']])
            album_name = item["track"]["album"]["name"]
            csv_writer.writerow([added_date, track_name, artists, album_name])

        offset += limit

with open("result.txt",'r',encoding='utf-8') as file:
    content=file.read()
    print(content)    
    
    
    print("data is sucessfully loaded into csv file...!")        
            
    
    