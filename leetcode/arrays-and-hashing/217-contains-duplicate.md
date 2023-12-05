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

*Example 3:*

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
```

*Constraints:*

```
1 <= nums.length <= 105
-109 <= nums[i] <= 109
```

## Naive Solution 1

### Approach
Compare each element with the other elements to see if there are any duplicates

### Complexity
$$Time: O(n^2)$$
$$Space: O(1)$$

### Code
```
def containsDuplicate(nums: List[int]) -> bool:
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    
    return False
```

## Naive Solution 2

### Approach
Using a hashmap or a set to keep track which num in nums were seen already, if num is already in the hashmap or set then return True. If you looped through the whole array without finding num in the hashmap or set then return False, there's no duplicates

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)

    return False
```

## Optimized Solution

### Approach
Sort array and loop through the array using two pointers to compare the elements for duplicates

### Complexity
$$Time: O(nlogn)$$

$$Space: O(1)$$

### Code
```
def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    j = 1
    for i in range(len(nums)):
        if j == len(nums):
            return False
        elif nums[i] == nums[j]:
            return True
        j += 1
```