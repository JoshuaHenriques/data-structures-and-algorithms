# 323. Number of Connected Components in an Undirected Graph (Premium)
In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

You need to return the number of connected components in that graph.

*Example 1:*

```
Input: 3, [[0,1], [0,2]]
Output: 1
```

*Example 2:*

```
Input: 6, [[0,1], [1,2], [2, 3], [4, 5]]
Output: 2
```

## Naive Solution

### Approach
DFS on each vertex to go through the adjacency map and keep track of the visited nodes in every vertex iteration. So when we go through the vertices if a vertex wasn' in the visited set from the first vertex then we know it's a different component. If we were able to visit all vertices from the first vertex then the whole graph is connected.

## Optimized Solution

### Approach


### Complexity
$$Time: O(E + V)$$

$$Space: O(E + V)$$

### Code
```
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    parent = [i for i in range(n)]
    rank = [1] * n

    def find(n1):
        res = n1
        
        while res != parent[res]:
            # path compression
            parent[res] = parent[parent[res]]
            res = parent[res]
        return res

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res
```