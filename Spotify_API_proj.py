# import requests: usually requests is used to make http requests however the spotify API handles that for me
# spotipy is the main library that I used to interact with the spotify api
# SpotifyOAuth is a way of authenticating credentials, good when trying to access private user data
# SpotifyClientCredentials: originally used to access public artist data, but i swithced it up in order to acess more private data

from pip._vendor import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials





# Set up the credentials
CLIENT_ID = 'EDITED FOR PRIVACY'  # identifies my app to the spotify api
CLIENT_SECRET = 'EDITED FOR PRIVACY'  # used to authenticate that it is in fact me trying to make requests to the api
REDIRECT_URI = 'http://localhost:8888/callback' # Oauth feedback: where I will be redirected after trying to authenticate
#----------------------------------------------------
import os

#----------------------------------------------------
# Determines the permissions the potential playlist will have, right now I wanted it to make private playlists at the moment
# My user which has been redacted
SCOPE = 'playlist-modify-private'
user = '###########'

#----------------------------------------------------

# Authenticate using client credentials
# sp is used to authenticate credentials using: client_id, client_secret, redirect_uri, and scope
# sp is an instance of the spotipy.Spotify class, object allows you to interact with the spotify api
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri = REDIRECT_URI, scope = SCOPE))
# current_user() - method provided by spotipy library, sends a request to the spotify API, on current authenticated user and returns a
# dictionary containing details on the user(such as ID,name, email, followers, country
# id part retreives the user's id and stored in user
user = sp.current_user()['id']
#-------------------------------------------------------------------------

# While True is the main loop that asks if you want to create a playlist if yes, then you will be prompted to create a name and description
# for the newly created playlist and then these details will be stored in variable playlist which will user an instance of sp and the 
# user_playlist_create function in order to create the function which has 4 parameters(user,name, public/private,description
while True:
    user_request = input("Would you like to create and name a playlist? (y or n)")
    if(user_request == "y"):
        playlist_n = input("What name would you want your playlist to be: \n")
        playlist_d = input("Enter in a playlist description: \n")

        playlist =sp.user_playlist_create(user=user, name = playlist_n, public = False, description = playlist_d)
        p_id = playlist['id'] # p_id stored the playlists id for the future, in order to add songs to it
        
        print(f"Playlist {playlist_n} created succesfully...") ## print statement to let you know that a playlist has been added succesfully
        while True: ## while true loop in order to further continue in whether you would like to add songs or not
            user_conf = input("would you like to add songs to the playlist?(Y or N)").strip().lower() # 
            if(user_conf == "y"):
                while True:
                    user_add = input("type the song you want add:(exit to stop)").strip() # user asked to enter in a song name
                    if user_add == "exit": # if exit then this while true loop stops and goes to user_conf loop
                        print("exiting the song addition process.")
                        break


                    try: # try block first wants to try the search function using authenticated credentials(sp)
                        result = sp.search(q = user_add, limit = 5, type = 'track') # limit of 5 tracks to choose from
                        if not result['tracks']['items']: # if no tracks found then print statement will happen and user will be asked to try again
                            print(f"No songs for {user_add} found, try again") # print statement to confirm that no songs found
                            continue

                        print(f"Found the following songs for '{user_add}':") # if songs found then this will print
                        for i, track in enumerate(result['tracks']['items']):
                             print(f"{i + 1}. {track['name']} by {track['artists'][0]['name']}")
                            
                        song_choice = input("Enter the number of the song that you want: (or exit to stop)").strip()

                        if song_choice == "exit":
                            print("exiting number that you wanted")
                            break
                        try:
                            song_choice = int(song_choice) - 1 # lists in python 0 indexed, therefore if i type in 3 im really asking for position 4
                            if song_choice < 0 or song_choice >= len(result['tracks']['items']): # cant enter a number less than zero while also checking the length of list tracks
                                print("Invalid Choice, try again")
                                continue
                            track_uri = result['tracks']['items'][song_choice]['uri']  # Get the URI of the first result
                            sp.user_playlist_add_tracks(user=user, playlist_id=p_id, tracks=[track_uri])# uses the user_playlist_add_tracks in order to add tracks needs authentication
                            print(f"Song '{result['tracks']['items'][song_choice]['name']}' has been added to the playlist!") # confirmation
                        except ValueError:
                            print("Invalid input, enter in a valid number:") #Exception handling

                    except Exception as e:
                        print(f"error adding song '{user_add}' : {e}") #exception handling
                        continue

            elif user_conf == "n":
                print("Understand, songs will not be added to the playlist...") # if you choose not to add songs to playlist
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

# This line of code never went anywhere really
lana = 'https://open.spotify.com/artist/00FQb4jTyendYWaN8pK0wa?si=qRS3Cy5JSf6GtbVdbQaT7A'


# https://spotipy.readthedocs.io/en/2.24.0/
# List of features I want to add 
# - Ability to search up an artist from input (Done)
# - ability to create a playlist and add songs to it (Done)



# FOR LINES 70 - 71:
# for API class, this is a nested dictionary and the "artists" key is another dictionary which has a list as a value
# "tracks" is a key, "items" is the value of that key which "items" itself is a key to a list containing another key/value, which in it of itself contains another key/value pairing
# {
    #"tracks": {
        #"items": [
            #{"name": "Song 1", "artists": [{"name": "Artist 1"}]},
            #{"name": "Song 2", "artists": [{"name": "Artist 2"}]},
            #{"name": "Song 3", "artists": [{"name": "Artist 3"}]},
            # More tracks...
        #]
    #}
#}

#
