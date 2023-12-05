# 994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

*Example 1:*

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

*Example 2:*

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

*Example 3:*

```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

*Constraints:*

```
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
```

## Solution

### Approach
BFS approach. Key part to this is when we initially go through each cell we don't call our bfs helper function on the first rotten orange we see, we instead add each rotten orange to our queue first. Then call bfs with queue as our parameter and while there is an oranges in the queue we loop through and pop each item in the queue (for loop the current snapshot of the queue length) and push any fresh oranges to the queue that's adjacent to that one and set it to a rotten orange. After that queue iteration we can increment minutes since we don't want to increment minutes at each adjacent orange. We pass through the grid again and if we find a fresh orange we return -1, that means it was impossible.

### Complexity
$$Time: O(n*m)$$

$$Space: O(n*m)$$

### Code
```
def orangesRotting(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    minutes, fresh = -1, 0
    queue = deque()
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                fresh += 1

    while queue: 
        for _ in range(len(queue)):
            row, col = queue.popleft()

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                rdr, cdc = row + dr, col + dc

                if rdr in range(rows) and cdc in range(cols) and (rdr, cdc) not in visited and grid[rdr][cdc] == 1:
                    queue.append((rdr, cdc))
                    visited.add((rdr, cdc))
                    grid[rdr][cdc] = 0
                    fresh -= 1
        minutes += 1

    if fresh > 0:
        return -1

    return 0 if minutes == -1 else minutes
```