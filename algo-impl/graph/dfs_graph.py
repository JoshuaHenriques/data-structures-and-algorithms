from graph import Graph
from collections import deque

def dfs_recursion(graph, vertex, discovered):
	discovered[vertex] = True # mark the current node as discovered
	print(vertex, end=' ')

	# do for every edge `v -> u`
	for u in graph.adjList[vertex]:
		if not discovered[u]: # if `u` is not yet discovered
			dfs_recursion(graph, u, discovered)

def dfs_iterative(graph, vertex, discovered):
	# create a stack used to do iterative DFS
	stack = deque()

	# push the source node into the stack
	stack.append(vertex)

	# loop till stack is empty
	while stack:
		# pop a vertex from the stack
		vertex = stack.pop()

		# if the vertex is already discovered, ignore it 
		if discovered[vertex]:
			continue

		# not discovered so mark vertex as discovered
		discovered[vertex] = True
		print(vertex, end=' ')

		# do for every edge `v -> u`
		adj = graph.adjList[vertex]
		# auxiliary stack to visit neighbours in the order they a in the
		# adjacency list. alternatively: iterate through ArrayList in reverse or
		# but this is only to get the same output as the recursion otherwise,
		# this would not be necessary
		for i in reversed(range(len(adj))):
			# print(adj[i])
			u = adj[i]
			if not discovered[u]:
				stack.append(u)
	
if __name__ == "__main__":
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # total number of nodes in the graph (0–12)
    N = 13
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all unconnected components of a graph
    for i in range(N):
        if not discovered[i]:
            dfs_recursion(graph, i, discovered)
            
    discovered1 = [False] * N
    for i in range(N):
        if not discovered1[i]:
            dfs_iterative(graph, i, discovered1)