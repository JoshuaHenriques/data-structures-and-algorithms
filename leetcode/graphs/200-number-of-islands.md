# 200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

*Example 1:*

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

*Example 2:*

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

*Constraints:*

```
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
```

## Optimized Solution

### Approach
Using BFS we can check the adjacent cells if they are also islands. Firstly we loop through all cells and if one of them is an island we increment islands counter and we perform bfs on it using the helper function. In the helper function we mark that cell as visited and add it to the queue then while the queue still has elements we pop an element off the queue and for each direction we need to go to we check if the cell is valid. The cell is valid if that direction is within the bounds of the grid and if it's an island and that cell wasn't visited already, if valid we add that cell to the queue and mark it as visited.

### Complexity
$$Time: O(n^2)$$

$$Space: O(n)$$

### Code
```
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque()
        visited.add((r, c))
        queue.append((r, c))

        while queue:
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and 
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                    queue.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands
```