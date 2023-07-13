# 42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

*Example 1:*

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

*Example 2:*

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

*Constraints:*

```
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
```

## Failed Solution (Time Limit Exceeded - 321/322)

### Approach
Loop through the list, if we're at the beginning we can loop past all the indices with height 0. For each index onwards we're going to get the max height on the left and the max height on the right so we can get the minimum of the two since the shortest height is the bottleneck of trapping water. After that we subtract that minimum with the height of the index we're on to get the trapped water. Do this for each index and add to the result each time.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def trap(self, height: List[int]) -> int:
    i, res = 0, 0
    while i < len(height):
        if i == 0:
            while i < len(height) and height[i] == 0:
                i += 1

        if i >= len(height):
            break

        if len(height[:i]) == 0:
            left_side = 0
        else:
            left_side = max(height[:i])

        if len(height[i:]) == 0:
            right_side = 0
        else:
            right_side = max(height[i:])

        trapped = min(left_side, right_side) - height[i]
        if trapped > 0:
            res += trapped

        i += 1

    return res
```

## Failed Solution 2 (Time Limit Exceeded - 321/322)

### Approach
Precompute the three arrays used to calculate the trapped water

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def trap(self, height: List[int]) -> int:
    # Algo min(l, r) - height[i]
    max_left = [0] * len(height)
    m_l = 0
    max_right = [0] * len(height)
    m_r = 0
    min_lr = [0] * len(height)
    m_lr = 0

    j = len(height) - 1
    for i in range(len(height)):
        if i == 0:
            continue

        m_l = max(height[0:i])
        max_left[i] = m_l

        m_r = max(height[len(height)-i:len(height)])
        max_right[len(height)-i-1] = m_r

    for i in range(len(height)):
        m_lr = min(max_left[i], max_right[i])
        min_lr[i] = m_lr

    water = 0
    for i in range(len(height)):
        x = min_lr[i] - height[i]
        if x > 0:
            water += x
        print(f'water: {water}, x: {x}, min_lr[i]: {min_lr[i]}, height[i]: {height[i]}')

    return water
```

## Optimized Solution

### Approach
Using two pointers keep track of the max left and right height. Starting with the left, at each height if the max height minus the current height is above zero then we can use that value to add towards the total number of water trapped. Increment the left pointer and continue the next iteration on the side with the minimum max height recorded.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def trap(self, height: List[int]) -> int:
    # Algo min(l, r) - height[i]
    max_l, max_r, water = 0, 0, 0
    i, j = 0, len(height) - 1

    while i <= j:
        if max_l <= max_r:
            max_l = max(max_l, height[i])   
            print(f'max_l: {max_l}')
            print(f'height[i]: {height[i]}')
            if max_l - height[i] > 0:
                water += max_l - height[i]
                print(f'left water: {water}')
            
            i +=1
        else:
            max_r = max(max_r, height[j])
            print(f'max_r: {max_r}')

            if max_r - height[j] > 0:
                water += max_r - height[j]
                print(f'right water: {water}')

            j -= 1
    
    return water
```