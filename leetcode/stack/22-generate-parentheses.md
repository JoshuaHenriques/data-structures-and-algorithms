# 22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

*Example 1:*

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

*Example 2:*

```
Input: n = 1
Output: ["()"]
```

*Constraints:*

```
1 <= n <= 8
```

## Optimized Solution

### Approach
Backtracking, add a open parenthesis if open < n, add a close parenthesis if close < open, and return result if open == closed == n

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def generateParenthesis(self, n: int) -> List[str]:
    stack = []
    result = []

    def backtracking(openN, closedN):
        if openN == closedN == n:
            print(f'stack: {stack}')
            result.append("".join(stack))

        if openN < n:
            stack.append("(")
            backtracking(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtracking(openN, closedN + 1)
            stack.pop()

    backtracking(0, 0)
    return result
```