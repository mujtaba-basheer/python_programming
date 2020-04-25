import min_heap
import un_wt_graph

class Dijkstra(un_wt_graph.UndirectedWeightedGraph):

    def __init__(self):
        super().__init__()
        self.S = set()
        self.Q = min_heap.MinHeap(list())

    def initialize_graph(self):
        source = input()
        self.initialize(source)

    def dijkstra(self):
        self.Q = min_heap.MinHeap([(v, self.d[v]) for v in self.vertices])

        while self.Q.get_length() != 0:
            u = self.Q.extract_min()
            self.S.add(u)

            if u not in self.adj:
                self.adj[u] = set()
            for v in self.adj[u]:
                val =  self.relax(u, v)
                if val != False:
                    self.Q.decrease_key(v, val)

    def find_shortest_path(self):
        u, v = list(map(str, input().split()))
        if u == v:
            print("At source!")
            print(f"Path length: {self.d[u]}")
            return
        self.get_shortest_path(u, v)

    def get_shortest_path(self, u, v):
        self.initialize(u)
        self.dijkstra()
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
    graph = Dijkstra()
    graph.find_shortest_path()
    graph.enumerate()
    # print(graph.S)