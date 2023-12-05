# 261 Graph Valid Tree (Premium)
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

*Example 1:*

```
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
```

*Example 2:*

```
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
```

## Optimized Solution

### Approach
Valid tree is when there are no loops and all vertices are connected. So we want to check from the starting vertex if we can reach every other vertex from that, so if the number of visited vertices equal the total vertices in the graph. Also if a vertex appears twice during traversal then we know we hit a cycle. While using our dfs helper function we keep track of the previous (parent) vertex visited to make sure we skip that parent vertex when we're at the next vertex and we want to visit the other connected vertices.

### Complexity
$$Time: O(V + E)$$

$$Space: O(V + E)$$

### Code
```
def validTree(self, n, edges):
    # empty graph is a tree
    if not n :
        return True

    adj = { i:[] for i in range(n) }
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = set()
    def dfs(vertex, prev):
        if vertex in visited:
            return False

        visited.add(vertex)
        for v in adj[vertex]:
            if v == prev:
                continue
            if not dfs(v, vertex):
                return False

        return True

    return dfs(0, -1) and len(visited) == n
```