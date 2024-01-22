# 73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

*Example 1:*

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

*Example 2:*

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

*Constraints:*
* m == matrix.length
* n == matrix[0].length
* 1 <= m, n <= 200
* -231 <= matrix[i][j] <= 231 - 1

## Naive Solution

### Approach
Create two sets for rows and cols. First pass through of the matrix will add the column and row if the element is zero. Second pass through will set that element to 0 if it's row or column is in the set

### Complexity
$$Time: O(n*m)$$

$$Space: O(n + m)$$

### Code
```py
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    setRows = set()
    setCols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                setRows.add(i)
                setCols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in setRows or j in setCols:
                matrix[i][j] = 0
```

## Optimized Solution

### Approach
Have a variable to know if the first row needs to be zero. First passthrough of the matrix, if we find a zero we set the first row at that column to 0 to mark that that column needs to be zero. Same thing for the row's, we set at column 0 at the i'th row we set to 0 except the first row. In the first row we set rowZero to true if we need to set the first row to 0. Second pass through sets the needed rows and columns to 0 except the first ones. Then we have seperate pass throughs to set the first row and first column if needed.

### Complexity
$$Time: O(n*m)$$

$$Space: O(1)$$

### Code
```py
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    # determine which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    # partially set matrix to 0
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # set first coloum to zero if needed
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    # set first row to zero if needed
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0
```
