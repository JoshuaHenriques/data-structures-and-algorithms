# 11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

*Example 1:*

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

*Example 2:*

```
Input: height = [1,1]
Output: 1
```

*Constraints:*

```
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
```

## Solution

### Approach
Using two pointers at each end of the area pass through the area and calculate the area and assign it to the max if it's bigger than max. If the height/element is bigger on the left side decrement the right pointer and increment if it's the opposite. If they equal the same then decrement and increment the pointers

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def maxArea(self, height: List[int]) -> int:
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        x = r-l
        y = min(height[l], height[r])
        area = x * y
        max_area = max(max_area, area)
        
        if height[l] > height[r]:
            r -= 1
        elif height[l] < height[r]: 
            l += 1
        else:
            l += 1
            r -= 1

    return max_area
```