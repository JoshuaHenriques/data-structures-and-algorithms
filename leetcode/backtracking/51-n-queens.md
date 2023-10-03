# 51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

*Example 1:*

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

*Example 2:*

```
Input: n = 1
Output: [["Q"]]
```

*Constraints:*

```
1 <= n <= 9
```

## Solution

### Approach
For each Q we need to keep track of the cells the queen can attack. We don't need to keep track of the row since we know only one Q can be on a row at a time. One Q for a column as well but we will keep track of it in a hashset. We keep track of the positive and negative diagonals. The positive diagonals always equate to the same value if you do row + col and the negative diagonals are row - col. We also initial a blank board. We create a dfs helper function to help us recursively call each row to get every combination of Q placements. In each recursive call the base case will be if the row we're at equals the total queens, if satisfied we convert that row into a string and append it to the result array. Then we loop through each column in that row and if the Q and col are valid we place the queen and update our tracker sets then recursively call the dfs function of the next row. Now for the backtracking part if a combination didn't work out we remove the current row & col from our trackers and remove the Q and continue on with the calls.

### Complexity
$$Time: O()$$

$$Space: O(n)$$

### Code
```
def solveNQueens(self, n: int) -> List[List[str]]:
    colSet = set()
    posDiag = set()
    negDiag = set()

    result = []
    board = [["."] * n for i in range(n)]

    def dfs(row):
        if row == n:
            copy = ["".join(r) for r in board]
            result.append(copy)
            return

        for col in range(n):
            if col in colSet or (row + col) in posDiag or (row - col) in negDiag:
                continue

            colSet.add(col)
            posDiag.add(row + col)
            negDiag.add(row - col)
            board[row][col] = "Q"

            dfs(row + 1)

            colSet.remove(col)
            posDiag.remove(row + col)
            negDiag.remove(row - col)
            board[row][col] = "."
    
    dfs(0)
    return result
```

board: [['Q', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['Q', '.', '.', '.'], ['.', '.', 'Q', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['Q', '.', '.', '.'], ['.', '.', '.', 'Q'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['Q', '.', '.', '.'], ['.', '.', '.', 'Q'], ['.', 'Q', '.', '.'], ['.', '.', '.', '.']]
board: [['.', 'Q', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', 'Q', '.', '.'], ['.', '.', '.', 'Q'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', 'Q', '.', '.'], ['.', '.', '.', 'Q'], ['Q', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', 'Q', '.', '.'], ['.', '.', '.', 'Q'], ['Q', '.', '.', '.'], ['.', '.', 'Q', '.']]
copy: ['.Q..', '...Q', 'Q...', '..Q.']
board: [['.', '.', 'Q', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', '.', 'Q', '.'], ['Q', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', '.', 'Q', '.'], ['Q', '.', '.', '.'], ['.', '.', '.', 'Q'], ['.', '.', '.', '.']]
board: [['.', '.', 'Q', '.'], ['Q', '.', '.', '.'], ['.', '.', '.', 'Q'], ['.', 'Q', '.', '.']]
copy: ['..Q.', 'Q...', '...Q', '.Q..']
board: [['.', '.', '.', 'Q'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', '.', '.', 'Q'], ['Q', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
board: [['.', '.', '.', 'Q'], ['Q', '.', '.', '.'], ['.', '.', 'Q', '.'], ['.', '.', '.', '.']]
board: [['.', '.', '.', 'Q'], ['.', 'Q', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
