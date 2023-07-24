# 155 Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

*Example 1:*

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

*Constraints:*

```
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
```

## Naive Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def __init__(self):
    self.stack = []

def push(self, val: int) -> None:
    self.stack.append(val)

def pop(self) -> None:
    self.stack.pop()

def top(self) -> int:
    return self.stack[-1]

def getMin(self) -> int:
    return min(self.stack)
```

## Optimized Solution 1

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(1)$$

$$Space: O(n)$$

### Code
```
def __init__(self):
    self.stack = []
    self.min = []

def push(self, val: int) -> None:
    self.stack.append(val)
    if self.min:
        minimum = min(self.min[-1], val)
        if minimum < self.min[-1] or val == minimum:
            self.min.append(minimum)
    else:
        self.min.append(val)
    print(f'self.min: {self.min}')

def pop(self) -> None:
    if self.stack:
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()

def top(self) -> int:
    return self.stack[-1]

def getMin(self) -> int:
    if self.min:
        return self.min[-1]
```

## Optimized Solution 2

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(1)$$

$$Space: O(1)$$

### Code
```
def __init__(self):
    self.stack = []
    self.min = []

def push(self, val: int) -> None:
    self.stack.append(val)
    value = min(val, self.min[-1] if self.min else val)
    self.min.append(value)


def pop(self) -> None:
    self.stack.pop()
    self.min.pop()

def top(self) -> int:
    return self.stack[-1]

def getMin(self) -> int:
    return self.min[-1]
```