# 48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

*Example 1:*

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

*Example 2:*

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

*Constraints:*

* n == matrix.length == matrix[i].length
* 1 <= n <= 20
* -1000 <= matrix[i][j] <= 1000

## Solution

### Approach
Use four pointers/boundaries: left, right, bottom, top. While the l is less than the right pointer we iterate n - 1 through the row. The top and bottom pointer gets updated to be the same as the right and left pointer. To avoid having more than one temporary variables to hold the values we can do the swap in reverse (counter-clockwise) so we only need to keep the first value in a temporary value. Our i index from the loop will be used as an offset for the next set of elements we need to move as the loop goes on.

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```py
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the topLeft
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft

        r -= 1
        l += 1
```
