# Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

*Example 1:*

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

*Example 2:*

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

*Example 3:*

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

*Constraints:*

```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
```

## Solution 1 (TLE)

### Approach
Keep track of the max sum while looping through each subarray.

### Complexity
$$Time: O(n^3)$$

$$Space: O(1)$$

### Code
```
def maxSubArray(self, nums: List[int]) -> int:
    res = float("-inf")
    
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            res = max(res, sum(nums[i:j + 1]))

    return res
```

## Solution 2 (TLE)

### Approach
Same as above but we keep track of the current sum.

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```
def maxSubArray(self, nums: List[int]) -> int:
    res = float("-inf")
    
    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            res = max(res, currSum)

    return res
```

## Solution 3 

### Approach
Same as above but we keep track of the current sum.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```

```
