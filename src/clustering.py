import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

def cluster_entregas(file_path, k=3):

    data = pd.read_csv(file_path)

    coords = data[['latitude','longitude']]

    kmeans = KMeans(n_clusters=k, random_state=42)
    data['cluster'] = kmeans.fit_predict(coords)

    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(8,6))

    scatter = plt.scatter(
        data['longitude'],
        data['latitude'],
        c=data['cluster'],
        cmap="viridis",
        s=120,
        edgecolors="black"
    )

    plt.title("Clusters de Entrega - Sabor Express", fontsize=14)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.grid(True)

    plt.savefig("outputs/clusters.png", dpi=300)

    return data