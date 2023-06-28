# Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

*Example 1:*

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

*Example 2:*

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

*Constraints:*

```
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```

## Optimized Solution

### Approach
Pass through to calculate the prefixs and store them in the result array. Pass through the array again from right to left and multiply the postfix with the prefix that's already in the result array and store it back in the result

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def productExceptSelf(self, nums: List[int]) -> List[int]:
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
```