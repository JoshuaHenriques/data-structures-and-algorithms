# 1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

*Example 1:*

```
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

*Example 2:*

```
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

*Example 3:*

```
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
```

*Constraints:*

* 2 <= n <= 5 * 104
* connections.length == n - 1
* connections[i].length == 2
* 0 <= ai, bi <= n - 1
* ai != bi


## Solution

### Approach

Create a bidirectional adjacency list so we know the neighbours of each node. Create a set of the edges from the input array connections and a set to track the visited nodes. In our helper function dfs with the parameter of the current node, we'll iterate through the neighbours if it hasn't been visited before. If there isn't an edge pointing the neighbour to the curr node then that's an edge we would have to change so increment the result, add that neighbour to the visited set and recursively call our helper function with it. Since we start these recursive calls with 0 we know that the current node either has an edge pointing to 0 or an edge to a node that points to 0.

### Complexity

$$Time: O(n)$$

$$Space: O(n)$$

### Code

```py
def minReorder(self, n: int, connections: List[List[int]]) -> int:
    adjDict = { i: [] for i in range(n) }
    edges = { (i, j) for i, j in connections }
    visited = set()
    res = 0

    for i, j in connections:
        adjDict[i].append(j)
        adjDict[j].append(i)

    def dfs(curr):
        nonlocal res
        for neighbour in adjDict[curr]:
            if neighbour in visited:
                continue

            if (neighbour, curr) not in edges:
                res += 1
            
            visited.add(neighbour)
            dfs(neighbour)

    visited.add(0)
    dfs(0)
    return res
```