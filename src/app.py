import os
import spotipy
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# get the environment variables
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

from spotipy.oauth2 import SpotifyClientCredentials

robbie_uri = 'spotify:artist:2HcwFjNelS49kFbfvMxQYw'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()) # we can also add client_id and client_secret as parameters

# get the artist's top tracks, its duration and popularity and store it in a dataframe 
results = spotify.artist_top_tracks(robbie_uri)
tracks = results['tracks']
df = pd.DataFrame(tracks)
df = df[['name', 'duration_ms', 'popularity']]
df['duration_ms'] = df['duration_ms'] / 60000
df = df.rename(columns={'name': 'track_name', 'duration_ms': 'duration_min', 'popularity': 'popularity_score'})
print(df)

# plot the results 
import seaborn as sns

# plot the popularity score and duration of the tracks i a scatter plot
sns.scatterplot(data=df, x='popularity_score', y='duration_min')
sns.set_theme(rc={'figure.figsize':(7, 4)})
sns.set_style("whitegrid") # to have a white grid on the background
sns.despine() # to remove the top and right spines