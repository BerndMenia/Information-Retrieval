from os.path import abspath
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA


# import the dataset
path_spotify_data = abspath("../../../resources/playlist_features.csv")
spotify_data = pd.read_csv(path_spotify_data)
print("Input data and Shape: ", spotify_data.shape)

# get the values
playlist = spotify_data["playlist"].values
tempo = spotify_data["tempo"].values
energy = spotify_data["energy"].values
speechiness = spotify_data["speechiness"].values
acousticness = spotify_data["acousticness"].values
danceability = spotify_data["danceability"].values
valence = spotify_data["valence"].values
instrumentalness = spotify_data["instrumentalness"].values
# np array for kmeans and dbscan
X = np.array(list(zip(tempo, energy, speechiness, acousticness, danceability, valence, instrumentalness)))


# build kmeans model
kmeans = KMeans(n_clusters=10)
kmeans = kmeans.fit(X)
labels_kmeans = kmeans.labels_.tolist()
centroids_kmeans = kmeans.cluster_centers_


# build dbscan model
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan = dbscan.fit(X)
labels_dbscan = dbscan.labels_.tolist


# apply PCA to spotify_data to visualize in 2D space
# note: fit fits our spotify data with the pca model and
#       transform then applies the dimensionality reduction to our spotify data
pca = PCA(n_components=2).fit(X)
X2D = pca.transform(X)


# plot clusters
color_labels = ["#FFFF00", "#008000", "#0000FF", "#800080", "#f5b041", "#5dade2", "#f1948a", "#d0d3d4", "#f9e79f", "#e8daef"]

# plot kmeans clusters
color_kmeans = [color_labels[i] for i in labels_kmeans]
plt.scatter(X2D[:,0], X2D[:,1], c=color_kmeans)
centroidpoint_kmeans = pca.transform(centroids_kmeans)
plt.scatter(centroidpoint_kmeans[:, 0], centroidpoint_kmeans[:, 1], marker='^', s=150, c='#000000')
plt.title("K-means")
plt.show()


# plot dbscan clusters
