import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

def Dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0

    predecessors = {node: None for node in graph.graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 6)
    graph.add_edge("C", "D", 3)

    start_node = "A"

    distances, predecessors = Dijkstra(graph, start_node)

    print(f"Najkrótsze odległości od wierzchołka {start_node}:")
    for node, distance in distances.items():
        print(f"{node}: {distance}")

    print("\nPoprzednicy na ścieżce:")
    for node, predecessor in predecessors.items():
        print(f"{node}: {predecessor}")
