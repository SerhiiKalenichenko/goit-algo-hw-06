import collections
import networkx as nx

from graph_model import build_city_graph


def dfs_path(G: nx.Graph, start: str, goal: str) -> list[str] | None:
   
    visited: set[str] = set()
    path: list[str] = []

    def dfs(node: str) -> bool:
        visited.add(node)
        path.append(node)

        if node == goal:
            return True

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        path.pop()
        return False

    found = dfs(start)
    return path if found else None


def bfs_path(G: nx.Graph, start: str, goal: str) -> list[str] | None:
   
    visited: set[str] = {start}
    queue: collections.deque[str] = collections.deque([start])
    parents: dict[str, str | None] = {start: None}

    while queue:
        node = queue.popleft()
        if node == goal:
            break

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = node
                queue.append(neighbor)

    if goal not in parents:
        return None

    path: list[str] = []
    current: str | None = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path


def main() -> None:
    G = build_city_graph()

    start, goal = "A", "H"
    print(f"Пошук шляху з {start} до {goal}")

    dfs_result = dfs_path(G, start, goal)
    bfs_result = bfs_path(G, start, goal)

    print("\n=== DFS шлях ===")
    if dfs_result:
        print(" -> ".join(dfs_result))
    else:
        print("Шлях не знайдено")

    print("\n=== BFS шлях ===")
    if bfs_result:
        print(" -> ".join(bfs_result))
    else:
        print("Шлях не знайдено")

    print("\n=== Порівняння ===")
    if dfs_result and bfs_result:
        print(f"DFS довжина (у вершинах): {len(dfs_result)}")
        print(f"BFS довжина (у вершинах): {len(bfs_result)}")

        if len(dfs_result) == len(bfs_result):
            print("BFS і DFS знайшли шляхи однакової довжини за кількістю вершин.")
        else:
            print(
                "BFS гарантує мінімальну кількість кроків (ребер), "
                "DFS може дати довший або більш «обхідний» шлях."
            )

        print(
            "Різниця пояснюється стратегіями обходу: "
            "DFS йде «в глибину» першою доступною гілкою, "
            "BFS рівномірно розширює фронт пошуку по всім сусідам."
        )
    else:
        print("Порівнювати нічого – один з алгоритмів шляху не знайшов.")


if __name__ == "__main__":
    main()