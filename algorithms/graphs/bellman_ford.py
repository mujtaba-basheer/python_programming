import dir_wt_graph

class Bellman_Ford(dir_wt_graph.DirectedWeightedGraph):

    def __init__(self):
        super().__init__()

    def initialize_graph(self):
        source = input()
        self.initialize(source)

    def bellman_ford(self):
        for x in self.vertices:
            for edge in self.edges:
                u, v = edge
                self.relax(u, v)

        for edge in self.edges:
            u, v = edge
            if self.d[v] > self.d[u] + self.weights[edge]:
                raise Exception("Negative cycle detected!")

    def find_shortest_path(self):
        u, v = list(map(str, input().split()))
        if u == v:
            print("At source!")
            print(f"Path length: {u}")
            return
        self.get_shortest_path(u, v)

    def get_shortest_path(self, u, v):
        self.initialize(u)
        self.bellman_ford()
        if self.d[u] == float("inf"):
            print("No possible path!")
        else:
            path = [v,]
            while self.predecessor[v] is not None:
                path.append(self.predecessor[v])
                v = self.predecessor[v]
            path.reverse()
            print("Path: ", end = "")
            for v in path:
                print(v, end = " ")
            print(f"\nPath length: {self.d[v]}")

if __name__ == "__main__":
    graph = Bellman_Ford()
    graph.initialize_graph()
    graph.bellman_ford()
    graph.enumerate()
    # graph.find_shortest_path()