# 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.


*Example 1:*

```
Input: s = "()"
Output: true
```

*Example 2:*

```
Input: s = "()[]{}"
Output: true
```

*Example 3:*

```
Input: s = "(]"
Output: false
```


*Constraints:*

```
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

## Naive Solution

### Approach
Pass through array while pushing to the stack, if we find a closing bracket we pop the stack and if it isn't it's corressponding opening bracket then false. If the stack still has something in it then it's also. 

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def isValid(self, s: str) -> bool:
    stack = []

    for b in s:
        if b == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return False
        elif b == "}":
            if len(stack) == 0 or stack.pop() != "{":
                return False
        elif b == "]":
            if len(stack) == 0 or stack.pop() != "[":
                return False
        else:
            stack.append(b)

    if len(stack) > 0:
        return False

    return True
```

## Optimized Solution

### Approach
Same as above but using a hashmap to map the close brackets to open brackets

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def isValid(self, s: str) -> bool:
    stack = []
    hashmap = { ")": "(", "}": "{", "]": "["}

    for b in s:
        if b in hashmap:
            if stack and stack[-1] == hashmap[b]:
                stack.pop()
            else:
                return False
        else:
            stack.append(b)

    return True if not stack else False
```