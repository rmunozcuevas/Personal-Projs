from pip._vendor import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials





# Set up the credentials
CLIENT_ID = 'EDITED FOR PRIVACY'  # Replace with your actual client ID
CLIENT_SECRET = 'EDITED FOR PRIVACY'  # Replace with your actual client secret
REDIRECT_URI = 'http://localhost:8888/callback'
#----------------------------------------------------
import os

#----------------------------------------------------
SCOPE = 'playlist-modify-private'
user = 'FitGoesHard'

#----------------------------------------------------

# Authenticate using client credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri = REDIRECT_URI, scope = SCOPE))

user = sp.current_user()['id']
#-------------------------------------------------------------------------


while True:
    user_request = input("Would you like to create and name a playlist? (y or n)")
    if(user_request == "y"):
        playlist_n = input("What name would you want your playlist to be: \n")
        playlist_d = input("Enter in a playlist description: \n")

        playlist =sp.user_playlist_create(user=user, name = playlist_n, public = False, description = playlist_d)
        p_id = playlist['id']
        
        print(f"Playlist {playlist_n} created succesfully...")
        while True:
            user_conf = input("would you like to add songs to the playlist?(Y or N)").strip().lower()
            if(user_conf == "y"):
                while True:
                    user_add = input("type the song you want add:(exit to stop)").strip()
                    if user_add == "exit":
                        print("exiting the song addition process.")
                        break


                    try:
                        result = sp.search(q = user_add, limit = 5, type = 'track')
                        if not result['tracks']['items']:
                            print(f"No songs for {user_add} found, try again")
                            continue

                        print(f"Found the following songs for '{user_add}':")
                        for i, track in enumerate(result['tracks']['items']):
                             print(f"{i + 1}. {track['name']} by {track['artists'][0]['name']}")
                            
                        song_choice = input("Enter the number of the song that you want: (or exit to stop)").strip()

                        if song_choice == "exit":
                            print("exiting number that you wanted")
                            break
                        try:
                            song_choice = int(song_choice) - 1
                            if song_choice < 0 or song_choice >= len(result['tracks']['items']):
                                print("Invalid Choice, try again")
                                continue
                            track_uri = result['tracks']['items'][song_choice]['uri']  # Get the URI of the first result
                            sp.user_playlist_add_tracks(user=user, playlist_id=p_id, tracks=[track_uri])
                            print(f"Song '{result['tracks']['items'][song_choice]['name']}' has been added to the playlist!")
                        except ValueError:
                            print("Invalid input, enter in a valid number:")

                    except Exception as e:
                        print(f"error adding song '{user_add}' : {e}")
                        continue

            elif user_conf == "n":
                print("Understand, songs will not be added to the playlist...")
                break

            else:
                print("Invalid input. Please enter 'Y' to add songs or 'N' to stop.")

    elif(user_request == "n"):
        print("No user playlist will be created. ")
        break
    else:
        print("Ermmmm that must have been an error")
        break



## currently just querying public data that the api allows me to access
print("*---------------------------------------------------------------*")
q = input("What Artist do you want to search up for their most listened to songs:")
results = sp.search(q=q, limit=10)

# for idx, track in enumerate(results['tracks']['items']):
# Print out the the public data track names

print("*---------------------------------------------------------------*")
for idx, track in enumerate(results['tracks']['items']):
    print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")
print("*---------------------------------------------------------------*")


lana = 'https://open.spotify.com/artist/00FQb4jTyendYWaN8pK0wa?si=qRS3Cy5JSf6GtbVdbQaT7A'


# https://spotipy.readthedocs.io/en/2.24.0/
# List of features I want to add
# - Ability to search up an artist from input
# - ability to create a playlist and add songs to it
