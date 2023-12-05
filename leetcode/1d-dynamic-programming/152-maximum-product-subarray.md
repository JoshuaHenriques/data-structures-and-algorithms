# Question Name

*Example 1:*

```

```

*Example 2:*

```

```

*Example 3:*

```

```

*Constraints:*

```

```

## Naive Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```
def maxProduct(self, nums: List[int]) -> int:
    largProd = float("-inf")

    for i in range(len(nums)):
        largProd = max(largProd, nums[i])
        for j in range(i + 1, len(nums)):
            largProd = max(largProd, prod(nums[i:j+1]))

    return largProd
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```
def maxProduct(self, nums: List[int]) -> int:
    largProd = float("-inf")

    def dfs(i, curr, currProd):
        nonlocal largProd
        if i >= len(nums):
            return
        
        curr.append(nums[i])
        currProd = prod(curr)
        largProd = max(largProd, currProd, nums[i])

        dfs(i + 1, curr.copy(), currProd)
        curr.pop()
        dfs(i + 1, [], 0)

    dfs(0, [], 0)
    return largProd
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def maxProduct(self, nums: List[int]) -> int:
    memo = defaultdict(int)

    def dfs(i, currProd):
        key = (i, currProd)
        if key in memo:
            return memo[key]

        if i >= len(nums):
            return currProd
        
        largProd = max(dfs(i+1, nums[i]*currProd), dfs(i + 1, nums[i]), currProd)
        memo[key] = largProd
        return largProd

    return dfs(1, nums[0])
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue

        tmp = curMax * n
        curMax = max(tmp, n * curMin, n)
        curMin = min(tmp, n * curMin, n)

        res = max(res, curMax)

    return res
```