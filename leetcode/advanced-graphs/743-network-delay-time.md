# 743. Network Delay Time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

*Example 1:*

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

*Example 2:*

```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

*Example 3:*

```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

*Constraints:*

```
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
```

## Optimized Solution

### Approach
Dijkstra's algorithm. First we create and populate the adjacency list using a hashmap with the list hold tuples of the target and weight. Dijkstra's algorithm involves using BFS and a minHeap (instead of queue) to keep track of the shortest path to that target vertex. While the minHeap isn't empty we pop from it and check if it's been visited before, if not we add it to the visited set and set the result time to the max of itself and the popped weight. The bfs part is us looping through each adjacent vertex and if it hasn't been visited we push it on the minHeap with the total weight, the current popped weight plus this adjacent weight, and the vertex as a tuple. In the end we'll have the minimum time it takes for each vertex to get the signal. Return -1 if would list of visited isn't the same length as the total nodes, this means the graph is disjointed

### Complexity
$$Time: O(E*logV)$$

$$Space: O()$$

### Code
```
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    adj = { i:[] for i in range(1, n+1) }
    for u, v, w in times:
        adj[u].append((v, w))

    minHeap = [(0, k)]
    visited = set()
    time = 0

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visited:
            continue

        visited.add(n1)
        time = max(time, w1)

        for n2, w2 in adj[n1]:
            if n2 not in visited:
                heapq.heappush(minHeap, (w2 + w1, n2))

    return time if len(visited) == n else -1
```