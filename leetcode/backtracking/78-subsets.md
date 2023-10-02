# 78. Subsets
Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

*Example 1:*

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
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
All the numbers of nums are unique.
```

## Naive Solution

### Approach
For each element that we call our recursive dfs helper function on we make two decisions, a recursive call including the element we're at and excluding the element. So we append the element to our current subset list and then we call it with that list and increment the pointer. The second decision is to call dfs without the current element

### Complexity
$$Time: O(n*2^n)$$

$$Space: O(n)$$

### Code
```
def subsets(self, nums: List[int]) -> List[List[int]]:
    result = [[]]

    def dfs(pos, curr):
        if pos >= len(nums):
            return

        curr.append(nums[pos])
        dfs(pos+1, curr)

        result.append(curr.copy())

        curr.pop()
        dfs(pos+1, curr)
    
    dfs(0, [])
    return result
```

### Code
```
def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []

    subsets = []
    def dfs(pos):
        if pos >= len(nums):
            result.append(subsets.copy())
            return

        # decision to include nums[i]
        subsets.append(nums[pos])
        dfs(pos+1)

        # decision to NOT include nums[i]
        subsets.pop()
        dfs(pos+1)
    
    dfs(0)
    return result
```