# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):

        # A list of lists to represent an adjacency list
        self.adjList_directed = [[] for _ in range(n)]
        self.adjList_undirected = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest) in edges:
            self.adjList_directed[src].append(dest)
            if dest not in self.adjList_undirected[src]:
                self.adjList_undirected[src].append(dest)
            if src not in self.adjList_undirected[dest]:
                self.adjList_undirected[dest].append(src)

    # Function to print adjacency list representation of a graph
    def printGraph(adjList):
        for src in range(len(adjList)):
            # print current vertex and all its neighboring vertices
            for dest in adjList[src]:
                print(f'({src} —> {dest}) ', end='')
            print()


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    graph = Graph(edges, 6)
    print('Directed')
    print(graph.adjList_directed)
    print('Undirected')
    print(graph.adjList_undirected)
    print('Directed')
    Graph.printGraph(graph.adjList_directed)
    print('Undirected')
    Graph.printGraph(graph.adjList_undirected)