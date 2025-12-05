import matplotlib.pyplot as plt
import networkx as nx

from graph_model import build_city_graph


def analyze_graph(G: nx.Graph) -> None:
    print("=== Базові характеристики графа ===")
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер:  {G.number_of_edges()}")

    degrees = dict(G.degree())
    print("\nСтупені вершин:")
    for node, deg in degrees.items():
        print(f"  {node}: {deg}")

    print("\nВаги ребер (distance_km):")
    for u, v, data in G.edges(data=True):
        print(f"  {u} – {v}: {data.get('weight', 1)} км")


def draw_graph(G: nx.Graph) -> None:
    """
    Візуалізація графа з підписами вершин і вагами ребер.
    """
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=800,
        font_size=10,
        node_color="lightblue",
        edgecolors="black",
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    plt.title("Транспортна мережа району міста (умовний граф)")
    plt.tight_layout()
    plt.show()


def main() -> None:
    G = build_city_graph()
    analyze_graph(G)
    draw_graph(G)


if __name__ == "__main__":
    main()