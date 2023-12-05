# 286 Walls and Gates (Premium)
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

*Example 1:*

```
Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

the answer is:
  3  -1   0   1

  2   2   1  -1

  1  -1   2  -1

  0  -1   3   4
```

*Example 2:*

```
Input:
[[0,-1],[2147483647,2147483647]]
Output:
[[0,-1],[1,2]]
```

## Optimized Solution

### Approach
Traverse the graph and find all gate cells and push to the queue. While there's something in the queue we loop and pop from the queue (for loop the current snapshot of the queue length) to look at adjacent cells that aren't walls and push them on the queue, set them as the current distance, and add them to the visited set. After for loop on that layer of the queue we increment the distance.

### Complexity
$$Time: O(n*m)$$

$$Space: O(n*m)$$

### Code (not tested)
```
def wallsAndGates(self, rooms: List[List[int]]) -> None:
    rows, cols = len(rooms), len(rooms[0])
    visited = set()
    queue = deque()

    for r in range(rows):
        c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))
                visited.add((r, c))

    dist = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            rooms[r][c] = dist

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if r in range(rows) and c in range(cols) and (r, c) not in visited and rooms[r][c] != -1:
                    visited.add((r, c))
                    queue.append((r, c))

        dist += 1
```