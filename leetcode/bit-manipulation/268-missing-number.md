#  268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

*Example 1:*

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

*Example 2:*

```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

*Example 3:*

```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

*Constraints:*

```
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
```

## Solution 1

### Approach
XOR the input array with the range array and the last number left over in the range array is the missing number. Since when you XOR two of the same numbers you get 0 and when you XOR something with 0 you get the original number.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

## Solution 2

### Approach
Get the sum of both arrays and subtract the range with the input array and the missing number will be the answer.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def missingNumber(self, nums: List[int]) -> int:
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]
    return res
```