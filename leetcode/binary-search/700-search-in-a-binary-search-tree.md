# 700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

*Example 1:*

```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

*Example 2:*

```
Input: root = [4,2,7,1,3], val = 5
Output: []
```

*Constraints:*

* The number of nodes in the tree is in the range [1, 5000].
* 1 <= Node.val <= 107
* root is a binary search tree.
* 1 <= val <= 107

## Solution

### Approach
Return if root is None. If val equals the root return the root, if val is greater than the root recursively call with the right subtree, if it's less than recursively call with the left.

### Complexity
$$Time: O(n)$$

$$Space: O(logn)$$

### Code
```py
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None

    if val == root.val:
        return root
    elif val > root.val:
        return self.searchBST(root.right, val)
    else:
        return self.searchBST(root.left, val)

    return self.searchBST(root, val)
```
