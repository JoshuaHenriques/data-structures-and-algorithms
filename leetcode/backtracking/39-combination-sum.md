# 39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

*Example 1:*

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

*Example 2:*

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

*Example 3:*

```
Input: candidates = [2], target = 1
Output: []
```

*Constraints:*

```
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
```

## Solution

### Approach (Decision Tree)
Each dfs step we can make two decisions, where we get all combinations including the element our index is looking at that add to our target value and then get all combinations excluding the element. For the parameters we have, i, which is the index of the element in candidates that we're allowed to choose, curr is the array what elements we added to the current combination, and a current total of them. So the first base case is if the current total equals the target we append it to our result arr (we append the copy of it since we are always mutating the curr array during the algorithm). Second base case is when i is out of bounds or the total is greater than target. To include candidates[i] we append it to the current combination array then recursively call dfs with the updated current array and updated the total plus that element. For the second decision we remove that same candidate from the current combination and call dfs so it won't be included this time and we have to increment the index so it's not looking at that element anymore and keep the total the same since it's excluded now.

### Complexity
$$Time: O(2^target)$$

$$Space: O(n)$$

### Code
```
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(i, curr, total):
        if total == target:
            result.append(curr.copy())
            return

        if i >= len(candidates) or total > target:
            return

        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return result
```