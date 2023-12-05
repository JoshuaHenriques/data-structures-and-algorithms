# Question Name
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

*Example 1:*

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

*Example 2:*

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

*Constraints:*

```
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
```

## Solution

### Approach
Perform a binary search on the first elements of each array in the 2d array, while checking if target is in that array. Once array is found perform another binary search on that array.

### Complexity
$$Time: O(log(n*m))$$

$$Space: O(n)$$

### Code
```
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        arr = []
        while l <= r:
            mid = (l + r) // 2

            if target in matrix[mid]:
                arr = matrix[mid]
                break
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][0]:
                l = mid + 1

        if len(arr) > 0:
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                if target < arr[mid]:
                    r = mid - 1
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    return True
        else:
            return False
```

## Optimized Solution

### Approach
Similar to top solution but with out checking if target is in the middle row. Check if target is greater than the largest value in row or smaller than smallest value in row

### Complexity
$$Time: O(log(n*m))$$

$$Space: O(1)$$

### Code
```
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False
```