from clustering import cluster_entregas
from route_optimization import shortest_path

def main():

    print("Calculando clusters de entrega...")

    data = cluster_entregas("data/entregas.csv")

    print(data)

    print("\nCalculando melhor rota:")

    path = shortest_path()

    print("Melhor rota:", path)

if __name__ == "__main__":
    main()