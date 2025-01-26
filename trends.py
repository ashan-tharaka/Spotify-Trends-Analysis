import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

spotify_data=pd.read_csv('dataset.csv')

print(spotify_data.head())

#1 analyze music trends

top_genres = spotify_data["track_genre"].value_counts().head(10)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="viridis")
plt.title("Top 10 Genres on Spotify")
plt.xlabel("Number of Tracks")
plt.ylabel("Genres")
plt.show()


# Average popularity by artist
#popularity_by_artist = spotify_data.groupby("artists")["popularity"].mean().sort_values(ascending=False)

# Plot
#plt.figure(figsize=(10, 6))
#sns.barplot(x=popularity_by_artist.values, y=popularity_by_artist.index, palette="mako")
#plt.title("Top Artists by average popularity")
#plt.xlabel("Average Popularity")
#plt.ylabel("Artist")
#plt.show()

# Scatter plot for danceability vs energy
plt.figure(figsize=(10, 6))
sns.scatterplot(data=spotify_data, x="danceability", y="energy", hue="track_genre", alpha=0.6, palette="tab10")
plt.title("Danceability vs Energy")
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid()
plt.show()

# Correlation matrix
correlation_matrix = spotify_data[["danceability", "energy", "tempo", "popularity"]].corr()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Audio Features and Popularity")
plt.show()

# Filter for a specific genre
pop_genre_tracks = spotify_data[spotify_data["track_genre"] == "afrobeat"].sort_values(by="popularity", ascending=False).head(10)

print("Top 10 Popular AfroBeat Tracks:")
print(pop_genre_tracks[["track_name", "artists", "popularity"]])

