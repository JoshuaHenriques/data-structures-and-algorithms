# 1926. Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

*Example 1:*

```
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
```

*Example 2:*

```
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
```

*Example 3:*

```
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
```

*Constraints:*

*  maze.length == m
*  maze[i].length == n
*  1 <= m, n <= 100
*  maze[i][j] is either '.' or '+'.
*  entrance.length == 2
*  0 <= entrancerow < m
*  0 <= entrancecol < n
*  entrance will always be an empty cell.

## Solution

### Approach

Using a queue and a visited set we can use BFS to traverse the maze level by level. The queue will keep track of the current row, col, and steps. When we pop the cell from the queue we'll check it's surronding cells to see if it's empty or a wall. If it's empty we check if it's not an exit then we add it back to the queue if it is an exit we can just return since that'll be the nearest exit since we checked level by level with BFS traversal.

### Complexity

$$Time: O(n*m)$$

$$Space: O(n*m)$$

### Code

```py
def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    rows, cols = len(maze), len(maze[0])

    queue = deque([(entrance[0], entrance[1], 0)])
    visited = set()
    visited.add((entrance[0], entrance[1]))

    while queue:
        row, col, steps = queue.popleft()

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            rdr, cdc = dr + row, dc + col
            if rdr in range(rows) and cdc in range(cols) and maze[rdr][cdc] == "." and (rdr, cdc) not in visited:
                if (rdr == 0 or rdr == rows - 1) or (cdc == 0 or cdc == cols - 1):
                    return steps + 1
                
                queue.append((rdr, cdc, steps + 1))
                visited.add((rdr, cdc))

    return -1
```
