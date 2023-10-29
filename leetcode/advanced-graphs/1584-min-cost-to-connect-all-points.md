# 1584. Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

*Example 1:*

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: We can connect the points as shown above to get the minimum cost of 20. Notice that there is a unique path between every pair of points.
```

*Example 2:*

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

*Constraints:*

```
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
```

## Prim's Algorithm Solution

### Approach
Create the adjacency list by using a double for loop to get the weights and create the edges from vertex to vertex. Then apply Prim's Algorithm. Refer to Prim's Algorithm in algorithms.md.

### Complexity
$$Time: O(n^2logn)$$

$$Space: O(n)$$

### Code
```
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    N = len(points)
    adjMap = defaultdict(list) # i : list of [cost, node]
    
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adjMap[i].append([dist, j])
            adjMap[j].append([dist, i])

    # Prim's
    result = 0
    visited = set()
    minHeap = [[0, 0]] # [cost, point]
    while len(visited) < N:
        cost, i = heapq.heappop(minHeap)
        if i in visited:
            continue
        
        result += cost
        visited.add(i)
        for neighCost, neigh in adjMap[i]:
            if neigh not in visited:
                heapq.heappush(minHeap, [neighCost, neigh])

    return result
```

## Kruskal's Algorithm Solution

### Approach
Union Find. Refer to Kruskal's Algorithm in algorithms.md.

### Complexity
$$Time: O(n^2logn)$$

$$Space: O(n^2)$$

### Code
```
def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return False
        
        if self.rank[u] > self.rank[v]:
            u, v = v, u
            
        self.parent[u] = v
        
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
        
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        
        edges = []
        
        for i in range(n):
            for j in range(i+1, n):
                distance = manhattan_distance(points[i], points[j])
                heappush(edges, (distance, i, j))
        
        mst_weight = 0
        mst_edges = 0
        
        while edges:
            w, u, v = heappop(edges)
            if uf.union(u, v):
                mst_weight += w
                mst_edges += 1
                if mst_edges == n - 1:
                    break
                    
        return mst_weight
```