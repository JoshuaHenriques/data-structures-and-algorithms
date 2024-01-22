# 54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

*Example 1:*

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

*Example 2:*

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

*Constraints:*
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 10
* -100 <= matrix[i][j] <= 100

## Optimized Solution

### Approach
Create a left, right, top, and bottom variables to use as the boundaries of the matrix. While these pointers don't cross over we iterate the rows/cols in spiral order by using those boundaries in a loop. After each one we update that specific pointer. 

### Complexity
$$Time: O(n*m)$$

$$Space: O(n)$$

### Code
```py
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # get every i in the right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in the left col
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res
```
