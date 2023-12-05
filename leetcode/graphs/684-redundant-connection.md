# 684. Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

*Example 1:*

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

*Example 2:*

```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

*Constraints:*

```
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
```

## Naive Solution

### Approach
A tree is an undirected graph that is connected and has no cycles. Redundant edge will always be the one which is responsible for forming a cycle within a graph. We know a cycle will be formed because the number of edges >= number of nodes. For each edge in edges we check if there's a path that exists from v1 to v2 in our adjMap that we're building during this for loop. Each loop we reset our visited vertices. So if a path exists from v1 to v2 we return that edge if not we add it to our graph. In our recursive dfs function, if we ever get the same two vertices then we know there's a path, go through each neighbour of v1 and if that neighbour wasn't visited already we check and see if a path exists from vertex to v2. We eventually do this until we go to a neighbour that is the same as v2 and we return true.

### Complexity
$$Time: O(n^2)$$

$$Space: O(n*m)$$

### Code
```
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    adjMap = defaultdict(list)

    def path_exists(v1, v2):
        if v1 == v2:
            return True

        visited.add(v1)
        for vertex in adjMap[v1]:
            if vertex not in visited:
                if path_exists(vertex, v2):
                    return True

        return False

    for v1, v2 in edges:
        visited = set()

        if path_exists(v1, v2):
            return [v1, v2]
        else:
            adjMap[v1].append(v2)
            adjMap[v2].append(v1)

    return None
```

## Optimized Solution

### Approach
Union find approach.

### Complexity
$$Time: O(n)$$

$$Space: O()$$

### Code
```
# code
```