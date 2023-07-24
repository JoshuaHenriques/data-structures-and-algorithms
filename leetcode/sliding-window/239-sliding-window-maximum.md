# Question Name

*Example 1:*

```

```

*Example 2:*

```

```

*Constraints:*

```

```

## Naive Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
# code
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

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