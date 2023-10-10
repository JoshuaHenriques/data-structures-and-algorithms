# 543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

*Example 1:*

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

*Example 2:*

```
Input: root = [1,2]
Output: 1
```

*Constraints:*

```
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
```

## Solution

### Approach
Similar to getting the maximum height of a tree. To get the diameter of a tree from a node we add the left and right subtree's diameter and get the max of that and the current diameter. So using recursion, once we end up at a leaf, we return 1 + the max between the left and right. The + 1 is that leafs edge connecting to the parent node. So when we get to a parent node with two children that returned 1 because they are both leafs, we get 2 as the diameter. Then we go back up to the parent node of those nodes.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    diameter = 0
    
    def dfs(root):
        nonlocal diameter
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        diameter = max(left + right, diameter)

        return 1 + max(left, right)

    dfs(root)
    return diameter
```