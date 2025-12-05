import heapq
import math
import networkx as nx

from graph_model import build_city_graph


def dijkstra(
    G: nx.Graph,
    source: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
   
    distances: dict[str, float] = {node: math.inf for node in G.nodes}
    parents: dict[str, str | None] = {node: None for node in G.nodes}

    distances[source] = 0.0
    queue: list[tuple[float, str]] = [(0.0, source)]

    while queue:
        current_dist, node = heapq.heappop(queue)

        if current_dist > distances[node]:
            continue

        for neighbor in G.neighbors(node):
            weight = G[node][neighbor].get("weight", 1)
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parents[neighbor] = node
                heapq.heappush(queue, (new_dist, neighbor))

    return distances, parents


def restore_path(
    parents: dict[str, str | None],
    source: str,
    target: str,
) -> list[str]:
   
    if parents[target] is None and source != target:
        return []

    path: list[str] = [target]
    current = target

    while current != source:
        parent = parents[current]
        if parent is None:
            return []
        path.append(parent)
        current = parent

    path.reverse()
    return path


def main() -> None:
    G = build_city_graph()

    print("=== Найкоротші шляхи між усіма вершинами (алгоритм Дейкстри) ===")

    for source in G.nodes:
        distances, parents = dijkstra(G, source)
        print(f"\nДжерело: {source}")
        for target in G.nodes:
            path = restore_path(parents, source, target)
            dist = distances[target]
            if not path:
                print(f"  {source} -> {target}: шляху немає")
            else:
                path_str = " -> ".join(path)
                print(f"  {source} -> {target}: {dist:.1f} км ({path_str})")


if __name__ == "__main__":
    main()