# 79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

*Example 1:*

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

*Example 2:*

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

*Example 3:*

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

*Constraints:*

```
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
```

## DFS/Backtracking Solution

### Approach
We get the length of the rows and cols from the board. Create a set that will store the tuples of the row and col that we have already seen so we don't revisit a cell. Create a helper function we can use to help with our DFS/Backtracking approach. In each call we first want to check if the current row and col is at is out of bounds in anyway, has already been visited/seen before, and if the character in that cell is equal to the current character we're at in the word. We keep an index as a parameter in the helper function to keep track of which character we're checking against. So if the index ever reaches the length of the word (minus one) then we know we got to the end of the word and we can return True. If it passes these checks and isn't the end of the word we add the row and col to the visited/seen set and recursively call the helper function for each direction while incrementing our word index. When finished remove the visited/seen row and col from the set and return the result.

### Complexity
$$Time: O(n * m * 4^n)$$

$$Space: O(n * m * 4^n)$$

### Code
```
def exist(self, board: List[List[str]], word: str) -> bool:
    def dfs(row, col, i):
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return False
        
        if (row, col) in seen:
            return False

        if board[row][col] != word[i]:
            return False


        if i == len(word) - 1:
            return True

        seen.add((row, col))
        res = (dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or 
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1))

        seen.remove((row, col))
        return res

    ROWS, COLS = len(board), len(board[0])
    seen = set() 
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == word[0] and dfs(r, c, 0): 
                    return True

    return False
```