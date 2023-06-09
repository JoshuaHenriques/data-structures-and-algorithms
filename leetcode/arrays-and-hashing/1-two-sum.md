# Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

*Example 1:*

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

*Example 2:*

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

*Example 3:*

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

*Constraints:*

```
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
```

## Naive Solution

### Approach
Use two loops to add each element with every other element to see if it adds up to the target

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j] 
```

## Optimized Solution

### Approach
Use a hashmap to keep track of the indices and numbers of the nums array. Loop through array and see if "target - number" is in the hashmap then after you add the value to the hashmap to prevent it from counting the first element in the array

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i in range(len(nums)):
        if target-nums[i] in hashmap:
            return [i, hashmap[target-nums[i]]]
        hashmap[nums[i]] = i       
```