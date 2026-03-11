from clustering import cluster_entregas
from route_optimization import shortest_path
from map_visualization import gerar_mapa


def main():

    print("Calculando clusters de entrega...")

    data = cluster_entregas("data/entregas.csv")

    print(data)

    print("\nCalculando melhor rota...")

    path = shortest_path()

    print("Melhor rota:", path)

    print("\nGerando mapa da rota...")

    gerar_mapa()


if __name__ == "__main__":
    main()