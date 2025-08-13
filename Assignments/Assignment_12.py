from collections import deque, defaultdict
import heapq


class CityGraph:
    def __init__(self):
        # adjacency[u] = {v: weight, ...}  (directed edges u -> v)
        self.adjacency = defaultdict(dict)

    # ---------- Locations ----------
    def add_location(self, name: str):
        """Add a location (vertex). No-op if it already exists."""
        _ = self.adjacency[name]  # ensures key exists

    def remove_location(self, name: str):
        """Remove location and all incident roads."""
        if name not in self.adjacency:
            return
        # remove outgoing
        self.adjacency.pop(name, None)
        # remove incoming
        for u in list(self.adjacency.keys()):
            self.adjacency[u].pop(name, None)


    # Roads (directed)
    def add_road(self, src: str, dst: str, time: float):
        """Add/update a directed road src -> dst with travel time."""
        if src not in self.adjacency:
            self.add_location(src)
        if dst not in self.adjacency:
            self.add_location(dst)
        self.adjacency[src][dst] = float(time)

    def remove_road(self, src: str, dst: str):
        """Remove the directed road src -> dst."""
        if src in self.adjacency:
            self.adjacency[src].pop(dst, None)

    #Shortest Path: Dijkstra
    def shortest_path(self, start: str, goal: str):
        """
        Dijkstra's algorithm (non-negative weights).
        Returns (total_time, path_list). Raises ValueError if unreachable or missing nodes.
        """
        if start not in self.adjacency or goal not in self.adjacency:
            raise ValueError("Start or goal location does not exist.")

        dist = {start: 0.0}
        prev = {}
        pq = [(0.0, start)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if u == goal:
                break
            if d != dist.get(u, float("inf")):
                continue  # stale
            for v, w in self.adjacency[u].items():
                nd = d + w
                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))

        if goal not in dist:
            raise ValueError(f"No path from {start} to {goal}.")

        # reconstruct path
        path = [goal]
        cur = goal
        while cur != start:
            cur = prev[cur]
            path.append(cur)
        path.reverse()
        return dist[goal], path

    #  Reachable: BFS (unweighted reachability)
    def reachable_from(self, start: str):
        """
        Returns a list of locations reachable from start (including start),
        discovered by BFS over directed edges.
        """
        if start not in self.adjacency:
            raise ValueError("Start location does not exist.")

        seen = set([start])
        order = []
        q = deque([start])
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return order

    # Pretty-print 
    def __str__(self):
        lines = []
        for u in sorted(self.adjacency):
            edges = ", ".join(f"{u} -> {v} ({w})" for v, w in self.adjacency[u].items())
            lines.append(edges if edges else f"{u} -> ∅")
        return "\n".join(lines)


# Demo 
if __name__ == "__main__":
    g = CityGraph()

    # 1) Add at least 6 locations
    locations = ["Hospital", "School", "Store", "Library", "Station", "Park"]
    for loc in locations:
        g.add_location(loc)

    # 2) Add at least 10 directed roads (with travel times in minutes)
    roads = [
        ("Hospital", "School", 6),
        ("Hospital", "Store", 10),
        ("School", "Library", 5),
        ("School", "Station", 7),
        ("Store", "Library", 2),
        ("Library", "Park", 4),
        ("Station", "Park", 3),
        ("Station", "Store", 6),
        ("Park", "Hospital", 12),
        ("Store", "Station", 3),
        # extras to make routing interesting
        ("Hospital", "Library", 15),
        ("Library", "School", 8),
    ]
    for u, v, w in roads:
        g.add_road(u, v, w)

    print("City Map (directed, weighted):")
    print(g)
    print()

    # 3A) Add/remove examples
    g.add_location("CityHall")
    g.add_road("CityHall", "Hospital", 5)
    g.add_road("CityHall", "Library", 9)
    g.remove_road("Library", "School")     # remove an edge
    # g.remove_location("CityHall")        # try removing a vertex if you want

    # 3B) Shortest path (Dijkstra)
    start, goal = "Hospital", "Park"
    total_time, path = g.shortest_path(start, goal)
    print(f"Shortest path from {start} to {goal}: {path} (time={total_time} min)")

    # 3C) Reachable locations (BFS)
    origin = "School"
    print(f"Reachable from {origin}: {g.reachable_from(origin)}")
