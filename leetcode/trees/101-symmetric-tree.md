# Question Name
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

*Example 1:*

```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

*Example 2:*

```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

*Constraints:*
 
* The number of nodes in the tree is in the range [1, 1000].
* -100 <= Node.val <= 100


## Recursive Solution

### Approach
Using a helper function with the parameters for the left and right subtree. We first check if both trees are null, then if one of them is null, and if the values aren't the same for the roots. If any of those are false we know they're not symmetrical. If they're true we can return the result of both of the recursive calls. (left.left, right.right) and (left.right, right.left).

### Complexity
$$Time: O(n)$$

$$Space: O(logn)$$

### Code
```py
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def helper(left, right):
        if not left and not right:
            return True

        if (not left and right) or (left and not right):
            return False

        if left.val != right.val:
            return False

        return helper(left.left, right.right) and helper(left.right, right.left)

    return helper(root.left, root.right)
```

## Iterative Solution

### Approach
Same as above but using a queue instead of recursion

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    queue = deque([(root.left, root.right)])
    while queue:
        left, right = queue.pop()
        if not left and not right:
            continue

        if (not left and right) or (left and not right):
            return False

        if left.val != right.val:
            return False

        queue.append((left.left, right.right)) 
        queue.append((left.right, right.left))

    return True
```