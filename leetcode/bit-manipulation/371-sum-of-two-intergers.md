# 371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

*Example 1:*

```
Input: a = 1, b = 2
Output: 3
```

*Example 2:*

```
Input: a = 2, b = 3
Output: 5
```

*Constraints:*

```
-1000 <= a, b <= 1000
```

## Solution

### Approach
XOR each bit of the two numbers, then we AND each bit and shift to the left by 1 to handle the carries (in addition). Then we'll do the same thing with both of those results until there is no carries left.

### Complexity
$$Time: O(1)$$

$$Space: O(1)$$

### Code
```py
def getSum(self, a: int, b: int) -> int:
    def add(a, b):
        if not a or not b:
            return a or b
        return add(a ^ b, (a & b) << 1)

    if a * b < 0:  # assume a < 0, b > 0
        if a > 0:
            return self.getSum(b, a)
        if add(~a, 1) == b:  # -a == b
            return 0
        if add(~a, 1) < b:  # -a < b
            return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

    return add(a, b)  # a*b >= 0 or (-a) > b > 0
```
