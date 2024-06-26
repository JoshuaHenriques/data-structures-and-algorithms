# 554. Brick Wall

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

*Example 1:*

```txt
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
```

*Example 2:*

```txt
Input: wall = [[1],[1],[1]]
Output: 3
```

*Constraints:*

```txt
n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1
```

## Solution

### Approach

Count the gaps of each inner column and store the count in a hashmap. Count the gaps by going through each row and incrementing the counter at each gap, we go to each gap by adding the element to a marker which tells us what inner column we're on. Return the difference between the length of the wall subtracted by the maximum gap in order to get the minimum number of crossed bricks. 

### Complexity

$$Time: O(n*m)$$

$$Space: O(m)$$

### Code

```py
def leastBricks(self, wall: List[List[int]]) -> int:
    countGap = defaultdict(int)

    for i in range(len(wall)):
        marker = 0
        for j in range(len(wall[i]) - 1):
            marker += wall[i][j]
            countGap[marker] += 1

    valueLen = countGap.values()
    maxGap = max(valueLen) if valueLen else 0
    
    return len(wall) - maxGap
```
