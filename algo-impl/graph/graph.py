# A class to represent a directed graph object
class Graph:
    # constructor
    def __init__(self, edges, N):
 
        # a list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            # self.adjList[dest].append(src)