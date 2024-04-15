# 236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

*Example 1:*

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

*Example 2:*

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

*Example 3:*

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

*Constraints:*

* The number of nodes in the tree is in the range [2, 105].
* -109 <= Node.val <= 109
* All Node.val are unique.
* p != q
* p and q will exist in the tree.

## Solution

### Approach
Each recursive call we check if any root value equals p or q, if it does return that root since a node can be a descendant of itself. If not we recursively call the helper function on the left and right subtree. If the left and right call both return a node then we know that that current node is the LCA however if one of those nodes return null we can return the non-null node.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def helper(root):
        if not root:
            return None
            
        if root.val == p.val or root.val == q.val:
            return root

        left = helper(root.left)
        right = helper(root.right)

        if left and right:
            return root
        elif left and not right:
            return left
        else:
            return right

    return helper(root)
```
