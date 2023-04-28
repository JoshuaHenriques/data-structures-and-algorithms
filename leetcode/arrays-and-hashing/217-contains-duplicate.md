# Contains Duplicate 

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

*Example 1:*

```
Input: nums = [1,2,3,1]

Output: true
```

*Example 2:*

```
Input: nums = [1,2,3,4]

Output: false
```

*Example: 3*

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
```

## Naive Solution
### Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

### Approach
<!-- Describe your approach to solving the problem. -->
Using a hashmap to keep track which num in nums were seen already, if num is already in the hashmap then return True. If you looped through the whole array without finding num in the hashmap then return False, there's no duplicates
### Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Code
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        
        return False
```

## Optimized Solution
### Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

### Approach
<!-- Describe your approach to solving the problem. -->
Sort array and loop through the array using two pointers to compare the elements for duplicates

### Complexity
- Time complexity: O(nlogn)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Code
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        j = 1
        for i in range(len(nums)):
            if j == len(nums):
                return False
            elif nums[i] == nums[j]:
                return True
            j += 1
```