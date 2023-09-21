# 572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

*Example 1:*

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

*Example 2:*

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

*Constraints:*

```
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
```

## Naive Solution

### Approach
Inorder to use recursion we created a bunch of base cases. First check if both root and subRoot equal null, return True. If one of them is null then return False. If both root.val == subRoot.val then we can check if that sub-tree is the same as the other sub-tree by using our isSameTree helper function. Lastly if both root values don't match we recursively call the function twice with the subRoot root node and root's left and right node separetly.

### Complexity
$$Time: O(r*s)$$

$$Space: O(h)$$

### Code
```
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root and not subRoot:
        return True        
    elif not root or not subRoot:
        return False

    if root.val == subRoot.val:
        if self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right):
            return True

    if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
        return True

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
    return False
```

### Code
```
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot: return True
    if not root: return False

    if self.isSameTree(root, subRoot):
        return True

    return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
    return False
```