# 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.


*Example 1:*

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

*Example 2:*

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

*Constraints:*

* m == matrix.length
* n == matrix[i].length
* 1 <= n, m <= 300
* -109 <= matrix[i][j] <= 109
* All the integers in each row are sorted in ascending order.
* All the integers in each column are sorted in ascending order.
* -109 <= target <= 109


## Solution

### Approach

Search through the matrix using binary search on the rows and cols but the key is where you start the binary search. Start at the last row and first column, if the target is less than the current element you move up a row and if it's greater you go to the next column.

### Complexity

$$Time: O(n+m)$$

$$Space: O(1)$$

### Code

```py
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    N, M = len(matrix), len(matrix[0])
    r, c = N - 1, 0

    while r >= 0 and c < M:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            r -= 1
        else:
            c += 1

    return False
```
