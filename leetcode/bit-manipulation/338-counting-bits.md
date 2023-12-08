# 338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

*Example 1:*

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

*Example 2:*

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

*Constraints:*

```
0 <= n <= 105
```

## Naive Solution

### Approach
For each number in range n, we count the number of 1's and append to result array.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def countBits(self, n: int) -> List[int]:
    res = []
    for n in range(0, n + 1):
        cnt = 0
        while n:
            n = n & (n - 1)
            cnt += 1
        res.append(cnt)
    return res
```

## Optimized Solution

### Approach
Refer to Neetcode's video on this type of solution.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def countBits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    
    return dp
```
