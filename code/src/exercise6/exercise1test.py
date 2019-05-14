# from gensim.models.doc2vec import Doc2Vec
# from code.src.exercise5.kmeans import kmeans

import csv
import matplotlib.pyplot as plt
import numpy as np

from pandas import DataFrame
from sklearn.cluster import KMeans



from sklearn.decomposition import PCA


########## load doc2vec model ##########
# model = Doc2Vec.load("./playlist_features.csv")

########## kmeans ##########
#cluster = kmeans()
#cluster.kmeans_cluster(model.docvecs.doctag_syn0)

# "playlist","tempo","energy","speechiness","acousticness","danceability","valence","instrumentalness"

def string_to_float(arr):
    return [float(x) for x in arr]



tempo = []
energy = []
speechiness = []
acousticness = []
danceability = []
valence = []
instrumentalness = []

with open('./playlist_features.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    # https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
    next(csvReader, None)  # skip the headers

    for row in csvReader:
        tempo.append(row[1])
        energy.append(row[2])
        speechiness.append(row[3])
        acousticness.append(row[4])
        danceability.append(row[5])
        valence.append(row[6])
        instrumentalness.append(row[7])

    tempo = string_to_float(tempo)
    energy = string_to_float(energy)

#df = DataFrame(Data, columns=['playlist', 'tempo', 'energy','speechiness','acousticness','danceability','valence','instrumentalness'])


Data = {'tempo' : tempo, 'energy' : energy, 'speechiness' : speechiness, 'acousticness' : acousticness, 'danceability' : danceability, 'valence' : valence, 'instrumentalness' : instrumentalness}
# print(Data)
df = DataFrame(Data, columns=['tempo', 'energy', 'speechiness','acousticness','danceability','valence','instrumentalness'])


kmeans = KMeans(n_clusters=10).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['tempo'], df['energy'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()


print("\n\n-------------------------PCA----------------------")

X = np.array(list(zip(tempo, energy, speechiness, acousticness, danceability, valence, instrumentalness)))
X = X.astype(np.float64)

pca = PCA(n_components=2).fit(X)
datapoint = pca.transform(X)

kmeans = KMeans(n_clusters=10).fit(df)
centroids2 = kmeans.cluster_centers_
print(centroids)

plt.scatter(datapoint[:, 0], datapoint[:, 1], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
#centroids2 = kmeans.cluster_centers_
centroidpoint = pca.transform(centroids)
plt.scatter(centroidpoint[:,0], centroidpoint[:,1], c='red', s=50)
plt.show()