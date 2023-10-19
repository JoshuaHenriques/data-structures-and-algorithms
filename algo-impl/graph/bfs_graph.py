"""
Deque (Doubly Ended Queue) in Python is implemented using the module
“collections“. Deque is preferred over list in the cases where we need quicker
append and pop operations from both the ends of container, as deque provides an
O(1) time complexity for append and pop operations as compared to list which
provides O(n) time complexity.
"""

from collections import deque
from graph import Graph

def bfs_iterative(graph, vertex, discovered):

	queue = deque()

	discovered[vertex] = True

	queue.append(vertex)
	
	# loop till queue is empty
	while queue:

		# dequeue front node and print it
		vertex = queue.popleft()
		print(vertex, end=' ')

		# do for every edge `v -> u`
		for u in graph.adjList[vertex]:
			if not discovered[u]:
				# mark it as discovered and enqueue it
				discovered[u] = True
				queue.append(u)

def bfs_recursion(graph, queue, discovered):
	if not queue:
		return

	# dequeue front node and print it
	vertex = queue.popleft()
	print(vertex, end=' ')

	# do for every edge `v -> u`
	for u in graph.adjList[vertex]:
		if not discovered[u]:
			# mark it as discovered and enqueue it
			discovered[u] = True
			queue.append(u)

	bfs_recursion(graph, queue, discovered)

if __name__ == '__main__':
	# list of graph edges as per the above diagram
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]
 
    # total number of nodes in the graph
    N = 15
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
 
    # perform BFS traversal from all undiscovered nodes to
    # cover all unconnected components of a graph
    for i in range(N):
        if not discovered[i]:
            # start BFS traversal from vertex i
            bfs_iterative(graph, i, discovered)
            
    que = deque()
    discovered1 = [False] * N
    for i in range(N):
        if not discovered1[i]:
            discovered1[i] = True
            que.append(i)
            bfs_recursion(graph, que, discovered1)