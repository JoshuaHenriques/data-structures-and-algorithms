# 130. Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

*Example 1:*

```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
```

*Example 2:*

```
Input: board = [["X"]]
Output: [["X"]]
```

*Constraints:*

```
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
```

## Optimized Solution

### Approach
Reverse thinking is a clever way of approaching this problem. Instead of first capturing the surrounded regions, we capture the unsurrounded regions starting from the border. Once we find a "O" cell we run dfs on it's neighbours since those would also be unsurrounded and mark them all "T" temporarily. Now we can simple pass through the board again and swap any "O"'s with "X"'s since we know the "O"'s that are left in the board are all valid to be changed. Next we just swap back the "T"'s to "O"s

### Complexity
$$Time: O(n*m)$$

$$Space: O()$$

### Code
```
def solve(self, board: List[List[str]]) -> None:
    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r not in range(rows) or c not in range(cols) or r == rows or c == cols or board[r][c] != "O":
            return

        board[r][c] = "T"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                dfs(r, c)
    
    # 2. Capture surrounded regions (O -> X)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
    
    # 3. Uncapture unsurrounded regions (T -> O)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "T":
                board[r][c] = "O"
```