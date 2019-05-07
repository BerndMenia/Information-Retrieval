from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# NOTE: this script constructs our kmeans model and forms the plot; kmeans_cluster is called in clusterdocs.py

class kmeans:
    def kmeans_cluster(self, docvec):
        # create the kmeans object with doc vecs
        # TODO:NOTE: adapt the n_cluster parameter for experimenting with kmeans; note that the color_labels below need to include n_cluster different items; the effect of choosing n_clusters can be seen well when comparing n_cluster=5 and n_cluster=10
        kmeans_model = KMeans(n_clusters=5, n_init=10, max_iter=2500)
        X = kmeans_model.fit(docvec)
        labels = kmeans_model.labels_.tolist()

        l = kmeans_model.fit_predict(docvec)
        # reduce dimensionality of our data to to project it in 2D space
        pca = PCA(n_components=2).fit(docvec)
        datapoint = pca.transform(docvec)

        plt.figure()
        color_labels = ["#FFFF00", "#008000", "#0000FF", "#800080", "#f5b041", "#5dade2", "#f1948a", "#d0d3d4", "#f9e79f", "#e8daef"]
        '''
        just experimented with more clusters, hence given up to 50 different colors below
        color_labels = ["#7CFC00",
                        "#7FFF00",
                        "#32CD32",
                        "#00FF00",
                        "#228B22",
                        "#008000",
                        "#006400",
                        "#ADFF2F",
                        "#9ACD32",
                        "#00FF7F",
                        "#00FA9A",
                        "#90EE90",
                        "#98FB98",
                        "#8FBC8F",
                        "#3CB371",
                        "#2E8B57",
                        "#808000",
                        "#556B2F",
                        "#6B8E23",
                        "#E0FFFF",
                        "#00FFFF",
                        "#00FFFF",
                        "#7FFFD4",
                        "#66CDAA",
                        "#AFEEEE",
                        "#40E0D0",
                        "#48D1CC",
                        "#00CED1",
                        "#20B2AA",
                        "#5F9EA0",
                        "#008B8B",
                        "#008080",
                        "#B0E0E6",
                        "#ADD8E6",
                        "#87CEFA",
                        "#87CEEB",
                        "#00BFFF",
                        "#B0C4DE",
                        "#1E90FF",
                        "#6495ED",
                        "#4682B4",
                        "#4169E1",
                        "#0000FF",
                        "#0000CD",
                        "#00008B",
                        "#000080",
                        "#191970",
                        "#7B68EE",
                        "#6A5ACD",
                        "#483D8B"]
        '''
        color = [color_labels[i] for i in labels]
        plt.scatter(datapoint[:, 0], datapoint[:, 1], c=color)

        centroids = kmeans_model.cluster_centers_
        centroidpoint = pca.transform(centroids)
        plt.scatter(centroidpoint[:,0], centroidpoint[:,1], marker='^', s=150, c='#000000')
        plt.show()
