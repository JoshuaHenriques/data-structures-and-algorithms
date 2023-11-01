# 70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

*Example 1:*

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

*Example 2:*

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

*Constraints:*

```

```

## DFS Decision Tree Solution (Time Limit Exceeded)

### Approach
Using a decision tree we can calculate one step and two steps by recursively calling with n - 1 and n - 2 respectfully. This is very inefficient since the time complexity will be 2^n since there is two decisions being made n times.

### Complexity
$$Time: O(2^n)$$

$$Space: O(1)$$

### Code
```
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

## Memoization Solution

### Approach
Same decision tree as above however we store the computed result in memory do we don't have to re-compute any results in the future. This cuts down the time complexity by from O(2^n) to O(n) but at a cost of using O(n) memory from O(1).

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def climbStairs(self, n: int) -> int:
    memo = {}

    def helper(n, memo):
        if n == 0 or n == 1:
            return 1

        if n not in memo:
            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        
        return memo[n]

    return helper(n, memo)
```

## Bottom-up Approach

### Approach
Starting from the bottom up (5 -> 0) instead of (0 -> 5), we start at the last step. We'll have two variable both initialized as 1. We can loop through n - 1 (range() is not inclusive), since we precomputed n (one) and n - 1 (one variable), and in each iteration one will be updated by adding itself and two and two will be what one used to be. Since the next value we need only needs the last two computed values added together. So the idea is to only remember those last two values at each iteration.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def climbStairs(self, n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one
```