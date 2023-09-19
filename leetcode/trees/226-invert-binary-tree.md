# 226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

*Example 1:*

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

*Example 2:*

```
Input: root = [2,1,3]
Output: [2,3,1]
```

*Example 3:*

```
Input: root = []
Output: []
```

*Constraints:*

```
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

## BFS Solution

### Approach
Using depth first search we can look at the root node and swap the positions of the left and right child and recursively call invertTree on the left and right subtree.

### Complexity
$$Time: O(n)$$

$$Space: O(h)$$

### Code
```
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    temp = root.left
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(temp)

    return root
```

## Iterative Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```

```

## BFS Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```

```