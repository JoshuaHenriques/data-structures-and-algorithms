# 90. Subsets II
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

*Example 1:*

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

*Example 2:*

```
Input: nums = [0]
Output: [[],[0]]
```

*Constraints:*

```
1 <= nums.length <= 10
-10 <= nums[i] <= 10
```

## Naive Solution

### Approach
For each element that we call our recursive dfs helper function on we make two decisions, a recursive call including the element we're at and excluding the element. So we append the element to our current subset list and then we call it with that list and increment the pointer. The second decision is to call dfs without the current element. However since we don't want duplicates we can avoid them in two ways: 1. Sort the array and use tuples when inserting into the result array so before adding to it we can check if that subset is in the result already. 2. Sort the array and when before we recursively call our second decision we increment pass any duplicates in the array

### Complexity
$$Time: O(n*2^n)$$a

$$Space: O(n)$$

### Code
```
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    subsets = []
    def dfs(pos):
        if pos >= len(nums):
            if tuple(subsets.copy()) not in result:
                result.append(tuple(subsets.copy()))
            return

        # All subsets that include nums[i]
        subsets.append(nums[pos])
        dfs(pos+1)

        # All subsets that don't include nums[i]
        subsets.pop()
        dfs(pos+1)

    dfs(0)
    return result
```

### Code
```
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    subsets = []
    def dfs(pos):
        if pos >= len(nums):
            result.append(subsets.copy())
            return

        subsets.append(nums[pos])
        dfs(pos+1)

        while pos + 1 < len(nums) and nums[pos] == nums[pos+1]:
            pos += 1
        subsets.pop()
        dfs(pos+1)

    dfs(0)
    return result
```