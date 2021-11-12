'''
#1
Given a directed graph, design an algorithm to find out whether there is a route
between two nodes.

Example:
Directed
Input: [[1], [2], [0, 1], [2], [5], [4]]
Output: 
'''

from graph import Graph

def route_between_nodes(graph, node0, node1):
    vertices = graph.vertices
    for v in vertices:
        if 
