# 239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

*Example 1:*

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

*Example 2:*

```
Input: nums = [1], k = 1
Output: [1]
```

*Constraints:*

```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
```

## Optimized Solution

### Approach
Monotonically Decreasing Queue. While if the right most value in our queue is less than the value we're appending, pop from the queue. Then append the new index in our queue. If our left index is greater than the left most value in our queue, pop left most index deom queue. Make sure our window is at least size k before adding to our result

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # Monotonically Decreasing Queue
    output = []
    q = collections.deque() # hold indices
    l = r = 0

    while r < len(nums):
        # pop smaller values from the que
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        # add r to que    
        q.append(r)

        # remove left index from window
        if l > q[0]:
            q.popleft()

        #
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output
```