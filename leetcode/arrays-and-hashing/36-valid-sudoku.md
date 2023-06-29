# 36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
* Each row must contain the digits 1-9 without repetition.
* Each column must contain the digits 1-9 without repetition.
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

*Example 1:*

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

*Example 2:*

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

*Constraints:*

```
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
```

## Naive Solution

### Approach
Group the coordinates of each number in a hashmap. At each number, compare the list of coordinates to check if they satisfy each of the three rules of sudoku

### Complexity
$$Time: O(9^2)$$

$$Space: O(9^2)$$

### Code
```
def isValidSudoku(self, board: List[List[str]]) -> bool:
    hashmap = defaultdict(list)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                hashmap[board[i][j]].append([i,j])

    for v in hashmap.values():
        if len(v) == 1:
            continue

        for i in range(len(v)):
            for j in range(i+1, len(v)):
                print(f'v[i]: {v[i]}')
                print(f'v[j]: {v[j]}')
                if v[i][0] == v[j][0]:
                    return False
                elif v[i][1] == v[j][1]:
                    return False
                elif 0 <= v[i][0] < 3 and 0 <= v[j][0] < 3:
                    if 0 <= v[i][1] < 3 and 0 <= v[j][1] < 3:
                        return False
                    elif 3 <= v[i][1] < 6 and 3 <= v[j][1] < 6:
                        return False
                    elif 6 <= v[i][1] <= 8 and 6 <= v[j][1] <= 8:
                        return False  
                elif 3 <= v[i][0] < 6 and 3 <= v[j][0] < 6:
                    if 0 <= v[i][1] < 3 and 0 <= v[j][1] < 3:
                        return False
                    elif 3 <= v[i][1] < 6 and 3 <= v[j][1] < 6:
                        return False
                    elif 6 <= v[i][1] <= 8 and 6 <= v[j][1] <= 8:
                        return False 
                elif 6 <= v[i][0] <= 8 and 6 <= v[j][0] <= 8:
                    if 0 <= v[i][1] < 3 and 0 <= v[j][1] < 3:
                        return False
                    elif 3 <= v[i][1] < 6 and 3 <= v[j][1] < 6:
                        return False
                    elif 6 <= v[i][1] <= 8 and 6 <= v[j][1] <= 8:
                        return False 
    return True
```

## Optimized Solution

### Approach
Use a hashmap with a set as the value to check for repeated numbers in the rows, colomns, and squares (3x3 sections). By using integer division we're able to properly check if there is a duplicated number in each 3x3 section

### Complexity
$$Time: O(9^2)$$

$$Space: O(9^2)$$

### Code
```
def isValidSudoku2(self, board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set) # key is tuple (r//3, c//3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])

    return True
```