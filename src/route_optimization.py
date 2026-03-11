import networkx as nx

def create_graph():

    G = nx.Graph()

    edges = [
        ("Restaurante","A",2),
        ("Restaurante","B",4),
        ("A","C",3),
        ("B","C",1),
        ("C","D",5),
        ("D","Cliente",2)
    ]

    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G


def shortest_path():

    G = create_graph()

    path = nx.astar_path(G, "Restaurante", "Cliente")

    return path