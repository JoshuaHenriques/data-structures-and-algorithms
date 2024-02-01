# 1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

*Example 1:*

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

*Example 2:*

```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

*Example 3:*
```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

*Constraints:*
* 1 <= nums.length <= 105
* nums[i] is either 0 or 1.

## Solution

### Approach
Have a variable to track the current number of deletes used. Using two pointers we iterate through the array and if the right pointer is a 0 we decrement the delete tracker. In the same iteration if the delete tracker is less than 0 we shift the window and update the delete tracker is the left pointer was a 0.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def longestSubarray(self, nums: List[int]) -> int:
    delete = 1
    i, j = 0, 0

    while j < len(nums):
        if nums[j] == 0:
            delete -= 1

        if delete < 0:
            if nums[i] == 0:
                delete += 1
            i += 1

        j += 1

    return j - i - 1
```