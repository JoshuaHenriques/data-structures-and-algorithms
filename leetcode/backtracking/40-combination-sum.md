# 40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

*Example 1:*

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

*Example 2:*

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

*Constraints:*

```
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
```

## Optimized Solution

### Approach (Decision Tree)
Sort out candidates array to make it easier. Using a helper function since we'll be using recursion. Our parameters will be the curr combination, i the index we're at in the candidates array, and the current total. Base case would be when target and total are the same. Another base case if the current total greater than target. Iterate through the candidates and append it to the current combination and recursively call our helper function with current combination, current total, and the index plus 1. After we pop that candidate from curr and keep track of our previous value so in the next iteration we can skip it if the elements were the same.

### Complexity
$$Time: O(2^n)$$

$$Space: O(n)$$

### Code
```
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    result = []
    def dfs(curr, pos, total):
        if target == total:
            result.append(curr.copy())

        if total > target:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            curr.append(candidates[i])
            dfs(curr, i + 1, total + candidates[i])
            curr.pop()
            prev = candidates[i]

    dfs([], 0, 0)
    return result
```