# 84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

*Example 1:*

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

*Example 2:*

```
Input: heights = [2,4]
Output: 4
```

*Constraints:*

```
1 <= heights.length <= 105
0 <= heights[i] <= 104
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i # we don't know if we can extend it backwards yet
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index # move start index backwards to the one we just popped
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # extends to the end of the histogram

        return maxArea
```