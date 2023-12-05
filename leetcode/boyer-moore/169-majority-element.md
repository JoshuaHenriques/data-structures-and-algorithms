# 169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

*Example 1:*

```
Input: nums = [3,2,3]
Output: 3
```

*Example 2:*

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

*Constraints:*

```
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
```

## Naive Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def majorityElement(self, nums: List[int]) -> int:
    times = len(nums)//2
    freq = Counter(nums)

    for key in freq:
        if freq[key] > times:
            return key
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def majorityElement(self, nums: List[int]) -> int:
    times = len(nums)//2
    freq = Counter(nums)

    for key in freq:
        if freq[key] > times:
            return key
```