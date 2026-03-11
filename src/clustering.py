import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def cluster_entregas(file_path, k=3):

    data = pd.read_csv(file_path)

    coords = data[['latitude','longitude']]

    kmeans = KMeans(n_clusters=k, random_state=42)
    data['cluster'] = kmeans.fit_predict(coords)

    plt.scatter(data['longitude'], data['latitude'], c=data['cluster'])
    plt.title("Clusters de Entrega")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.savefig("outputs/clusters.png")

    return data