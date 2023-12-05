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

## Solution (Decision Tree)

### Approach
Using a decision tree approach we create a dfs helper function with the parameters of the index of the current element we're on in the array and the current combination (can be stored outside the helper function). Our only base case of the recursive call is when the index is out of bounds. We then append the current element to the current combination and for our first decision we do a recursive call with pos incremented and our second decision is where we pop the current element from the current combination and do a recursive call.

### Complexity
$$Time: O(2^n)$$

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
    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res
```