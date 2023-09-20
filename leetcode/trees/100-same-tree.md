# 100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

*Example 1:*

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

*Example 2:*

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

*Example 3:*

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

*Constraints:*

```
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
```

## Solution

### Approach
With trees we can use recursion, so the base case will be if both the nodes are null and if one of the nodes aren't null. We first check if both root node values equal to the same thing if so we recursively call the functions using both tree's left nodes together and both tree's right nodes together

### Complexity
$$Time: O(p+q)$$

$$Space: O(h)$$

### Code
```
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == None and q == None:
        return True
    elif not p or not q or p.val != q.val:
        return False

    if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
        return True
```

### Code
```
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return (self.sameTree(p.left, q.left) and
                self.sameTree(p.right, q.right))
    return False
```