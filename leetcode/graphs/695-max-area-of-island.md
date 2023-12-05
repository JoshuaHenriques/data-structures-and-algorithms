# 695. Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

*Example 1:*

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

*Example 2:*

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

*Constraints:*

```
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
```

## Optimized Solution

### Approach
Perform BFS on the graph with an extra parameter area that keeps track of the current area of that island. After traversing that current island we update the max area with the current area if it's bigger then return the result

### Complexity
$$Time: O(n*m)$$

$$Space: O()$$

### BFS Code
```
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    rows, cols  = len(grid), len(grid[0])
    maxArea = 0
    visited = set()

    def bfs(r, c, area):
        nonlocal maxArea
        queue = deque()
        if (r, c) in visited:
            return

        visited.add((r, c))
        queue.append((r, c))
        while queue:
            row, col = queue.popleft()

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                rdr, cdc = row + dr, col + dc

                if rdr in range(rows) and cdc in range(cols) and grid[rdr][cdc] == 1 and (rdr, cdc) not in visited:
                    queue.append((rdr, cdc))
                    visited.add((rdr, cdc))
                    area += 1

        maxArea = max(maxArea, area)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                bfs(row, col, 1)

    return maxArea
```

### DFS Code
```
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):
        if (
            r < 0
            or r == ROWS
            or c < 0
            or c == COLS
            or grid[r][c] == 0
            or (r, c) in visit
        ):
            return 0
        visit.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            area = max(area, dfs(r, c))
    return area
```