# 643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

*Example 1:*

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

*Example 2:*

```
Input: nums = [5], k = 1
Output: 5.00000
```

*Constraints:*

```
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
```

## Naive Solution (Time Limit Exceeded)

### Approach
Sliding window approach by setting a left and right pointer. For each iteration we calculate the sum of that subarray (window) and set the maxAvg.

### Complexity
$$Time: O((n-k)*k)$$

$$Space: O(1)$$

### Code
```
def findMaxAverage(self, nums: List[int], k: int) -> float:
    maxAvg = float("-inf")

    l = 0
    for i in range(k-1, len(nums)):
        currSum = sum(nums[l:i+1])
        maxAvg = max(maxAvg, currSum/k)
        l += 1

    return maxAvg
```

## Solution 1

### Approach
Loop through the array until we hit our window size then we start removing from the beginning of the window and added the new element to the window

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def findMaxAverage(self, nums: List[int], k: int) -> float:
    maxAvg = float("-inf")
    currSum = 0

    for i in range(len(nums)):
        currSum += nums[i]
        if i >= k-1:
            maxAvg = max(maxAvg, currSum/k)
            currSum -= nums[i-k+1]

    return maxAvg
```

## Optimized Solution

### Approach
First for loop is up to k-1 to get our first window sum. Second for loop is from k to the send of the array to compute the other windows. 

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def findMaxAverage(self, nums: List[int], k: int) -> float:
    currSum = 0
    for i in range(k):
        currSum += nums[i]

    maxSum = currSum
    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currSum)

    return maxSum/k
```