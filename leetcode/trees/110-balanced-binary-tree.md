# 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

*Example 1:*

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

*Example 2:*

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

*Example 3:*

```
Input: root = []
Output: true
```

*Constraints:*

```
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
```

## Optimized Solution

### Approach
Using a dfs helper function we first recursively call to figure out the solution from the bottom up. So we get to the bottom leaf of the left subtree we check if it's left and right subtree is balanced and return and array with the height of the max(left, right) and if it's balanced or not. Doing it this way we can keep track if a subtree wasn't balanced when we make our way back up to the root node. This approach replaces the solution of checking every node if it's balanced before recursively calling the left and right node to check if that's balanced.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def dfs(root):
        if not root:
            return [0, True]

        left = dfs(root.left)
        right = dfs(root.right)
        balanced = abs(left[0] - right[0]) < 2 and (left[1] and right[1])
        
        return [1 + max(left[0], right[0]), balanced]

    return dfs(root)[1]
```