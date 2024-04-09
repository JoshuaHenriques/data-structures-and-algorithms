# Question Name
Given the root of a binary tree, return the inorder traversal of its nodes' values.

*Example 1:*

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

*Example 2:*

```
Input: root = []
Output: []
```

*Example 3:*

```
Input: root = [1]
Output: [1]
```

*Constraints:*

* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100

## Recursive Solution

### Approach
Simple inorder traversal.

### Complexity
$$Time: O(n)$$

$$Space: O(logn)$$

### Code
```py
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def helper(root):
        if not root:
            return

        helper(root.left)
        res.append(root.val)
        helper(root.right)

    helper(root)
    return res
```

## Iterative Solution

### Approach
Loop until stack or root is empty/null. Traverse the leftmost node and push each node into the stack. Pop from the stack to get the root, append to the result, and then assign root the right subtree and repeat.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res, stack = [], []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res
```