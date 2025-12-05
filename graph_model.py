import networkx as nx


def build_city_graph() -> nx.Graph:
    """
    Будує неорієнтований зважений граф,
    що моделює транспортну мережу району міста.
    Вершини: перехрестя, ваги ребер: умовні кілометри.
    """
    G = nx.Graph()

    # Вершини – перехрестя/зупинки
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
    G.add_nodes_from(nodes)

    # Ребра (u, v, distance_km)
    edges = [
        ("A", "B", 2),
        ("A", "C", 4),
        ("B", "C", 1),
        ("B", "D", 7),
        ("C", "D", 3),
        ("C", "E", 4),
        ("D", "F", 2),
        ("E", "F", 3),
        ("E", "G", 5),
        ("F", "G", 1),
        ("F", "H", 4),
        ("G", "H", 2),
    ]

    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    return G